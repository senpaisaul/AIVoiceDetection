from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
import uvicorn
import os
from typing import Optional
import logging

from model import VoiceDetectionModel
from utils.audio import decode_base64_audio
from config import API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Voice Detection API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model
model = VoiceDetectionModel()

# Supported languages
SUPPORTED_LANGUAGES = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]

class VoiceDetectionRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str
    
    @field_validator('language')
    @classmethod
    def validate_language(cls, v):
        if v not in SUPPORTED_LANGUAGES:
            raise ValueError(f'Language must be one of: {", ".join(SUPPORTED_LANGUAGES)}')
        return v
    
    @field_validator('audioFormat')
    @classmethod
    def validate_audio_format(cls, v):
        if v != "mp3":
            raise ValueError('audioFormat must be "mp3"')
        return v

class VoiceDetectionResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str

class ErrorResponse(BaseModel):
    status: str
    message: str

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail={"status": "error", "message": "Invalid API key or malformed request"}
        )
    return x_api_key

@app.get("/")
async def root():
    return {"message": "Voice Detection API is running", "status": "ok"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/voice-detection", response_model=VoiceDetectionResponse)
async def detect_voice(
    request: VoiceDetectionRequest,
    api_key: str = Depends(verify_api_key)
):
    try:
        # Decode Base64 audio
        waveform, sample_rate = decode_base64_audio(request.audioBase64)
        
        # Run inference
        result = model.predict(waveform, sample_rate, request.language)
        
        return VoiceDetectionResponse(
            status="success",
            language=request.language,
            classification=result["classification"],
            confidenceScore=result["confidence_score"],
            explanation=result["explanation"]
        )
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail={"status": "error", "message": "Invalid API key or malformed request"}
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)