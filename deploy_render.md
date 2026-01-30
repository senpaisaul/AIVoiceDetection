# Quick Render Deployment

## Steps:
1. Push this code to GitHub repository
2. Go to https://dashboard.render.com/
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Use these exact settings:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Environment Variables:**
- `API_KEY` = `hackathon-voice-api-2024-secure-key`

## Your API will be live at:
`https://your-service-name.onrender.com`

## Test immediately with:
```bash
curl -X POST "https://your-service-name.onrender.com/health"
```