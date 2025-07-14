# 🧠 Asistente Web con OpenRouter

Este proyecto es un asistente conversacional basado en **OpenRouter**, diseñado para ejecutarse de forma local. Cuenta con una interfaz web minimalista y un backend en FastAPI que maneja las llamadas a modelos compatibles con la API de OpenAI/OpenRouter.

---

## 🧩 Características

- Frontend en **HTML/CSS/JS** con diseño oscuro y en español.
- Backend en **Python con FastAPI**, configurado para funcionar localmente.
- Script `.bat` para iniciar automáticamente el asistente.
- Soporte para múltiples modelos gratuitos disponibles en OpenRouter.
- Ideal como base para asistentes personales, prototipos o aprendizaje de APIs LLM.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/CarlosEzeQuintana/asistente-web-openrouter.git
cd asistente-web-openrouter
```

---

### 2. Configurar las variables de entorno

Crear un archivo `.env` en la carpeta `backend` con este contenido:

```env
OPENROUTER_API_KEY=tu_key_openrouter
OPENROUTER_MODEL=deepseek/deepseek-r1-0528:free
```

💡 Podés conseguir tu API Key en: https://openrouter.ai/

---

### 3. Crear el script de inicio automático (opcional)

Podés crear un archivo `run_asistente.bat` con este contenido:

```bat
@echo off
REM Activar entorno virtual de Python (si existe)
IF EXIST venv (
    echo Activando entorno virtual...
    call venv\Scripts\activate.bat
) ELSE (
    echo Creando entorno virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
)

REM Instalar dependencias del backend
echo Instalando dependencias del backend...
cd backend
pip install -r requirements.txt
cd ..

REM Ejecutar backend
start cmd /k "cd backend && uvicorn main:app --reload"

REM Abrir frontend
start index.html

echo Asistente iniciado. Esperá unos segundos y accedé a http://127.0.0.1:8000 si querés probar la API directamente.
```

---

## 💻 Uso

1. Hacé doble clic en el `.bat`  
2. Se abre una página web local donde podés hablar con el asistente  
3. ¡Listo! Escribí tu pregunta y el modelo responderá

---

## 🛠️ Tecnologías utilizadas

- 🐍 Python + FastAPI (backend)
- 🌐 HTML + CSS + JS (frontend)
- 🔑 OpenRouter API
- ⚡ Script `.bat` para ejecución local

