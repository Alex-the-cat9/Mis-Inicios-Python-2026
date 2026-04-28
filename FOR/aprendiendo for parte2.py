#Crea la lista mochila con: "piedra", "diamante", "madera", "anillo de oro", "barro".
#Usa el bucle for limpio (sin len, sin range).
#Dentro del bucle, usa la lógica de Alex:
#Si el objeto es "diamante" o es "anillo de oro", imprime: Alex vendió su {objeto} por 100 monedas.
#Si no, imprime: Alex guardó su {objeto}, no vale nada
mochila = ["piedra", "diamante", "madera", "anillo de oro", "barro"]
for Alex in mochila:
    if Alex in mochila == "diamante" or "anillo de oro":
        print(f"Alex vendio su {Alex} por 100$ monedas")
    else:
        print(f"Alex guardo su {Alex} no vale nada")
