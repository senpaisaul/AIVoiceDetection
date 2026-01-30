#!/bin/bash

# External Testing Script for Voice Detection API
# Replace YOUR_DEPLOYED_URL with your actual deployment URL

BASE_URL="https://YOUR_DEPLOYED_URL.onrender.com"
API_KEY="hackathon-voice-api-2024-secure-key"

echo "🧪 Testing Voice Detection API"
echo "================================"

# Test 1: Health Check
echo "1. Health Check..."
curl -s "$BASE_URL/health" | jq '.'
echo ""

# Test 2: Valid Voice Detection
echo "2. Valid Voice Detection (English)..."
curl -s -X POST "$BASE_URL/api/voice-detection" \
  -H "x-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "English",
    "audioFormat": "mp3",
    "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
  }' | jq '.'
echo ""

# Test 3: Invalid API Key
echo "3. Invalid API Key Test..."
curl -s -X POST "$BASE_URL/api/voice-detection" \
  -H "x-api-key: invalid-key" \
  -H "Content-Type: application/json" \
  -d '{"language": "English", "audioFormat": "mp3", "audioBase64": "dummy"}' | jq '.'
echo ""

# Test 4: Invalid Language
echo "4. Invalid Language Test..."
curl -s -X POST "$BASE_URL/api/voice-detection" \
  -H "x-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"language": "French", "audioFormat": "mp3", "audioBase64": "dummy"}' | jq '.'
echo ""

# Test 5: Tamil Language
echo "5. Tamil Language Test..."
curl -s -X POST "$BASE_URL/api/voice-detection" \
  -H "x-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "language": "Tamil",
    "audioFormat": "mp3",
    "audioBase64": "SUQzBAAAAAECBVRTU0UAAAAOAAADTGF2ZjYwLjE2LjEwMEdFT0IAAQFjAAADYXBwbGljYXRpb24veC1jMnBhLW1hbmlmZXN0LXN0b3JlAGMycGEAYzJwYSBtYW5pZmVzdCBzdG9yZQAAAECnanVtYgAAAB5qdW1kYzJwYQARABCAAACqADibcQNjMnBhAAAAQIFqdW1iAAAAR2p1bWRjMm1hABEAEIAAAKoAOJtxA3VybjpjMnBhOjkxNTY2OTZkLTVlNjktNDA3ZS1iY2FiLWYwNzYwZGY4OThiOAAAAAJ7anVtYgAAAClqdW1kYzJhcwARABCAAACqADibcQNjMnBhLmFzc2VydGlvbnMAAAAAy2p1bWIAAAApanVtZGNib3IAEQAQgAAAqgA4m3EDYzJwYS5hY3Rpb25zLnYyAAAAAJpjYm9yoWdhY3Rpb25zgaNmYWN0aW9ubGMycGEuY3JlYXRlZG1zb2Z0d2FyZUFnZW50akVsZXZlbkxhYnNxZGlnaXRhbFNvdXJjZVR5cGV4Rmh0dHA6Ly9jdi5pcHRjLm9yZy9uZXdzY29kZXMvZGlnaXRhbHNvdXJjZXR5cGUvdHJhaW5lZEFsZ29yaXRobWljTWVkaWE"
  }' | jq '.'
echo ""

echo "✅ Testing Complete!"
echo "Replace YOUR_DEPLOYED_URL with your actual deployment URL"