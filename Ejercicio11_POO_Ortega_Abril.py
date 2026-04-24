"""
EJERCICIO 11: BATALLA DE HECHICEROS
Dos hechiceros se enfrentan en un duelo mágico. Uno será controlado por el usuario, quien podrá tomar
decisiones estratégicas durante el combate.
Cada acción tiene consecuencias sobre los recursos disponibles del personaje, por lo que será necesario
administrarlos correctamente.
El enfrentamiento continúa hasta que uno de los participantes ya no pueda seguir luchando.
"""

import random                 #el enemigo elige acciones al azar
import os                     #sirve para limpiar la pantalla
import time                   #hace pausas, da tiempo a leer lo que pasó antes de que siga el turno

def limpiar():
    os.system('cls')          #comando para limpiar la pantalla en Windows
def barra(valor,maximo,largo=20):
    relleno=int((valor/maximo)*largo)
    return "█" * relleno + "-" * (largo - relleno)   #dibuja la parte llena o vacia

vida_jugador=100
mana_jugador=50
vida_enemigo=100

while vida_jugador>0 and vida_enemigo>0:             #mientras ambos este vivos...
    limpiar()
    print("╔══════════════════════════════╗")
    print("║   🧙 BATALLA DE HECHICEROS   ║")
    print("╚══════════════════════════════╝\n")

    print("TU ESTADO:")
    print(f"❤️ Vida:  [{barra(vida_jugador,100)}]  {vida_jugador}/100")   #dibujo la barra visual
    print(f"🔷 Maná:  [{barra(mana_jugador,50)}]   {mana_jugador}/50\n")

    print(f"ENEMIGO: ")
    print(f"💀Vida:  [{barra(vida_enemigo,100)}]  {vida_enemigo}/100\n")

    print("ACCIONES: ")
    print("1) ⚔️ Atacar (10 daño)")
    print("2) 🔥 Hechizo fuerte (25 daño, -10 maná)")
    print("3) 💚 Curarse (+20 vida, -10 maná)")

    opcion=input("\nElegí una acción: ")
    print("\n---- RESULTADO----")

    if opcion=="1":
        vida_enemigo-=10
        print("Atacaste al enemigo (-10 vida)")
    elif opcion=="2" and mana_jugador>=10:
        vida_enemigo-=25
        mana_jugador-=10
        print("Lanzaste un hechizo fuerte (-25 vida)")
    elif opcion=="3" and mana_jugador>=10:
        vida_jugador=min(100, vida_jugador+20)        #evita que la vida pase de 100
        mana_jugador-=10
        print("Te curaste (+20 vida)")

    else:
        print("Acción inválida o sin maná")
    
    time.sleep(1)                                     #espera 1 segundo antes del turno del enemigo

    #turno enemigo
    accion=random.choice(["ataque","fuerte"])         #elige una accion al azar

    if accion=="ataque":
        vida_jugador-=10
        print("El enemigo te atacó  (-10 vida)")

    else:
        vida_jugador-=20
        print("El enemigo lanzó un hechizo fuerte (-20 vida)")

    input("\nPresiona ENTER para continuar...")       #espero al usuario

#final, determino quien ganó
limpiar()
if vida_jugador>0:
    print("🏆 ¡GANASTE!")
else:
    print("💀 PERDISTE...")   
    