from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
app = FastAPI(title="Servidor de datos importantes")
@app.get("/")
def rickroll():
    return RedirectResponse(
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )