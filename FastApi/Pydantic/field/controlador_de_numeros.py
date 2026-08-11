from pydantic import BaseModel
class Usuario(BaseModel):
    id:int
    nombre:str
    email:str
Usuario_valido = Usuario(id=100, nombre="ALEX", email="ALEX@gmail.com")
print(Usuario_valido.nombre)
from pydantic import BaseModel, Field
class ProductoFinanciero(BaseModel):
    # El precio debe ser mayor
    #precio: int = Field(gt=0)
    # El descuento es un porcentaje: debe ir estrictamente de 0 a 100
    descuento_porcentaje: float = Field(ge=0.0, le=100.0)
    # El stock debe ser un número entero positivo o cero
    #stock: int = Field(ge=0)
    # Restricción estricta de temperatura para envío (menor a 4 grados, sin incluir el 4)
    #temperatura_envio: float = Field(lt=4.0)
precio = ProductoFinanciero(descuento_porcentaje=100)
#ya entendi son < > <= >= son asi iguales
print(precio.descuento_porcentaje)