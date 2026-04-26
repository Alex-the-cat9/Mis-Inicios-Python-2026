# Alex-the-cat9 | Examen de Certificación .sort()

# --- CASO 1: LA FILA DEL BANCO ---
# Tienes estos clientes. Ordénalos por el ABECEDARIO REAL 
# (Que a "alex" no le ganen solo por ser minúscula).
clientes = ["Zulema", "alex", "Belmont", "tiago"]
# [TU CÓDIGO AQUÍ]
clientes.sort(key=str.lower)
#solo memorize no se nada de lower solo vi qure decia que este codigo ase que las mayusculas y minusculas se comporten igual

# --- CASO 2: EL ALMACÉN DE AMAZON ---
# Tienes paquetes con pesos que son TEXTO. 
# Ordénalos de MENOR A MAYOR peso numérico (no por dibujo).
paquetes = ["10.5", "2.1", "50.0", "4.2"]
# [TU CÓDIGO AQUÍ]
paquetes.sort(key=float)#si la entendi ordenar numeros enteros con key regla

# --- CASO 3: EL CÓDIGO REVERSO ---
# Tienes esta lista: [1, 2, 3, 4, 5]
# Únicamente usando .sort(), haz que se convierta en [5, 4, 3, 2, 1]
numeros = [1, 2, 3, 4, 5]
# [TU CÓDIGO AQUÍ]
numeros.sort(reverse=True)
#ACTIVAR REVERSA
# --- RESULTADOS ---
print(f"Clientes: {clientes}")
print(f"Paquetes: {paquetes}")
print(f"Números: {numeros}")
