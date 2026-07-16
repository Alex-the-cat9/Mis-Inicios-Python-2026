from fastapi import FastAPI 
app = FastAPI()
@app.post("/manda_hola")
def mandar():
    return "hola"