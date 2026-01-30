# Deployment Guide

## Quick Deploy Options

### 1. Render (Recommended)

1. Fork this repository to your GitHub account
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - `API_KEY`: Set your secret API key

### 2. Railway

1. Fork this repository
2. Go to [Railway](https://railway.app/)
3. Click "Deploy from GitHub repo"
4. Select your forked repository
5. Set environment variable:
   - `API_KEY`: Your secret API key

### 3. HuggingFace Spaces

1. Create a new Space on [HuggingFace](https://huggingface.co/spaces)
2. Choose "Gradio" as SDK (we'll modify it)
3. Upload all files from this repository
4. Create `app.py`:

```python
import subprocess
import sys
import os

# Set API key
os.environ["API_KEY"] = "your-secret-api-key-here"

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn
    from main import app
    uvicorn.run(app, host="0.0.0.0", port=7860)
```

### 4. Docker Deployment

```bash
# Build the image
docker build -t voice-detection-api .

# Run the container
docker run -p 8000:8000 -e API_KEY=your-secret-key voice-detection-api
```

## Environment Variables

- `API_KEY`: Your secret API key for authentication
- `PORT`: Port number (automatically set by most platforms)

## Testing Your Deployment

Once deployed, test your API:

```bash
curl -X POST "https://your-domain.com/api/voice-detection" \
  -H "x-api-key: your-secret-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "English",
    "audioFormat": "mp3", 
    "audioBase64": "your-base64-encoded-mp3"
  }'
```

## Health Check

```bash
curl "https://your-domain.com/health"
```

Should return: `{"status":"ok"}`