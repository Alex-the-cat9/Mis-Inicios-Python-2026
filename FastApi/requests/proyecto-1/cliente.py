from requests import get, post, options
url = "http://127.0.0.1:8000"
ver = get(f"{url}/ver-estado")
print(ver.json())
#Alex:wow asi se comunican los servidores bueno no lo se aun se puso un error descubrire porque fue el error
#estas comunicaciones parecen las mismas cuando importas otros archivos tambien aprendi sobre el puerto :80
#maestro.IA:Mira con atención la última línea:127.0.0.1:63148 - "GET /ver-estado HTTP/1.1" 200 OKSé lo que estás pensando:
#"Oye, ¿por qué dice 63148 si quedamos en que el puerto era el 8000?". Aquí viene un concepto avanzado de redes:El 8000 es el puerto
#del Servidor (FastAPI). Está fijo esperando visitas.El 63148 es el puerto del Cliente (requests).
viendo = options(f"{url}/ver-estado")
print(viendo.text)
#Alex: por cierto estaba viendo que errores puede sufrir mi servidor y vi varios ataques uno de ellos yo mismo lo descubri sin querer
#mi curiosidad dijo que pasaria si ago muchos bots que agan un error millones de veces asiendo que el servidor muera y se sature
#se llama ataque:taque de denegación de servicio distribuido (DDoS) basado en la explotación de una vulnerabilidad específica
#Application-layer DDoS asi dice googlel lo busque me senti especial porque pense que descubri un erorr que ya existe xd
registro = post(f"{url}/registro", json={"nombre":"Alex", "edad":15})
print(registro.text)
from random import choices, randint
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v" "w", "x", "y", "z"]
for i in range(1000):
    ataque = post(f"{url}/registro", json={"nombre":f"{"".join(choices(letras, k=10))}", "edad":f"{randint(1, 100)}"})
    print(ataque.text)
    #vaya parece que si rompi el servidor aunque siga funcionando el programa json de los usuarios esta completamente mal
    #este dia nos pusimos el sombre negro jsjs are otro proyet 2 creare un servidor nuevo con mas seguridad