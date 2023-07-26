from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = os.path.join('images',file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}

app.mount("/", StaticFiles(directory="frontend", html=True))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')