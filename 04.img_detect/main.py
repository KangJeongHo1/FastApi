from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
from predict import predict

app = FastAPI()

@app.post('/predict/image')
async def predict_img(file: UploadFile=File(...)):
    
    img = Image.open(BytesIO(await file.read()))
    result = predict(img)

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
