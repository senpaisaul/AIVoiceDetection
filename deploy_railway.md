# Quick Railway Deployment

## Steps:
1. Push code to GitHub
2. Go to https://railway.app/
3. Click "Deploy from GitHub repo"
4. Select your repo
5. Set environment variable:
   - `API_KEY` = `hackathon-voice-api-2024-secure-key`

## Your API will be live at:
`https://your-project-name.up.railway.app`

## Test with:
```bash
curl "https://your-project-name.up.railway.app/health"
```