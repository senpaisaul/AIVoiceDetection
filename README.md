# Voice Detection API

A production-ready REST API for detecting AI-generated vs human voice samples.

## Features

- Supports Tamil, English, Hindi, Malayalam, and Telugu
- Base64 MP3 input processing
- Wav2Vec2-based feature extraction
- Binary classification with confidence scores
- Rule-based explanations
- API key authentication
- Health check endpoint

## API Endpoints

### POST /api/voice-detection

Detect if a voice sample is AI-generated or human.

**Headers:**
```
x-api-key: YOUR_SECRET_API_KEY
Content-Type: application/json
```

**Request:**
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "<Base64 encoded MP3>"
}
```

**Response:**
```json
{
  "status": "success",
  "language": "English",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.75,
  "explanation": "Unnatural pitch consistency detected"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your API key in `.env`:
```
API_KEY=your-secret-api-key-here
```

3. Run the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Deployment

The application is configured for deployment on platforms like Render, Railway, or HuggingFace Spaces.

### Docker Deployment

```bash
docker build -t voice-detection-api .
docker run -p 8000:8000 -e API_KEY=your-key voice-detection-api
```

## Supported Languages

- Tamil
- English  
- Hindi
- Malayalam
- Telugu