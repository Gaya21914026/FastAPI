import pathlib
import os
import shutil
import uuid
from fastapi import UploadFile
from fastapi import UploadFile, File
from fastapi import  File, UploadFile, HTTPException
import shutil
from pathlib import Path
import fitz

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# #Unit:MB
MAX_SIZE_MB=5

def is_pdf(MyFile: UploadFile) -> bool:
    if(pathlib.Path(MyFile.filename).suffix == ".pdf"): return True
    else: return False

def is_validate_file(MyFile: UploadFile) -> bool:
    MyFile.file.seek(0, os.SEEK_END)
    size=MyFile.file.tell() 
    MyFile.file.seek(0)
    return size <= MAX_SIZE_MB * 10**6   


def pdf_to_images(pdf_path, destination="uploads\cvs"):
    doc = fitz.open(pdf_path)
    image_paths = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=300)  
        img_name = f"{os.path.basename(pdf_path)}_{i}.png"
        img_path = os.path.join(destination, img_name)
        pix.save(img_path)
        image_paths.append(img_path)
    return image_paths


def save(file: UploadFile, destination="uploads\cvs"): 
    os.makedirs(destination, exist_ok=True)
    
    if not is_validate_file(file):raise HTTPException(status_code=400, detail="File size > 5MB")
    
    name = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(destination, name)
    with open(file_path, "wb") as buffer: 
         shutil.copyfileobj(file.file, buffer) 

    images = pdf_to_images(file_path, destination)
    os.remove(file_path)

    return {"images": images }


