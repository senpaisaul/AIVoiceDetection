import os
from dotenv import load_dotenv

load_dotenv()

# API Key for authentication
API_KEY = os.environ.get("API_KEY", "your-secret-api-key-here")

# Model configuration
MODEL_CONFIG = {
    "sample_rate": 16000,
    "max_duration": 30,  # seconds
    "confidence_threshold": 0.5
}

# Audio processing settings
AUDIO_CONFIG = {
    "target_sample_rate": 16000,
    "max_file_size_mb": 10
}