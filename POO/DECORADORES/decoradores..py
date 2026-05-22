#🩻 Las Especificaciones del Desafío: El Centinela de LogsTu misión es programar un decorador llamado @centinela [INDEX_3]
#Su objetivo es vigilar desde arriba a cualquier función esclavo y registrar en la pantalla cuándo inicia y cuándo termina
#⚠️ Las 3 Reglas del Rompecabezas:La Caja Externa (El Decorador): Debe llamarse def centinela(funcion_entrada):
#La Caja Interna (La Envoltura): Debe llamarse def envoltura(): [INDEX_3]. Dentro de ella, debes hacer exactamente
#esto en orden vertical [INDEX_3]:Hacer un print("🛰️ [CENTINELA] Interceptando llamada...") [INDEX_3].Disparar la función original
#usando el interruptor de los paréntesis () [INDEX_3].Hacer un print("✅ [CENTINELA] Ciclo terminado con éxito.") [INDEX_3].El Cierre 
#de Circuito: Al final de la caja externa, debes usar el return correcto para entregarle la envoltura a la etiqueta de abajo, evitando
#el temido TypeError que cazaste en tu cuaderno [INDEX_3].
def centinela(funcion_entrada):
    def envoltura():
        print("centinela:interceptando llamanda:..... ")
        funcion_entrada()
        print("centinela ciclo terminando con exito")
    return envoltura
@centinela
def primera_victima():
    print("Entrando vereficando si ay exito.....")
primera_victima()
#Alex:muy facil te pedi algo mas dificil estamos repitiendo luego are decoradores mas avansados