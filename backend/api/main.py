import os
import shutil
import time
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.model.resume_ranker import ResumeRanker

UPLOAD_DIR = "backend/data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()
ranker = ResumeRanker(upload_dir=UPLOAD_DIR)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:8501"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Upload successful", "filename": file.filename}

@app.post("/rank")
async def rank_resumes(payload: dict):
    start = time.time()
    results = ranker.rank_resumes(
        job_description=payload.get("job_description", ""),
        min_score=payload.get("min_score", 0.3),
        max_results=payload.get("max_results", 10)
    )
    return {
        "matches": results,
        "processing_time": f"{time.time() - start:.2f}s"
    }
