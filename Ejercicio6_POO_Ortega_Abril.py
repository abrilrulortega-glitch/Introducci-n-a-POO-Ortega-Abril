"""
EJERCICIO 6
En un banco tienen clientes que pueden hacer depósitos y extracciones de diero. El banco
requiere tambien al final del día calcular la cantidad de dinero que se ha depositado. 
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre
y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
"""
class cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=0
        
    def depositar(self,monto):
        self.cantidad+=monto
        
    def extraer(self,monto):
        if monto<=self.cantidad:
            self.cantidad-=monto
        else:
            print(f"{self.nombre} no tiene suficiente dinero para extraer")
            
    def mostrar_total(self):
        print(f"{self.nombre} tiene {self.cantidad} pesos")
        
class Banco:
    def __init__(self):
        self.cliente1=cliente("Ismael")
        self.cliente2=cliente("Luis")
        self.cliente3=cliente("Sandra")
        
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(450)
        
        self.cliente1.extraer(500)
        self.cliente2.extraer(1000)

        
    def deposito_total(self):
        total=(self.cliente1.cantidad+
               self.cliente2.cantidad+
               self.cliente3.cantidad)
        print(f"El total depositado en el banco es: {total} pesos")
        
    def mostrar_clientes(self):
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        
banco=Banco()
banco.operar()
banco.mostrar_clientes()
banco.deposito_total()
        