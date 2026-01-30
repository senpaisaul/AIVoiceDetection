import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import logging
from utils.audio import extract_acoustic_features
from config import MODEL_CONFIG

logger = logging.getLogger(__name__)

class VoiceDetectionModel:
    """Main model for AI voice detection using scikit-learn"""
    
    def __init__(self):
        logger.info("Initializing Voice Detection Model")
        
        # Initialize classifier and scaler
        self.classifier = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10
        )
        self.scaler = StandardScaler()
        
        # Initialize with demo training (in production, load trained model)
        self._initialize_model()
        
    def _initialize_model(self):
        """Initialize model with synthetic training data for demo purposes"""
        # In production, you would load pre-trained weights here
        # For demo, we'll create synthetic training data
        logger.info("Initializing model with synthetic training data")
        
        # Create synthetic features for training
        n_samples = 1000
        n_features = 26  # 13 MFCC mean + 13 MFCC std
        
        # Generate synthetic training data
        X_synthetic = np.random.randn(n_samples, n_features)
        y_synthetic = np.random.randint(0, 2, n_samples)
        
        # Fit scaler and classifier
        X_scaled = self.scaler.fit_transform(X_synthetic)
        self.classifier.fit(X_scaled, y_synthetic)
        
        logger.info("Model initialized with synthetic data")
        
    def extract_features(self, waveform: np.ndarray, sample_rate: int):
        """Extract acoustic features from waveform"""
        try:
            # Get acoustic features
            features = extract_acoustic_features(waveform, sample_rate)
            
            # Combine MFCC mean and std into feature vector
            feature_vector = np.concatenate([
                features["mfcc_mean"],
                features["mfcc_std"]
            ])
            
            return feature_vector, features
            
        except Exception as e:
            logger.error(f"Error extracting features: {str(e)}")
            # Return dummy features as fallback
            return np.random.randn(26), {
                "mfcc_mean": np.zeros(13),
                "mfcc_std": np.zeros(13),
                "pitch_variance": 0,
                "spectral_centroid_mean": 0,
                "spectral_flatness_mean": 0
            }
    
    def generate_explanation(self, acoustic_features: dict, confidence_score: float):
        """Generate rule-based explanation"""
        explanations = []
        
        # Check pitch variance
        if acoustic_features["pitch_variance"] < 100:
            explanations.append("Unnatural pitch consistency detected")
        
        # Check spectral flatness
        if acoustic_features["spectral_flatness_mean"] > 0.5:
            explanations.append("Synthetic spectral characteristics detected")
        
        # Check spectral centroid
        if acoustic_features["spectral_centroid_mean"] > 3000:
            explanations.append("Artificial frequency distribution patterns")
        
        # Default explanation
        if not explanations:
            if confidence_score > 0.7:
                explanations.append("Strong synthetic voice indicators detected")
            elif confidence_score < 0.3:
                explanations.append("Natural speech variability detected")
            else:
                explanations.append("Mixed acoustic characteristics observed")
        
        return "; ".join(explanations)
    
    def predict(self, waveform: np.ndarray, sample_rate: int, language: str):
        """Main prediction function"""
        try:
            # Extract features
            feature_vector, acoustic_features = self.extract_features(waveform, sample_rate)
            
            # Scale features
            feature_vector_scaled = self.scaler.transform(feature_vector.reshape(1, -1))
            
            # Get prediction probability
            confidence_score = self.classifier.predict_proba(feature_vector_scaled)[0][1]
            
            # Apply heuristic adjustments based on acoustic features
            confidence_score = self._apply_heuristics(confidence_score, acoustic_features)
            
            # Determine classification
            classification = "AI_GENERATED" if confidence_score >= MODEL_CONFIG["confidence_threshold"] else "HUMAN"
            
            # Generate explanation
            explanation = self.generate_explanation(acoustic_features, confidence_score)
            
            return {
                "classification": classification,
                "confidence_score": float(confidence_score),
                "explanation": explanation
            }
            
        except Exception as e:
            logger.error(f"Error in prediction: {str(e)}")
            # Return default response on error
            return {
                "classification": "HUMAN",
                "confidence_score": 0.3,
                "explanation": "Unable to analyze audio characteristics"
            }
    
    def _apply_heuristics(self, base_score: float, acoustic_features: dict):
        """Apply heuristic adjustments to base prediction"""
        score = base_score
        
        # Adjust based on acoustic features
        if acoustic_features["pitch_variance"] < 100:
            score += 0.15
        
        if acoustic_features["spectral_flatness_mean"] > 0.5:
            score += 0.1
        
        if acoustic_features["spectral_centroid_mean"] > 3000:
            score += 0.05
        
        # Clamp to [0, 1]
        return max(0.0, min(1.0, score))