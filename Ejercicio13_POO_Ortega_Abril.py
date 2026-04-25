"""
EJERCICIO 13: DESAFÍO DE DADOS
En un juego de azar participan varios jugadores. Uno de ellos será controlado por el usuario. En cada ronda,
el usuario podrá lanzar un dado para obtener un valor que se acumulará en su puntaje total. Los demás
jugadores también participarán automáticamente.
Al finalizar varias rondas, se deberá determinar el resultado del juego.
"""
import random

class Dado:
    def lanzar(self):
        return random.randint(1,6)
    
class Jugador:
    def __init__(self,nombre,es_usuario=False):      #usuario indica si es cpu o no
        self.nombre=nombre
        self.puntaje=0                            #inicializa el puntaje en 0
        self.es_usuario=es_usuario                #guarda si es usuario o no

    def jugador_turno(self,dado):
        if self.es_usuario:                       #si es el jugador real...
            input(f"\n🎲 {self.nombre}, presiona ENTER para tirar el dado...")
        else:                                     
            print(f"\n👤{self.nombre} está tirando el dado...") 

        resultado=dado.lanzar()
        self.puntaje+=resultado
        print(f"🎲 {self.nombre} sacó: {resultado}")
        print(f"🌟Puntaje total: {self.puntaje}")

#programa principal:
dado=Dado()

nombre=input("Ingresa tu nombre: ")
jugador_usuario=Jugador(nombre,True)

jugadores=[
    jugador_usuario,
    Jugador("Contrincante 1"),
    Jugador("Contrincante 2")
]

while True:
    try:
        rondas=int(input("Cuántas rondas desea jugar?: "))
        if rondas>0:      #si el dato es valido, sale del bucle
            break
        else:
            print("Porfavor, ingrese un número mayor a 0")
    except ValueError:                                         #CONSULTAAAAAAAAAAAAAAAAAAAAAA
        print("Porfavor, ingrese un número válido")

for ronda in range(1,rondas+1):      #repite desde 1 hasta la cantidad de rondas
    print(f"\n---- RONDA {ronda} ----")
    for jugador in jugadores:
        jugador.jugador_turno(dado)

print("\nRESULTADOS FINALES:")
for jugador in jugadores:
    print(f"{jugador.nombre}: {jugador.puntaje} puntos")

max_puntaje=max(jugador.puntaje for jugador in jugadores)   #busca el puntaje mas alto
ganadores=[jugador for jugador in jugadores if jugador.puntaje==max_puntaje]  #creo una lista con los jugadores que tienen el puntaje mas alto
if len(ganadores)>1:
    print("\nHUBO UN EMPATE ENTRE: ")
    for jugador in ganadores:
        print(f"-{jugador.nombre} ({jugador.puntaje}) puntos")    #muestra los empatados

else:
    ganador=ganadores[0]                                          #si hay uno solo, ese es el ganador
    print(f"\n🏆GANADOR: {ganador.nombre} con {ganador.puntaje} puntos")

print("GAME OVER")