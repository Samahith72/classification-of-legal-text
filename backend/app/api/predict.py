from fastapi import APIRouter
from backend.app.api.schemas import PredictionRequest, PredictionResponse
from backend.app.services.classifier import predict_label

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    label = predict_label(request.text)
    return {"label": label}
