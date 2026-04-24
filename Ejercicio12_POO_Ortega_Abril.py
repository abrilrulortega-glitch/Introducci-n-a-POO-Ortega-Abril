"""
EJERCICIO 12: AVENTURA Y OBJETOS
Un aventurero recorre distintos escenarios recolectando objetos que encuentra en su camino. El usuario podrá
decidir qué hacer con cada objeto: guardarlo, utilizarlo o descartarlo. Además, deberá poder consultar en todo
momento qué elementos posee.
El programa debe permitir gestionar esta información de forma dinámica durante la ejecución.
"""
import random

class Objeto:
    def __init__(self, nombre, emoji):
        self.nombre=nombre
        self.emoji=emoji

    def mostrar(self):
        return f"{self.emoji} {self.nombre}"
class Aventurero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.inventario=[]

    def guardar_objeto(self,objeto):
        self.inventario.append(objeto)
        print(f"Guardaste: {objeto.mostrar()}")

    def usar_objeto(self,nombre_objeto):
        for obj in self.inventario:                        #recorre todos los objetos de inventario
            if obj.nombre.lower()==nombre_objeto.lower():  #compara nombres ignorando las mayusculas
                print(f"Usaste: {obj.mostrar()}")          #muestra lo que usaste 
                self.inventario.remove(obj)                #y lo borra del inventario
        print("No tenes ese objeto...")

    def descartar_objeto(self,descartar_objeto):
        for obj in self.inventario:
            if obj.nombre.lower()==nombre_objeto.lower():
                self.inventario.remove(obj)
                print(f"Descartaste: {obj.mostrar()}")
                return
        print("No tenes ese objeto...")

    def mostrar_inventario(self):
        if not self.inventario:                             #si la lista esta vacia...
            print("Inventario vacío")
        else:                                               #si no es asi..
            print("Inventario: ")
            for obj in self.inventario:
                print("-", obj.mostrar())

objetos=[
    ("Espada", "⚔️"),
    ("Poción", "🧪"),
    ("Escudo", "🛡️"),
    ("Oro", "💰"),
    ("Llave", "🗝️"),
    ("Arco", "🏹"),
    ("Mapa", "🗺️")
]

#programa principal
nombre=input("Nombre del aventurero: ")
jugador=Aventurero(nombre)

print(f"\n¡Bienvenido, {jugador.nombre}!\n")

while True:                                     #el juego se repite infinitamente hasta salir
    print("---- EXPLORANDO ----")
    nombre_obj, emoji=random.choice(objetos)    #elige un objeto al azar
    objeto=Objeto(nombre_obj, emoji)            
    print(f"Encontraste: {objeto.mostrar()}")

    print("\nQue quieres hacer?")
    print("1. Guardar")
    print("2. Usar un objeto del inventario")
    print("3. Descartar un objeto del inventario")
    print("4. Ver inventario")
    print("5. Salir")

    opcion=input("👉Elegí una opción: ")
    if opcion=="1":
        jugador.guardar_objeto(objeto)
    elif opcion=="2":
        objeto_usar=input("Que objeto quieres usar?: ")
        jugador.usar_objeto(objeto_usar)
    elif opcion=="3":
        objeto_descartar=input("Que objeto quieres descartar?: ")
        jugador.descartar_objeto(objeto_descartar)
    elif opcion=="4":
        jugador.mostrar_inventario()
    elif opcion=="5":
        print("\nGAME OVER")
        break
    else:
        print("Opción inválida")
