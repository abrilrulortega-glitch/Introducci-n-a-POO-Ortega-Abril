"""
EJERCICIO 10: GRAN CARRERA
Se está llevando a cabo una carrera entre varios autos. Uno de ellos será controlado por el usuario, quien podrá
decidir cómo actuar en cada turno.
Cada acción influirá en el desempeño del vehículo, afectando su avance en la pista. Mientras tanto, los demás
competidores avanzarán automáticamente. El programa debe permitir observar la evolución de la carrera y
determinar el resultado final.
"""
import random   #numeros aleatorios (simular avances distintos)

class Auto:
    def __init__(self,nombre):
        self.nombre=nombre
        self.posicion=0   #todos los autos inician en la posición 0

    def avanzar(self,tipo="normal"): #"tipo" indica como se mueve(acelerar,frenar,etc)
        if tipo=="acelerar":
            avance=random.randint(10,15)  #si acelera, avanza entre 10 y 15
        elif tipo=="frenar":
            avance=random.randint(1,5)  #si disminuye la velocidad, avanza entre 1 y 5
        else:
            avance=random.randint(5,10)  #movimiento normal

        self.posicion+=avance  #suma el avance a la posicion actual
        print(f"{self.nombre} avanza {avance} metros. Posición total:{self.posicion}") #muestra que paso en ese turno

    def mostrar_posicion(self):
        print(f"{self.nombre}: {self.posicion} metros")

class Carrera:  #representa toda la carrera
    def __init__(self,meta):
        self.meta=meta
        self.autos=[]  #lista donde guardo los autos

    def agregar_auto(self,auto): #cada vez que llamo esta función, estoy “inscribiendo” un auto en la carrera
        self.autos.append(auto)  #agrega un auto a la lista
    
    def mostrar_estado(self):
        print("\n--- ESTADO DE LA CARRERA ---")
        
        largo_pista=50  #tamaño visual de la pista
        for auto in self.autos: #recorre todos los autos
            progreso=int((auto.posicion/self.meta)*largo_pista) #convierte la posicion real en posicion visual
                                                          #(regla de 3, que tan cerca esta de la meta)
            if progreso>largo_pista: #evita que se pase del dibujo
                progreso=largo_pista

            pista = "-" * progreso + "🚗" + "-" * (largo_pista - progreso) #construyo pista
            
            print(f"{auto.nombre:10} |{pista}| {auto.posicion}m") #muestra:nombre alineado,pista y metros recorridos

    def turno_jugador(self,auto):
        print("\nTu turno:")
        print("1. Acelerar")
        print("2. Mantener velocidad")
        print("3. Frenar")

        opcion=input("Elegí una opción: ")

        if opcion=="1":
            auto.avanzar("acelerar")
        elif opcion=="3":
            auto.avanzar("frenar")
        else:
            auto.avanzar("normal")

    def turno_cpu(self):
        for auto in self.autos:
            if auto.nombre!="Jugador":                                #evito mover al jugador otra vez
                accion=random.choice(["acelerar","normal","frenar"])  #elige accion al azar
                auto.avanzar(accion)                                  #ejecuta movimiento
    def ganador(self):
        for auto in self.autos:
            if auto.posicion>=self.meta:                              #si paso o llego a la meta
                return auto                                           #devuelve el ganador
        return None                                                   #si nadie gano todavia
    
    def iniciar(self):
        print("¡Comienza la carrera!\n")

        while True:                                                  #loop infinito hasta que alguien gane
            self.mostrar_estado()

            #Turno del jugador:
            for auto in self.autos:
                if auto.nombre=="Jugador":
                    self.turno_jugador(auto)

            #turno cpu:
            self.turno_cpu()

            #verifica ganador:
            verificar_ganador=self.ganador()
            if verificar_ganador:
                self.mostrar_estado()          #muestra estado final
                print(f"\n¡{verificar_ganador.nombre} ganó la carrera!")
                print("GAME OVER")
                break                           #termina juego

#programa principal:
carrera=Carrera(100)
jugador=Auto("Jugador")        #crea los autos
cpu1=Auto("Auto 1")
cpu2=Auto("Auto 2")

carrera.agregar_auto(jugador)  #los agrega a la carrera
carrera.agregar_auto(cpu1)
carrera.agregar_auto(cpu2)

carrera.iniciar()              #arranca el juego