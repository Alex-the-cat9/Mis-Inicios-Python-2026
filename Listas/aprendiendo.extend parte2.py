print("mochila de Alex deve conbinarse con la de pedrito")
mochila_de_alex = ["piedra", "basura", "plata"]
mochila_de_pedrito = ["papel", "gato", "oro"]
print("mochila de ALex:")
for mochila in mochila_de_alex:
    print(mochila)
print("mochila de pedrito:")
for mochila2 in mochila_de_pedrito:
    print(mochila2)
print("combinando...")
mochila_de_alex.extend(mochila_de_pedrito)
print("mochila combinada")
for combinado in mochila_de_alex:
    print(combinado)
#mi viaje duro mucho y por lo tanto el 11 de abril no pude subir un archivo sorry..:(
