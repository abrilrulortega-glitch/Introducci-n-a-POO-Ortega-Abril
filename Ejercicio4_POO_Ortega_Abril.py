"""
EJERCICIO 4
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los
resultados obtenidos. Llamar a la clase Calculadora.
"""
class Calculadora:
    def __init__(self):
        self.valor1=int(input("Ingrese el 1er valor: "))
        self.valor2=int(input("Ingrese el 2do valor: "))

    def suma(self):
        print(f"Suma:", {self.valor1+self.valor2})
    def resta(self):
        print(f"Resta:", {self.valor1-self.valor2})
    def multiplicacion(self):
        print(f"Multiplicacion:", {self.valor1*self.valor2})
    def division(self):
        if self.valor2 != 0:
            print("División:", {self.valor1/self.valor2})
        else:
            print("No se puede dividir por cero")

calcu=Calculadora()
calcu.suma()
calcu.resta()
calcu.multiplicacion()
calcu.division()