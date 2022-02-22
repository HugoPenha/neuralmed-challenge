import base64

from fastapi import FastAPI, UploadFile

from .services import publish

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    
    #encode image to send through rabbitmq
    contents = await file.read()
    encoded_data = base64.b64encode(contents)
    encoded_string = encoded_data.decode('ascii')  

    data = {
        "file_name" : file.filename,
        "file_content" : encoded_string
    }

    publish('images', data)
    return {"message": 'Upload successfully', 'image' : file.filename}