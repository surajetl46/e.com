# app/__init__.py
from .data_preprocessing import load_data, preprocess_data
from .model_training import train_collaborative_filtering
from .hybrid_recommendation import hybrid_recommendation
from .evaluation import evaluate_model
