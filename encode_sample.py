#!/usr/bin/env python3
"""
Encode the sample MP3 file to Base64 for testing
"""

import base64

def encode_sample_audio():
    """Encode sample voice 1.mp3 to Base64"""
    try:
        with open("sample voice 1.mp3", "rb") as f:
            audio_data = f.read()
        
        # Encode to Base64
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        
        # Save to file for easy copying
        with open("sample_base64.txt", "w") as f:
            f.write(audio_base64)
        
        print(f"✅ Sample audio encoded to Base64")
        print(f"📁 Saved to: sample_base64.txt")
        print(f"📊 Original size: {len(audio_data)} bytes")
        print(f"📊 Base64 size: {len(audio_base64)} characters")
        
        # Show first 100 characters as preview
        print(f"\n🔍 Preview (first 100 chars):")
        print(audio_base64[:100] + "...")
        
        return audio_base64
        
    except FileNotFoundError:
        print("❌ Error: 'sample voice 1.mp3' not found")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

if __name__ == "__main__":
    encode_sample_audio()