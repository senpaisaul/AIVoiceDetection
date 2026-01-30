import base64
import io
import librosa
import numpy as np
from pydub import AudioSegment
from config import AUDIO_CONFIG
import logging

logger = logging.getLogger(__name__)

def decode_base64_audio(base64_string: str):
    """
    Decode Base64 MP3 to waveform without modifying audio content.
    Only resamples to 16kHz if required by model.
    """
    try:
        # Validate Base64 format
        if not base64_string or len(base64_string) < 10:
            raise ValueError("Base64 string too short or empty")
        
        # Decode Base64
        try:
            audio_bytes = base64.b64decode(base64_string, validate=True)
        except Exception as e:
            raise ValueError(f"Invalid Base64 format: {str(e)}")
        
        if len(audio_bytes) < 100:  # Minimum reasonable MP3 size
            raise ValueError("Decoded audio data too small")
        
        # Load MP3 using pydub
        audio_segment = AudioSegment.from_mp3(io.BytesIO(audio_bytes))
        
        # Convert to numpy array
        samples = np.array(audio_segment.get_array_of_samples())
        
        # Handle stereo audio
        if audio_segment.channels == 2:
            samples = samples.reshape((-1, 2))
            samples = samples.mean(axis=1)  # Convert to mono
        
        # Normalize to [-1, 1]
        samples = samples.astype(np.float32) / 32768.0
        
        original_sr = audio_segment.frame_rate
        target_sr = AUDIO_CONFIG["target_sample_rate"]
        
        # Resample only if necessary
        if original_sr != target_sr:
            samples = librosa.resample(samples, orig_sr=original_sr, target_sr=target_sr)
        
        logger.info(f"Audio decoded: {len(samples)} samples at {target_sr}Hz")
        return samples, target_sr
        
    except Exception as e:
        logger.error(f"Error decoding audio: {str(e)}")
        raise ValueError("Invalid Base64 audio data")

def extract_acoustic_features(waveform: np.ndarray, sample_rate: int):
    """
    Extract acoustic features for explanation generation.
    """
    try:
        # MFCC features
        mfccs = librosa.feature.mfcc(y=waveform, sr=sample_rate, n_mfcc=13)
        
        # Pitch variance
        pitches, magnitudes = librosa.piptrack(y=waveform, sr=sample_rate)
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        
        pitch_variance = np.var(pitch_values) if pitch_values else 0
        
        # Spectral features
        spectral_centroids = librosa.feature.spectral_centroid(y=waveform, sr=sample_rate)[0]
        spectral_flatness = librosa.feature.spectral_flatness(y=waveform)[0]
        
        return {
            "mfcc_mean": np.mean(mfccs, axis=1),
            "mfcc_std": np.std(mfccs, axis=1),
            "pitch_variance": pitch_variance,
            "spectral_centroid_mean": np.mean(spectral_centroids),
            "spectral_flatness_mean": np.mean(spectral_flatness)
        }
        
    except Exception as e:
        logger.error(f"Error extracting features: {str(e)}")
        return {
            "mfcc_mean": np.zeros(13),
            "mfcc_std": np.zeros(13),
            "pitch_variance": 0,
            "spectral_centroid_mean": 0,
            "spectral_flatness_mean": 0
        }