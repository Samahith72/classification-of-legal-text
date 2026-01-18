from fastapi import FastAPI
from backend.app.api.predict import router as predict_router

app = FastAPI(
    title="Legal Text Classification API",
    description="Backend API for classifying legal documents",
    version="1.0.0"
)

app.include_router(predict_router)


@app.get("/")
def root():
    return {"message": "Legal Text Classification API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
