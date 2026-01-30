import requests
import base64
import json

# Test the API with the sample MP3 file
def test_api():
    # Read the sample MP3 file
    try:
        with open("sample voice 1.mp3", "rb") as f:
            audio_data = f.read()
        
        # Encode to Base64
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        
        # API endpoint
        url = "http://localhost:8000/api/voice-detection"
        
        # Headers
        headers = {
            "x-api-key": "your-secret-api-key-here",
            "Content-Type": "application/json"
        }
        
        # Request payload
        payload = {
            "language": "English",
            "audioFormat": "mp3",
            "audioBase64": audio_base64
        }
        
        # Make request
        response = requests.post(url, headers=headers, json=payload)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get("http://localhost:8000/health")
        print(f"Health Check - Status Code: {response.status_code}")
        print(f"Health Response: {response.json()}")
    except Exception as e:
        print(f"Health check error: {str(e)}")

def test_invalid_api_key():
    """Test with invalid API key"""
    try:
        url = "http://localhost:8000/api/voice-detection"
        headers = {
            "x-api-key": "invalid-key",
            "Content-Type": "application/json"
        }
        payload = {
            "language": "English",
            "audioFormat": "mp3",
            "audioBase64": "dummy"
        }
        
        response = requests.post(url, headers=headers, json=payload)
        print(f"Invalid API Key Test - Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except Exception as e:
        print(f"Invalid API key test error: {str(e)}")

if __name__ == "__main__":
    print("Testing Voice Detection API...")
    print("\n1. Health Check:")
    test_health()
    
    print("\n2. Invalid API Key Test:")
    test_invalid_api_key()
    
    print("\n3. Voice Detection Test:")
    test_api()