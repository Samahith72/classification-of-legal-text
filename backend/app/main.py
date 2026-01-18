from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.predict import router as predict_router

app = FastAPI(
    title="Legal Text Classification API",
    description="Backend API for classifying legal documents",
    version="1.0.0"
)

# ✅ CORS Configuration
origins = [
    "http://localhost:3000",  # React (CRA)
    "http://localhost:5173",  # React (Vite)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(predict_router)


@app.get("/")
def root():
    return {"message": "Legal Text Classification API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
