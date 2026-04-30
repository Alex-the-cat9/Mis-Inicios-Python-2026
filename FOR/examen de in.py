#🛡️ Tu Reto de hoy: "El Validador de Negocio"
#Vamos a simular que un cliente te pide un sistema para ver si un producto está en stock. Si lo logras, estarás un paso más cerca de tu primer "trabajo".
#Misión:
#Tienes este inventario (Diccionario): stock = {"laptop": 5, "mouse": 0, "teclado": 10}.
#Pídele al usuario un producto (input).
#Usa in para ver si el producto existe en el stock.
#Si existe Y el valor es mayor a 0, imprime: "✅ Producto disponible para venta".
#Si no, imprime: "❌ No disponible".
stock = {
    "laptop": 5,
    "mouse": 0,
    "teclado":10
}
for i in stock:
    print(i)
pedir = input("pide un producto sobre este stok: ")
if pedir in stock:
    if stock[pedir] > 0:
        print(f"el producto:{pedir} si esta en el stok")
    else:
      print(f"el producto:{pedir} no esta en el stock")
else:
    print(f"ese no es algo del stock")
