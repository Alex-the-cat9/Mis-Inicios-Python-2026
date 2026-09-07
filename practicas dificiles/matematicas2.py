import numpy as np
from sklearn.linear_model import LogisticRegression

# CORRECCIÓN: Dejamos solo 2 muestras y dejamos solo 2 respuestas
X_entrenamiento = np.array([[10, 2], [2, 8]]) # 2 muestras
y_respuestas = np.array([0, 1])               # 2 respuestas (Ajusta estos números a tus respuestas reales)

ia = LogisticRegression()
ia.fit(X_entrenamiento, y_respuestas)

print("¡Modelo entrenado con éxito!")
print(f"respuesta:{ia}")
# ESCRIBE ESTAS TRES LÍNEAS AL FINAL DE TU CÓDIGO:
print(f"Importancia del primer número: {ia.coef_[0][0]}")
print(f"Importancia del segundo número: {ia.coef_[0][1]}")
print(f"Número base (Sesgo): {ia.intercept_[0]}")