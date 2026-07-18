from fastapi import FastAPI, status
from pydantic import BaseModel
import requests
app = FastAPI(title="Busqueda de usuarios")
class Usuario(BaseModel):
    User:str
@app.get("/")
def bienvenida():
    return "bienvenido busqueda de usuarios"
@app.post("/buscar", status_code=status.HTTP_201_CREATED)
def buscar(user:Usuario):
    redes_sociales = {
        "yootube":f"https://www.youtube.com/@{user.User}",
        "instagran":f"https://www.instagram.com/{user.User}",
        "tiktok":f"https://www.tiktok.com/@{user.User}",
        "github":f"https://github.com/{user.User}",
        "X":f"https://x.com/{user.User}?lang=es",
        "Facebook":f"https://es-la.facebook.com/{user.User}",
        "pinterest": f"https://pinterest.com/{user.User}",
        "reddit": f"https://reddit.com/{user.User}",
        "spotify": f"https://spotify.com/{user.User}",
        "gitlab": f"https://gitlab.com/{user.User}",
        "behance": f"https://behance.net/{user.User}",
        "whatsapp": f"https://wa.me/{user.User}",
        "telegram": f"https://t.me/{user.User}",
        "twitch": f"https://twitch.tv/{user.User}",
        "linkedin": f"https://linkedin.com/in/{user.User}"
    }
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with open(f"{user.User}.text", "w", encoding="utf-8") as f:
        for red,enlace in redes_sociales.items():
            try:
                respuesta = requests.get(enlace, headers=headers, allow_redirects=False, timeout=5)
                if respuesta.status_code == 200:
                    f.write(f"{red}: {redes_sociales[red]}\n")
                elif respuesta.status_code in [301, 302]:
                    redes_sociales[red] = "no encontrado redirige a login"
                    f.write(f"{red}: {redes_sociales[red]}\n")        
                else:
                    redes_sociales[red] = "no encontrado"
                    f.write(f"{red}: {redes_sociales[red]}\n")
            except requests.RequestException:
                redes_sociales[red] = "error de conexion o no encontrado"
                f.write(f"{red}: {redes_sociales[red]}\n")
                continue
    return "listo el texto ya ah sido descargado puede ver resultado :)"