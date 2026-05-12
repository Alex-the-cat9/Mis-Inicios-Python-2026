class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("hola estoy hablando")
class empleado(persona):
    def __init__(self,nombre,edad,nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
roberto = empleado("ROBERTO", 23, "Nose", "programador", 20000)
print(roberto.nacionalidad)
#Alex:porque funciona este codigo
#maestro.IA:La magia ocurre en esta línea:super().__init__(nombre, edad, nacionalidad)Cuando llamas a super(),
#Python abre un túnel hacia la clase Padre (persona). Es como decirle: 
#"Oye, papá Persona, haz tu trabajo y guarda el nombre, la edad y la nacionalidad en este nuevo empleado, que yo me encargo de lo demás".
#Alex:describeme linea por linea todo conectado porque funciona
#class persona: # 1. Creas el "Molde Maestro" (La Clase Padre).
#    def __init__(self, nombre, edad, nacionalidad): # 2. El constructor que define qué es ser una "persona".
#        self.nombre = nombre # 3. Guardas el nombre en la memoria del objeto.
#        self.edad = edad # 4. Guardas la edad.
#        self.nacionalidad = nacionalidad # 5. Guardas la nacionalidad.
#        
#    def hablar(self): # 6. Creas un "poder" o método que tienen TODAS las personas.
#        print("hola estoy hablando")
#
#class empleado(persona): # 7. ¡HERENCIA! Aquí conectas los cables. Dices: "empleado" es un hijo de "persona".
 #   def __init__(self, nombre, edad, nacionalidad, trabajo, salario): # 8. El constructor del hijo. Pide los datos del padre MÁS los suyos.
 #       super().__init__(nombre, edad, nacionalidad) # 9. EL PUENTE: 'super()' viaja a la clase 'persona' y ejecuta su __init__.
 #       # Esto rellena automáticamente self.nombre, self.edad y self.nacionalidad usando el código de arriba.
 #       
 #       self.trabajo = trabajo # 10. El hijo añade su propia característica única.
 ##       self.salario = salario # 11. El hijo añade otra característica única.
#
 #   pass # 12. Un relleno que no hace nada aquí (porque ya escribiste código arriba).

# 13. INSTANCIACIÓN: Creas a Roberto. 
# Le pasas 5 datos, pero la clase 'empleado' reparte: 3 para el padre y 2 para él mismo.
#roberto = empleado("ROBERTO", 23, "Nose", "programador", 20000)

#rint(roberto.trabajo) # 14. ¡FUNCIONA! Porque 'roberto' es un objeto que tiene guardado 'programador' en su memoria.
