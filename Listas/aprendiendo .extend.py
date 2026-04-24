#segun mi maestro(ia) dijo que el .extend() añade la copia de otra lista a lo que entendi 
#voy a probar aver que historia puedo contar mmm...
print("eres alex vas caminando tranquilamente tienes cosas de tu mochila")
mochila_de_Alex = ["piedra", "pluma", "cuerdas"]
print("tus cosas:")
for objetos in mochila_de_Alex:
    print(objetos)
print("despues de revisar tu mochila vas caminando tranquilamente asta que te encuentras con un cofre de oro")
cofre_de_oro = ["anillo de oro", "diamante", "plata"]
print("entonces alex decides quedarte con el cofre")
mochila_de_Alex.extend(cofre_de_oro)
print(mochila_de_Alex)
