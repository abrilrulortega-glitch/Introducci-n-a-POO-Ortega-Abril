"""
EJERCICIO 9: EL TESORO ESCONDIDO
Un explorador se adentra en una cueva en busca de tesoros. En su camino encuentra cofres que pueden estar
cerrados o abiertos, y que contienen cierta cantidad de monedas.
El usuario deberá decidir qué hacer en cada momento: intentar abrir cofres, recolectar monedas o continuar
explorando.
El sistema debe permitir visualizar el estado del cofre y la cantidad de recursos acumulados por el jugador
hasta finalizar la exploración.
"""
import random    #elige al azar las monedas de cada cofre
def limpiar():
    print("\n"*30)   #limpia la pantalla

class Cofre:
    def __init__(self):
        self.abierto=False   #el cofre comienza cerrado
        self.monedas=random.randint(1,5) #puede tener entre 1 y 5 monedas aleatorias

    def abrir(self):
        if not self.abierto:   #si el cofre no esta abierto
            self.abierto=True  #lo abre
            print("Abriste el cofre")

        else:
            print("El cofre ya estaba abierto")

    def mostrar_estado(self):
        if self.abierto:
            dibujo=[
                "      _________      ",
                "     /         \\     ",
                "    /  💰 💰 💰  \\    ",
                "   /___________\\    ",
                "   |           |     ",
                "   |           |     ",
                "   |___________|     ",
                "     (ABIERTO)       "
            ]

        else:
            dibujo=[
                "      _________      ",
                "     /         \\     ",
                "    /           \\    ",
                "   /___________\\    ",
                "   |     🔒     |    ",
                "   |           |     ",
                "   |___________|     ",
                "     (CERRADO)       "
            ]

        for linea in dibujo:
            print(linea)  #imprime el cofre linea por linea

        if self.abierto:  #si esta abierto muestra monedas
            print(f"\nMonedas dentro: {self.monedas}")

        else:     #si esta cerrado, no muestra
            print(f"\nMonedas dentro: ???")
class Explorador:
    def __init__(self):
        self.monedas=0  #el usuario empieza con 0 monedas

    def recolectar(self,cofre):  #permite recolectar monedas del cofre
        if cofre.abierto and cofre.monedas>0:  #funciona si el cofre esta abierto y si todavia tiene monedas
            self.monedas+=cofre.monedas        #suma monedas al usuario
            print(f"Recolectaste {cofre.monedas} monedas")
            cofre.monedas=0   #vacia el cofre

        else:
            print("No podes recolectar monedas")    #si no cumple las condiciones, no permite recolectar

    def mostrar_estado(self):
        print(f"\n🪙Monedas acumuladas: {self.monedas}")

usuario=Explorador()

for turno in range(3):  #se exploran 3 cofres
    cofre=Cofre()  #cada vuelta genera un cofre nuevo

    while True:  #permite repetir acciones hasta salir del cofre
        limpiar()
        print(f"\n--- Cofre {turno+1} ---\n")  #muestra en que cofre estas

        cofre.mostrar_estado()
        usuario.mostrar_estado()

        print("\n1. Abrir cofre")
        print("2. Recolectar monedas")
        print("3. Seguir explrando")

        opcion=input("\nElegí una opción: ")

        if opcion=="1":
            cofre.abrir()
        elif opcion=="2":
            usuario.recolectar(cofre)
        elif opcion=="3":
            print("Seguis explorando...")
            break            #sale del bucle del cofre
        else:
            print("Opción inválida")

        input("\nPresione ENTER para continuar...")

print("\n--- Exploraxión finalizada ---")
usuario.mostrar_estado()  #muestra total de monedas ganadas