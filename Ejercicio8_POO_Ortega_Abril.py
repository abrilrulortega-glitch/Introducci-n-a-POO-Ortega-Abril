"""
EJERCICIO 8:DUELO EN LA ARENA
En una arena de combate se enfrentan dos personajes: uno controlado por el usuario y otro controlado por el
sistema.
Cada personaje posee ciertas características que determinan su capacidad de resistir ataques y de causar daño.
Durante el combate, el usuario puede decidir qué acción realizar en su turno, mientras que el oponente
responde automáticamente.
A medida que transcurre el enfrentamiento, se debe poder observar el estado de cada participante. El combate
finaliza cuando uno de los personajes ya no puede continuar.
"""
import random                      #Libreria random para que el enemigo elija acciones al azar(atacar o defender)
class Personaje:                   #Defino clase
    def __init__(self,nombre):
        self.nombre=nombre
        self.vida=5
        self.defensa=False       #Indica si está defendiendo(true,false)
        
    def esta_vivo(self):           #devuelve true si el personaje sigue vivo
        return self.vida>0       #devuelve false si su vida es 0
    
    def atacar(self,enemigo):
       if enemigo.defensa:
           print(f"{enemigo.nombre} se defendió y no recibe daño")
           enemigo.defensa=False                                   #se desactiva la defensa
       else:
            enemigo.vida-=1                                        #si no se defiende, pierde 1 vida
            print(f"{self.nombre} ataca a {enemigo.nombre} y le quita 1 vida")

       if enemigo.vida<0:
           enemigo.vida=0              #evito que la vida sea negativa
        
    def defender(self):
        self.defensa=True      #activa la defensa
        print(f"{self.nombre} se está defendiendo")

    def mostrar_estado(self):
        corazones="❤️" * self.vida             #representacion visual de vida
        print(f"{self.nombre}: {corazones} ({self.vida})")  #muestra nombre + corazones + numero vidas

#creo personajes
usuario=Personaje("Héroe")
enemigo=Personaje("Villano")

print("--- Estado Inicial ---") #muestro estado inicial de los personajes
usuario.mostrar_estado()
enemigo.mostrar_estado()

#combate
while usuario.esta_vivo() and enemigo.esta_vivo(): #el combate sigue mientras ambos esten vivos
    print("\nTu turno:")
    print("1. Atacar")
    print("2. Defender")
    opcion=input("Elegí una opción: ")
     
    if opcion=="1":
        usuario.atacar(enemigo)
    elif opcion=="2":
        usuario.defender()
    else:
        print("Opción inválida")

    if enemigo.esta_vivo():    #solo actua si sigue vivo
        print("\nTurno del enemigo:")
        accion=random.choice(["atacar", "defender"])  #elige accion al azar

        if accion=="atacar":
            enemigo.atacar(usuario)
        else:
            enemigo.defender()

    print("--- Estado Actual ---") 
    usuario.mostrar_estado()
    enemigo.mostrar_estado()

print("\n--- Fin del Combate ---")
if usuario.esta_vivo():
    print("¡Ganaste!")
else:
    print("Perdiste :(")