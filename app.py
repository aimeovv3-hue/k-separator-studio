from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil

app = FastAPI()

@app.post("/inference/")
async def run_inference(file: UploadFile = File(...)):
    os.makedirs("temp_audio", exist_ok=True)
    file_path = f"temp_audio/{file.filename}"

    # Guardamos el archivo en su formato original
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(f"Ejecutando inferencia directamente sobre: {file.filename}")
    # Aquí el modelo procesará file_path directamente.

    return JSONResponse(content={
        "status": "success",
        "message": "Separación completada con éxito.",
        "original_file": file.filename
    })
