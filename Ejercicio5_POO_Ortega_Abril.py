"""
EJERCICIO 5
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y
el email. Además deberá mostrar un menú con las siguientes opciones
● Añadir contacto
● Lista de contactos
● Buscar contacto
● Editar contacto
● Cerrar agenda
"""
class Agenda:
    def __init__(self):
        self.contactos=[]

    def añadir_contactos(self):
        nombre=input("Nombre: ")
        telefono=input("Teléfono: ")
        email=input("Email: ")

        contactos={
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }

        self.contactos.append(contactos)
        print("Contacto añadido")

    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos")
            return
        for i, c in enumerate(self.contactos, 1):
            print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}")
            print()

    def buscar_contacto(self):
        nombre=input("Ingrese el nombre a buscar: ")
        encontrado=False

        for c in self.contactos:
            if c["nombre"].lower()==nombre.lower():
                print(f"{c['nombre']}-{c['telefono']}-{c['email']}")
                encontrado=True

        if not encontrado:
            print("Contacto no encontrado")
            print()

    def editar_contacto(self):
        nombre=input("Ingrese el nombre del contacto a editar: ")

        for c in self.contactos:
            if c["nombre"].lower()==nombre.lower():
                c["telefono"]=input("Nuevo teléfono: ")
                c["email"]=input("Nuevo email: ")
                print("Contacto editado")
                return
        print("Contacto no encontrado.\n")

    def menu(self):
        while True:
            print("----- AGENDA -----")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            op=int(input("Seleccione una opción: "))
            if op==1:
                self.añadir_contactos()
            elif op==2:
                self.lista_contactos()
            elif op==3:
                self.buscar_contacto()
            elif op==4:
                self.editar_contacto()
            elif op==5:
                print("Agenda cerrada")
                break
            else:
                print("Opción inválida.\n")

agenda=Agenda()
agenda.menu()