class Libro:
    def __init__(self, titulo, dato, cantidad):
        self.titulo = titulo
        self.dato = dato
        self.cantidad = cantidad
    def mostrar_info(self):
        print(f"el titulo es:{self.titulo}")
        print(f"el dato es :{self.dato}")
        print(f"la cantidad es:{self.cantidad}")
class biBlioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def mostrar_catalogo(self):
        for libro in self.libros:
            libro.mostrar_info()
    def presentar_libro(self, titulo):
        for libros in self.libros:
            if libros.titulo == titulo:
                if libros.cantidad >0:
                    libros.cantidad -=1
                    print("libro prestrado")
                else:
                    print("no ay stok disponible")
                return
        print("libro no encontrado")
    def devolver_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.cantidad >0:
                    libro.cantidad +=1
                    print("libro devuelto")
                    return
        print("no ay libros en el stok")
        
        