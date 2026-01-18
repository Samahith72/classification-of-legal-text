from fastapi import FastAPI

app = FastAPI(
    title="Legal Text Classification API",
    description="Backend API for classifying legal documents",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Legal Text Classification API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
