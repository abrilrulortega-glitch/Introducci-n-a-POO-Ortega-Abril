"""
EJERCICIO 2
Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como
atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los
atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        
    def resultado(self):
        if self.edad<=17:
            print(self.nombre, "es menor de edad")
        else:
            print(self.nombre, "es mayor de edad")
            
Persona1=Persona("Sandra", 40)
Persona1.mostrar()
Persona1.resultado()
