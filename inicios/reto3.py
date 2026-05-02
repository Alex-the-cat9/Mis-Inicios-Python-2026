fila = ["zapatos", "libros", "comida", "juguetes"]

# 2. El comando mágico para "colarse" al principio
# Estructura: lista.insert(posición, objeto)
fila.insert(0, "Paquete Presidencial")

# 3. El cartero saca al que está en el primer lugar (el 0)
# Estructura: variable = lista.pop(posición)
enviado = fila.pop(0)

print(f"Despachando ahora mismo: {enviado}")
print(f"Paquetes que siguen esperando: {fila}")
