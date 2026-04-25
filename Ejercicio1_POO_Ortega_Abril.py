"""
EJERCICIO 1:
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota
del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el
resultado de la nota y si ha aprobado o no.
"""
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota1=nota
        
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Nota: ", self.nota1)
        
    def evalua(self):
        if self.nota1 >= 7:
            print(self.nombre, "aprobó")
        else:
            print(self.nombre, "no abrobó")
        
Alumno1=Alumno("Abril", 8)
Alumno1.mostrar()
Alumno1.evalua()

