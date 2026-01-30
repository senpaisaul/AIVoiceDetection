#!/usr/bin/env python3
"""
Example client for Voice Detection API
"""

import requests
import base64
import json
import sys

class VoiceDetectionClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        
    def detect_voice(self, audio_file_path, language="English"):
        """
        Detect if voice in audio file is AI-generated or human
        
        Args:
            audio_file_path: Path to MP3 file
            language: One of Tamil, English, Hindi, Malayalam, Telugu
            
        Returns:
            dict: API response
        """
        try:
            # Read and encode audio file
            with open(audio_file_path, "rb") as f:
                audio_data = f.read()
            
            audio_base64 = base64.b64encode(audio_data).decode('utf-8')
            
            # Prepare request
            url = f"{self.api_url}/api/voice-detection"
            headers = {
                "x-api-key": self.api_key,
                "Content-Type": "application/json"
            }
            
            payload = {
                "language": language,
                "audioFormat": "mp3",
                "audioBase64": audio_base64
            }
            
            # Make request
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"API request failed with status {response.status_code}",
                    "details": response.text
                }
                
        except Exception as e:
            return {"error": str(e)}
    
    def health_check(self):
        """Check API health"""
        try:
            response = requests.get(f"{self.api_url}/health")
            return response.json()
        except Exception as e:
            return {"error": str(e)}

def main():
    # Configuration
    API_URL = "http://localhost:8000"  # Change to your deployed URL
    API_KEY = "your-secret-api-key-here"  # Change to your API key
    
    if len(sys.argv) != 2:
        print("Usage: python example_client.py <path_to_mp3_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    # Initialize client
    client = VoiceDetectionClient(API_URL, API_KEY)
    
    # Health check
    print("Checking API health...")
    health = client.health_check()
    print(f"Health: {health}")
    
    if "error" in health:
        print("API is not healthy. Exiting.")
        sys.exit(1)
    
    # Detect voice
    print(f"\nAnalyzing audio file: {audio_file}")
    result = client.detect_voice(audio_file, language="English")
    
    if "error" in result:
        print(f"Error: {result['error']}")
        if "details" in result:
            print(f"Details: {result['details']}")
    else:
        print("\n" + "="*50)
        print("VOICE DETECTION RESULTS")
        print("="*50)
        print(f"Language: {result['language']}")
        print(f"Classification: {result['classification']}")
        print(f"Confidence Score: {result['confidenceScore']:.3f}")
        print(f"Explanation: {result['explanation']}")
        print("="*50)

if __name__ == "__main__":
    main()