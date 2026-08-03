import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="K-Separator Studio API Completa")

# Permitir conexiones desde tu app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = "/tmp/kseparator/"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/api/v1/separate")
async def separate_audio(
    file: UploadFile = File(...),
    model_type: str = Form("VOCALS-MelBand-Roformer"), # Modelo por defecto
    shifts: int = Form(1),
    overlap: float = Form(0.5)
):
    """
    Endpoint que recibe el archivo, el modelo elegido y los ajustes de calidad.
    """
    if not file.filename.endswith(('.flac', '.mp3', '.m4a', '.wav')):
        raise HTTPException(status_code=400, detail="Formato inválido.")
    
    file_path = os.path.join(TEMP_DIR, file.filename)
    
    try:
        # 1. Guardar archivo
        with open(file_path, "wb") as f:
            f.write(await file.read())
            
        # 2. Aquí conectas TU LÓGICA DE SEPARACIÓN enviando los parámetros
        print(f"Iniciando {model_type} con {shifts} shifts y {overlap} overlap...")
        # stems_paths = run_separation(file_path, model=model_type, shifts=shifts, overlap=overlap)
        
        # 3. Simulación de respuesta
        return {
            "status": "success",
            "model_used": model_type,
            "settings": {"shifts": shifts, "overlap": overlap},
            "stems": {
                "vocals": f"https://tu-url-en-render.onrender.com/descargas/voc_{file.filename}",
                "instrumental": f"https://tu-url-en-render.onrender.com/descargas/inst_{file.filename}"
            }
        }
        
    finally:
        if os.path.exists(file_path):
            os.remove(file_path) # Limpieza estricta de RAM/Disco
