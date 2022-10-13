from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')