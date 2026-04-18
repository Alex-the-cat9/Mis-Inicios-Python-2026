numeros = [1, 2, 3 , 4 , 5, 6 , 7, 8, 9, 10]
nombres = ["juan", "Alex", "alejandro", "luis", "Mayordomo"]
nombres.sort(key=len)
print(nombres)
# --- 1. EL CONCEPTO CLAVE ---
# .sort() es el "Organizador Automático". 
# ¡OJO!: Cambia la lista original para siempre (In-place).

# --- 2. LA LÓGICA OCULTA (ASCII) ---
# Las computadoras ven números: 'A'=65, 'a'=97.
# Por defecto, las MAYÚSCULAS mandan y van primero.
# "Zebra" siempre aparecerá antes que "alex".

# --- 3. EL PARÁMETRO KEY= (Las Gafas Especiales) ---
# El 'key' es la REGLA que le impones a Python para ordenar:

# A) key=str.lower -> El Abecedario Real
# Ignora el poder de las mayúsculas. Junta a la 'A' con la 'a'.
# nombres.sort(key=str.lower)

# B) key=len -> El Organizador por Tamaño
# Ordena del nombre más corto al más largo.
# nombres.sort(key=len)

# C) key=int o key=float -> El Traductor Numérico
# Si tus números son texto (["10", "2"]), esto hace que el 2 vaya primero.
# lista_precios.sort(key=int)

# --- 4. LA KATANA DE REVERSA (reverse=True) ---
# No es un key, es un interruptor.
# Pone todo al revés: de mayor a menor o de la Z a la A.
# lista.sort(reverse=True)