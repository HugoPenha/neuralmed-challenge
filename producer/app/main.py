import base64
import os.path

from fastapi import FastAPI, HTTPException, UploadFile

from .services import publish

app = FastAPI()

ACCEPTABLE_IMAGE_EXTENSIONS = ['.png' , '.jpeg', '.jpg']

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    file_extension = os.path.splitext(file.filename)[1]

    if file_extension not in ACCEPTABLE_IMAGE_EXTENSIONS:
        raise HTTPException(status_code=415, detail="Invalid image extension")
    
    #encode image to send through rabbitmq
    contents = await file.read()
    encoded_data = base64.b64encode(contents)
    encoded_string = encoded_data.decode('ascii')  

    data = {
        "file_name" : file.filename,
        "file_content" : encoded_string
    }

    publish(data)
    return {"message": 'Uploaded successfully', 'image' : file.filename}