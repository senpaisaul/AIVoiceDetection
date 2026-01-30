# 🧪 EXTERNAL TEST ENTRIES

## 🔗 API ENDPOINT INFORMATION

**You need to deploy first, then replace with your actual URL**

**Base URL**: `https://your-deployed-app.onrender.com` (or Railway/HuggingFace)
**API Key**: `hackathon-voice-api-2024-secure-key`
**Content-Type**: `application/json`

---

## 📝 TEST ENTRY 1: Health Check

**Method**: `GET`
**URL**: `https://your-deployed-app.onrender.com/health`
**Headers**: None required

**Expected Response**:
```json
{
  "status": "ok"
}
```

---

## 📝 TEST ENTRY 2: Valid Voice Detection

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
}
```

**Expected Response Format**:
```json
{
  "status": "success",
  "language": "English",
  "classification": "AI_GENERATED" | "HUMAN",
  "confidenceScore": 0.0-1.0,
  "explanation": "Descriptive explanation text"
}
```

---

## 📝 TEST ENTRY 3: Invalid API Key

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: invalid-key-test
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "dummy-data"
}
```

**Expected Response**:
```json
{
  "status": "error",
  "message": "Invalid API key or malformed request"
}
```
**Expected Status Code**: `401`

---

## 📝 TEST ENTRY 4: Invalid Language

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "French",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0I"
}
```

**Expected Response**:
```json
{
  "status": "error",
  "message": "Invalid API key or malformed request"
}
```
**Expected Status Code**: `400`

---

## 📝 TEST ENTRY 5: Tamil Language

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
}
```

---

## 📝 TEST ENTRY 6: Hindi Language

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "Hindi",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
}
```

---

## 📝 TEST ENTRY 7: Malayalam Language

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "Malayalam",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
}
```

---

## 📝 TEST ENTRY 8: Telugu Language

**Method**: `POST`
**URL**: `https://your-deployed-app.onrender.com/api/voice-detection`
**Headers**:
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body**:
```json
{
  "language": "Telugu",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
}
```

---

## 🚀 QUICK DEPLOYMENT STEPS

### 1. Deploy to Render (5 minutes):
1. Push code to GitHub
2. Go to https://dashboard.render.com/
3. "New" → "Web Service" → Connect GitHub
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Environment Variable**: `API_KEY` = `hackathon-voice-api-2024-secure-key`

### 2. Get Your URL:
After deployment, Render gives you a URL like:
`https://voice-detection-api-xyz.onrender.com`

### 3. Replace URLs:
Replace `https://your-deployed-app.onrender.com` with your actual URL in all test entries above.

---

## ✅ VERIFICATION

Test the health endpoint first:
```bash
curl "https://your-actual-url.onrender.com/health"
```

Should return: `{"status":"ok"}`

Then use the test entries above for external evaluation.

---

## 🎯 SUBMISSION FORMAT

**API Endpoint**: `https://your-actual-url.onrender.com`
**API Key**: `hackathon-voice-api-2024-secure-key`
**Supported Languages**: Tamil, English, Hindi, Malayalam, Telugu
**Response Time**: < 3 seconds
**Authentication**: x-api-key header required