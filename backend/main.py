from fastapi import Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from ai.layout_generator import generate_layout
from ai.detector import detect_room
from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()
app.mount("/layouts", StaticFiles(directory="layouts"), name="layouts")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Image uploaded successfully",
        "filename": file.filename
    }
    print(detected)
@app.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...),
    style: str = Form("Modern")
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detected = detect_room(file_path)
    print("Detected:", detected)
    layout_path = "layouts/layout.png"
    generate_layout(detected, layout_path)
    
    print("Selected Style:", style)

    return {
    "objects": detected,
    "layout": "/layouts/layout.png",
    "style": style
}