def validacion(entrega):
    lista = {}
    def vereficar(**kwargs):
        for e,i in kwargs.items():
            for o,a in i.items():
                if a < 18:
                    print(f"{o} no pasas")
                else:
                    print(f"{o} si pasas")
                    lista[o] = a
        entrega()
        print("ESTA LISTO")
        for nombre,edad in lista.items():
            print(f"{nombre} pasas porque tienes {edad} años eres mayor de edad")
    return vereficar
@validacion
def saludar():
    print("todos estan vereficado?")
saludar(integrantes={"Alex":14, "Olivia":15, "Saul":10, "IA":1000, "Anciano":99})
