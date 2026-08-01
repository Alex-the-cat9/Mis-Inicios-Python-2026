#Tus Objetivos EstratégicosObjetivo 1:
#Construir el Firewall Web (Pydantic): Rellenar la clase AccountCreateRequest. Debes declarar las variables owner
#(tipo str) e initial_deposit (tipo int). Pydantic rechazará automáticamente si un atacante envía letras en el depósito
#o un formato JSON corrupto.Objetivo 2: Implementar la Compuerta Asíncrona: Completar el cuerpo de la función async def
#create_bank_account.Objetivo 3: Aplicar Contención Contracíclica (try-except):Dentro del try, instancia tu clase SecureAccount
#pasándole los datos que vienen del modelo (request_data.owner y request_data.initial_deposit).Dentro del except ValueError, intercepta el error
#de depósito insuficiente y levanta fulminantemente un raise HTTPException(status_code=400, detail="INVALID_DEPOSIT") para cortar la conexión del
#atacante web.Si pasa el filtro, ejecuta el retorno con código 201.
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Final
from secrets import token_hex
import json
code: Final[str] = token_hex(15)
app = FastAPI(title="Core_Bancario_Web",docs_url=f"/{code}",redoc_url=f"/{code}")
# 1. CLASE DE DOMINIO BLINDADA (Sujeta a encapsulamiento estricto)
class SecureAccount:
    def __init__(self, owner: str, initial_deposit: int) -> None:
        if initial_deposit < 100:
            raise ValueError("INVALID")
        self.__owner: Final[str] = owner
        self.__balance: Final[int] = initial_deposit
    def get_owner(self) -> str: 
        return self.__owner
    def get_balance(self) -> int: 
        return self.__balance
# ==============================================================================
# 2. MODELO DE CONTROL DE ENTRADA (Tu Objetivo 1)
class AccountCreateRequest(BaseModel):
    # Rellena aquí las dos variables necesarias con tipado estricto de Pydantic
    owner: str
    initial_deposit: int
# 3. ENDPOINT ASÍNCRONO DE ALTA CONCURRENCIA (Tu Objetivo 2 y 3)
@app.post("/v1/accounts/create", status_code=status.HTTP_201_CREATED)
async def create_bank_account(request_data: AccountCreateRequest) -> dict:
    """
    Endpoint asíncrono corporativo. 
    Intercepta payloads maliciosos web y valida contra reglas de negocio POO.
    """
    try:
        # IMPLEMENTA AQUÍ EL FLUJO DE VALIDACIÓN INTERNA:
        # 1. Instanciar SecureAccount usando los atributos de request_data
        View = SecureAccount(request_data.owner, request_data.initial_deposit)
        owner = View.get_owner()
        initial = View.get_balance()
        Json = {"status":"created", "owner":owner, "request_data":initial}
        # 2. Si es exitoso, retornar el JSON: {"status": "created", "owner": ...}

        return Json
    except ValueError as error:
        print(f"ERROR:{str(error)}")
        raise HTTPException(
            status_code=400,
            detail="INVALID DEPOSIT"
        )