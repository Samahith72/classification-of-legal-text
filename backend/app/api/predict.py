from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.app.services.classifier import predict_label

router = APIRouter()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files are supported"
        )

    # Read file content
    content = await file.read()
    text = content.decode("utf-8").strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    # Predict label
    result = predict_label(text)

    return {
        "filename": file.filename,
        "article": result["article"],
        "description": result["description"],
        "confidence": result["confidence"]
    }

