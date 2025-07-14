from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configuracion para que el front pueda tirar request
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cliente OpenRouter (OpenAI era la idea - Termino siendo Deepseek)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost",
        "X-Title": "Asistente Web OpenRouter"
    }
)

# Modelo elegido
modelo = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-r1-0528:free")


class Mensaje(BaseModel):
    mensaje: str


@app.post("/chat")
async def chat(m: Mensaje):
    try:
        respuesta = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": "Sos un asistente útil que responde en español."},
                {"role": "user", "content": m.mensaje}
            ],
            max_tokens=512,
            temperature=0.7
        )
        contenido = respuesta.choices[0].message.content.strip()
        return {"respuesta": contenido}
    except Exception as e:
        return {"error": str(e)}
