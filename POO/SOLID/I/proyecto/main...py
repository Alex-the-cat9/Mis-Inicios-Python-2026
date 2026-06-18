#Los Planos Moleculares (Interfaces):
#Crea una clase abstracta base RobotBase(abc.ABC) que solo tenga el __init__ para el nombre
#Crea tres "Planos Pequeños" independientes:
#Volador(abc.ABC) con el método abstracto volar(self) -> str.
#Caminante(abc.ABC) con el método abstracto caminar(self) -> str.
#Reparador(abc.ABC) con el método abstracto reparar(self) -> str.
#Las Unidades Especializadas (Tus Clases Hijas):
#El Sabotaje de Contrainteligencia (Tu Misión de Prueba):
#Instancia un DroneExplorador.
#La Trampa: Intenta obligar al Drone a ejecutar el método caminar().
#Como aplicaste la I, el Drone no tiene ese cable en su ADN
#Tu código no debería tener métodos con pass para simular funciones que no usa; simplemente no debe conocerlas
#📡 TU BITÁCORA DE INSPECCIÓN
#Pica el código usando Type Hinting (: str, -> str) para que el radar de mypy esté activo
import DroneExplorador
Dron = DroneExplorador.DroneExplorador("Robot.Alex")
#Dron.caminar()
#si marca error