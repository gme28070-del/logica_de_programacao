from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import uvicorn

app = FastAPI()

# Configuração CORS (para desenvolvimento)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

VALID_CODE = "LOGICA2024"
SECRET_TOKEN = "token_secreto_123"

class CodeCheck(BaseModel):
    code: str

@app.post("/api/verify")
async def verify_code(data: CodeCheck):
    if data.code.strip().upper() == VALID_CODE:
        return JSONResponse({
            "access": True,
            "token": SECRET_TOKEN,
            "redirect": "/dashboard.html"
        })
    raise HTTPException(status_code=403, detail="Código inválido")

@app.get("/")
async def serve_index():
    return FileResponse("index.html")

@app.get("/dashboard.html")
async def serve_dashboard():
    return FileResponse("dashboard.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)