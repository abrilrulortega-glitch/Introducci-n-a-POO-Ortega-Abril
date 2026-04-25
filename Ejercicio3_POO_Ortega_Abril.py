"""
EJERCICIO 3
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para
inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es
(equilátero, isósceles o escaleno).
"""

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def mayor(self):
        lado_mayor=max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es", {lado_mayor})

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triángulo equilatero")
        elif self.lado1==self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triángulo isóseles")
        else:
            print("Es un triángulo escaleno")

    def mostrar_lados(self):
        print(f"Lado 1:", {self.lado1})
        print(f"Lado 2:", {self.lado2})
        print(f"Lado 3:", {self.lado3})

triangulo1=Triangulo(5,5,3)
triangulo1.mostrar_lados()
triangulo1.mayor()
triangulo1.tipo_triangulo()

        