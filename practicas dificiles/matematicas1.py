import numpy as np

# 1. Los datos originales (Vectores de Comida)
# Cada fila es una comida: [Grasa, Vitaminas]
comidas = np.array([   # Manzana,   # Pizza
    [1, 10]   # Brócoli
])

# 2. La Matriz de la IA (La máquina de transformación)
# Esta matriz fue "aprendida" por la IA para separar lo sano de lo no sano.
# Fila 1: Qué hacer con la grasa. Fila 2: Qué hacer con las vitaminas.
matriz_IA = np.array([
    [-0.5,  0.1],  # Penaliza la grasa, premia un poco la vitamina
    [ 0.2,  1.5]   # Premia mucho la vitamina
])

# 3. EL CABLE: Multiplicación de matrices (El espacio se transforma)
# En Python, '@' significa multiplicación de matrices en álgebra lineal
datos_transformados = comidas @ matriz_IA

print("Datos Originales:\n", comidas)
print("\nDatos Transformados por la IA:\n", datos_transformados)
