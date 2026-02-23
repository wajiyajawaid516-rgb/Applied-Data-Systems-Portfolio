"""
OmniClassify AI Backend — FastAPI

Serves text categorization predictions using multiple model backends.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI(title="OmniClassify AI", version="1.0.0")

class TextRequest(BaseModel):
    text: str
    model_type: str  # e.g., 'SVM', 'Random Forest', 'Naive Bayes'

class PredictionEntry(BaseModel):
    category: str
    probability: float

class PredictionResponse(BaseModel):
    model_used: str
    top_predictions: List[PredictionEntry]
    performance_metrics: Dict

# Mock categories for the 20-category project
CATEGORIES = [
    "Alt.Atheism", "Comp.Graphics", "Comp.Os.Ms-Windows.Misc", 
    "Comp.Sys.Ibm.Pc.Hardware", "Comp.Sys.Mac.Hardware", "Comp.Windows.X", 
    "Misc.Forsale", "Rec.Autos", "Rec.Motorcycles", "Rec.Sport.Baseball", 
    "Rec.Sport.Hockey", "Sci.Crypt", "Sci.Electronics", "Sci.Med", 
    "Sci.Space", "Soc.Religion.Christian", "Talk.Politics.Guns", 
    "Talk.Politics.Mideast", "Talk.Politics.Misc", "Talk.Religion.Misc"
]

@app.get("/")
async def root():
    return {"status": "OmniClassify AI Engine Live", "categories_count": 20}

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # In a real scenario, we would load the serialized model here
    # and run model.predict_proba(). For this portfolio version, 
    # we simulate the inference logic of your 20-category models.
    
    # 1. Select mock probabilities
    top_indices = random.sample(range(20), 5)
    probs = sorted([random.uniform(0.01, 0.8) for _ in range(5)], reverse=True)
    
    predictions = [
        PredictionEntry(category=CATEGORIES[idx], probability=round(prob, 3))
        for idx, prob in zip(top_indices, probs)
    ]
    
    # 2. Mock performance metrics specific to the selected model
    metrics = {
        "Random Forest": {"accuracy": 0.89, "f1_score": 0.88, "latency_ms": 45},
        "SVM": {"accuracy": 0.92, "f1_score": 0.91, "latency_ms": 120},
        "Naive Bayes": {"accuracy": 0.84, "f1_score": 0.83, "latency_ms": 12}
    }.get(request.model_type, {"accuracy": 0.85, "f1_score": 0.84, "latency_ms": 50})

    return PredictionResponse(
        model_used=request.model_type,
        top_predictions=predictions,
        performance_metrics=metrics
    )
