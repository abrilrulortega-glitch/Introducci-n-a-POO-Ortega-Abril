"""
EJERCICIO 7
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro.
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. La
clase CajaAhorro tendrá un método para heredar los datos y uno mostrar la información.
La clase PlazoFijo tendrá dos atributos tendrá dos atributos propios, plazo e interés. Tendrá un método 
para obtener el importe del interés(cantidad*interés/100) y otro método para mostrar la información, datos 
del titular plazo, interés y total de interés.
Crear al menos un objeto de cada subclase.
"""
class Cuenta:
    def __init__(self, titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
        
    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")
        
class CajaAhorro(Cuenta):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
        
    def mostrar(self):
        print("___Caja de Ahorro___")
        self.imprimir()
        
class PlazoFijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
        
    def calcular_interes(self):
        return self.cantidad*self.interes/100
    
    def mostrar(self):
        print("___Plazo Fijo___")
        self.imprimir()
        print(f"Plazo: {self.plazo}")
        print(f"Interés: {self.interes}")
        print(f"Importe de interés: {self.calcular_interes()}")
        
caja=CajaAhorro("Ana", 5000)
plazo=PlazoFijo("Luis",1000,50,3)

caja.mostrar()
print()
plazo.mostrar()