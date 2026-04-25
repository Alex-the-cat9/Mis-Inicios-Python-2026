# --- 1. LA SINTAXIS BÁSICA ---
# .remove("nombre") busca por VALOR, no por posición.
# Si el nombre no existe, el programa EXPLOTA (ValueError).
lista = ["Alex", "Bot", "Gato"]
if "Bot" in lista:
    lista.remove("Bot") # ✅ Seguro

# --- 2. LA MAGIA NEGRA: "EL DOBLE ASESINATO" ---
# Descubrimiento de Alex: remove.remove(remove.pop(0))
# ¿Qué pasó aquí?
# 1. El .pop(0) SECUESTRA al primero de la fila.
# 2. El .remove() recibe el nombre del secuestrado y BUSCA a otro 
#    que se llame igual en la lista restante para ELIMINARLO también.
# Resultado: ¡Dos bajas en una sola línea de código! 💀💀

# --- 3. DIFERENCIAS CLAVE ---
# .pop(índice)   -> Usa el número de la silla (0, 1, 2...).
# .remove(valor) -> Usa el nombre de la persona ("Alex").

# --- 4. REGLA DE ORO DEL TECH LEAD ---
# Jamás uses .remove() sin un "if ... in ..." antes. 
# Un programa profesional nunca debe teñirse de rojo por un error de búsqueda.

# --- 5. EL CASO DEL NÚMERO "1" ---
# Alex: "hice almacen.remove(1) ¿está bien?"
# Respuesta: Solo si el CONTENIDO es el número 1. 
# Si quieres borrar la silla 1, usa .pop(1). No confundas el nombre con el asiento.

# ============================================================
