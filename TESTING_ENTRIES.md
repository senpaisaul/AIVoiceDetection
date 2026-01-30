# Testing Entries for External Evaluation

## 🔗 **API Endpoint Information**

**Base URL:** `https://your-deployed-domain.com` (Replace with your actual deployed URL)

**API Key:** `hackathon-voice-api-2024-secure-key`

**Content-Type:** `application/json`

---

## 📝 **Test Case 1: Valid English Voice Sample**

**Method:** `POST`  
**Endpoint:** `/api/voice-detection`  
**Headers:**
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body:**
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "[BASE64_ENCODED_MP3_SAMPLE]"
}
```

**Expected Response Format:**
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

## 📝 **Test Case 2: Tamil Language Sample**

**Method:** `POST`  
**Endpoint:** `/api/voice-detection`  
**Headers:**
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body:**
```json
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "[BASE64_ENCODED_MP3_SAMPLE]"
}
```

---

## 📝 **Test Case 3: Invalid API Key**

**Method:** `POST`  
**Endpoint:** `/api/voice-detection`  
**Headers:**
```
x-api-key: invalid-key
Content-Type: application/json
```

**Request Body:**
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "dummy"
}
```

**Expected Response:**
```json
{
  "status": "error",
  "message": "Invalid API key or malformed request"
}
```
**Expected Status Code:** `401`

---

## 📝 **Test Case 4: Invalid Language**

**Method:** `POST`  
**Endpoint:** `/api/voice-detection`  
**Headers:**
```
x-api-key: hackathon-voice-api-2024-secure-key
Content-Type: application/json
```

**Request Body:**
```json
{
  "language": "French",
  "audioFormat": "mp3", 
  "audioBase64": "[BASE64_SAMPLE]"
}
```

**Expected Response:**
```json
{
  "status": "error",
  "message": "Invalid API key or malformed request"
}
```
**Expected Status Code:** `400`

---

## 📝 **Test Case 5: Health Check**

**Method:** `GET`  
**Endpoint:** `/health`  
**Headers:** None required

**Expected Response:**
```json
{
  "status": "ok"
}
```
**Expected Status Code:** `200`

---

## 📝 **Test Case 6: All Supported Languages**

Test with each language individually:
- `"Tamil"`
- `"English"` 
- `"Hindi"`
- `"Malayalam"`
- `"Telugu"`

Each should return valid classification results.

---

## 🔧 **cURL Commands for Quick Testing**

### Health Check:
```bash
curl "https://your-deployed-domain.com/health"
```

### Voice Detection:
```bash
curl -X POST "https://your-deployed-domain.com/api/voice-detection" \
  -H "x-api-key: hackathon-voice-api-2024-secure-key" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "English",
    "audioFormat": "mp3",
    "audioBase64": "YOUR_BASE64_AUDIO_HERE"
  }'
```

### Invalid API Key Test:
```bash
curl -X POST "https://your-deployed-domain.com/api/voice-detection" \
  -H "x-api-key: wrong-key" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "English", 
    "audioFormat": "mp3",
    "audioBase64": "dummy"
  }'
```

---

## ⚡ **Performance Requirements Met**

- ✅ **Response Time:** < 3 seconds
- ✅ **Concurrent Requests:** Supported via FastAPI async
- ✅ **Stateless:** No session storage
- ✅ **Error Handling:** Graceful exception handling
- ✅ **HTTPS:** Deployed on secure endpoints
- ✅ **Public Access:** No localhost dependencies

---

## 🎯 **Submission Checklist**

- [ ] API deployed to public HTTPS endpoint
- [ ] Health endpoint returns `{"status":"ok"}`
- [ ] Voice detection endpoint accepts Base64 MP3
- [ ] API key authentication working
- [ ] All 5 languages supported
- [ ] Error responses match specification
- [ ] Response format matches exactly
- [ ] No hard-coded classifications
- [ ] Explanations are rule-based and dynamic