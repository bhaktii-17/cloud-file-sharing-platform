from fastapi import FastAPI, UploadFile, File
from app.s3_service import (
    upload_file,
    list_files,
    generate_download_url,
    delete_file
)

app = FastAPI(
    title="Cloud File Sharing Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Cloud File Sharing Platform Running Successfully"
    }

@app.get("/files")
def get_files():
    return {
        "files": list_files()
    }

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    upload_file(file.file, file.filename)

    return {
        "message": f"{file.filename} uploaded successfully"
    }

@app.get("/download/{filename}")
def download_file(filename: str):
    return {
        "download_url": generate_download_url(filename)
    }
@app.delete("/delete/{filename}")
def remove_file(filename: str):
    delete_file(filename)

    return {
        "message": f"{filename} deleted successfully"
    }
