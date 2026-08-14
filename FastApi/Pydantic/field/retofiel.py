from pydantic import Field, BaseModel, ValidationError
from random import  SystemRandom
from typing import Final
seguridad = SystemRandom()
class cupon(BaseModel):
    Cupon:int = Field(gt=0, le=100)
class systema_de_cupon:
    def __init__(self):
        self._lista: Final[list[int]] = [10, 25, 50, 80, 100]
    def crear_cupon(self):
        descuento = seguridad.choices(self._lista, weights=[60, 20, 10, 8, 2], k=1)[0]
        definitivo = cupon(Cupon=descuento)
        return definitivo
if __name__ == "__main__":
    try:
        system = systema_de_cupon()
        user1 = system.crear_cupon()
        print(f"SU CUPON ES:{user1.Cupon}")
    except ValidationError:
        print("Una disculpa el sistema fallo")

