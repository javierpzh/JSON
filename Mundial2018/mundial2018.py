from funciones_mundial2018 import *

with open("mundial2018.json") as fichero:
    datos=json.load(fichero)

while True:
    menu=('''OPCIONES:
    1- LISTAR INFORMACIÓN: Listar de todos los partidos, las selecciones que han jugado como locales este mundial.
    2- CONTAR INFORMACIÓN: Mostrar el número de partidos que se han disputado en este mundial.
    3- BUSCAR O FILTRAR INFORMACIÓN: Mostrar todos los partidos de la selección dada, es decir, todos los rivales a los que se ha enfrentado.
    4- BUSCAR INFORMACIÓN RELACIONADA: Mostrar los partidos que han terminado con un resultado dado.
    5- ÚLTIMO PARTIDO: Mostrar el último partido que jugó en esta competición una selección dada. Tiene que mostrar la fecha y la hora en que se disputó, la selección rival y el resultado final del encuentro.
    6- SALIR
    ''')

    print(menu)
    opcion=int(input("¿Qué acción desea realizar?: "))
    while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6:
        opcion=int(input("Error. Introduzca una opción del 1 al 6: "))

    #EJERCICIO 1
    if opcion==1:
        print("LOCALES")
        print()
        for seleccion in listar_informacion(datos):
            print(seleccion)

    #EJERCICIO 2
    if opcion==2:
        print(contar_informacion(datos))

    #EJERCICIO 3
    if opcion==3:
        cadena=str(input("Selección: "))
        for partido in buscar_informacion(datos,cadena):
            print(partido)

    #EJERCICIO 4
    if opcion==4:
        cadena=int(input("Goles locales: "))
        cadena2=int(input("Goles visitantes: "))
        for goles in buscar_informacion_relacionada(datos,cadena,cadena2):
            print(goles)

    #EJERCICIO 5
    if opcion==5:
        cadena=str(input("Selección: "))
        for partido in ejercicio_libre(datos,cadena):
            print(partido)

    #Salir
    if opcion==6:
        print("FIN DEL PROGRAMA")
        break