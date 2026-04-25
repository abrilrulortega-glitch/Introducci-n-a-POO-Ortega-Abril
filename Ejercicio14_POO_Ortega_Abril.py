"""
EJERCICIO 14: ÚLTIMA DEFENSA
Una torre protege un territorio de ataques constantes. El usuario podrá decidir cómo actuar frente a cada
situación. A medida que transcurre el tiempo, la torre recibe daños que afectan su estado. El sistema debe
permitir observar su condición en cada momento.
El juego finaliza cuando la torre ya no puede resistir más ataques.
"""
import random

def barra(vida,maximo=100,largo=20):
    relleno=int((vida/maximo)*largo)
    return "█" *relleno+"-"*(largo-relleno)  #CONSULTAAAAAAAAAAAAAA

class Enemigo:
    def __init__(self,nombre,emoji,danio_min,danio_max):
        self.nombre=nombre
        self.emoji=emoji
        self.danio_min=danio_min
        self.danio_max=danio_max

    def atacar(self):
        return random.randint(self.danio_min, self.danio_max)
    
    def mostrar(self):
        return f"{self.emoji} {self.nombre}"
    
class Torre:
    def __init__(self):
        self.vida=100

    def recibir_danio(self,cantidad):
        self.vida-=cantidad
        if self.vida<0:                          #evito que la vida sea negativa
            self.vida=0

    def reparar(self):
        reparacion=random.randint(5,15)          #curacion aleatoria
        self.vida+=reparacion                    #suma vida
        if self.vida>100:                        #no deja pasar del maximo
            self.vida=100
        print(f"Reparaste la torre (+{reparacion} vida)")

    def mostrar_estado(self):
        print(f"\n❤️ Vida: [{barra(self.vida)}] {self.vida}/100")  #barra visual de vida + numero real de vida

enemigos=[                                                        #creo diferentes enemigos con distintos daños
    Enemigo("Goblin", "👺", 5, 12),
    Enemigo("Orco", "👹", 10, 20),
    Enemigo("Dragón", "🐉", 15, 30),
    Enemigo("Esqueleto", "💀", 8, 15),
    Enemigo("Bruja Malvada","🧙",20,40)
]


#progama principal
torre=Torre()
turno=1                                                           #contador de turnos

print("¡LA TORRE ESTA SIENDO ATACADA!")
while torre.vida>0:
    print(f"\n---- TURNO {turno} ----")

    enemigo=random.choice(enemigos)
    ataque=enemigo.atacar()                                      #caluculo cuanto daño es el que hace

    print(f"Aparece: {enemigo.mostrar()}")
    print(f"Ataca con {ataque} de daño")

    print("\n¿Qué querés hacer?")
    print("1. Defender")
    print("2. Reparar")
    print("3. No hacer nada")

    opcion=input("Elegí una opción: ")
    if opcion=="1":
        reduccion=random.randint(5,15)
        ataque-=reduccion               #resta el daño
        if ataque<0:                    #no permite daño negativo
            ataque=0
        print(f"Redujiste el daño en {reduccion}")

    elif opcion=="2":
        torre.reparar()
    
    elif opcion=="3":
        print("No hiciste nada")

    else:
        print("Opción inválida, no hiciste nada")

    torre.recibir_danio(ataque)                    #aplica el daño final
    torre.mostrar_estado()                         #muestra el estado actual
    turno+=1                                       #suma uno al turno

print("\n💀LA TORRE HA SIDO DESTRUIDA💀")
print("GAME OVER")