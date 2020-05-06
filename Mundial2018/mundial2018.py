import time
import json
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
        print("Has seleccionado la opción 1:")
        print("LISTAR INFORMACIÓN: Listar de todos los partidos, las selecciones que han jugado como locales este mundial.")
        time.sleep(1)
        print()
        print("LOCALES")
        print()
        for elem in listar_informacion(datos):
            print(elem)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 2
    if opcion==2:
        print("Has seleccionado la opción 2:")
        print("CONTAR INFORMACIÓN: Mostrar el número de partidos que se han disputado en este mundial.")
        time.sleep(1)
        print()
        print("Nº DE PARTIDOS")
        print(contar_informacion(datos))
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 3
    if opcion==3:
        print("Has seleccionado la opción 3:")
        print("BUSCAR O FILTRAR INFORMACIÓN: Mostrar todos los partidos de la selección dada, es decir, todos los rivales a los que se ha enfrentado.")
        time.sleep(1)
        print()
        print("ATENCIÓN: Debes introducir el nombre de la selección en inglés.")
        seleccion=str(input("Selección: "))
        while validar_selecciones(datos,seleccion)!=True:
            seleccion=str(input("No existe esta selección. Vuelva a intentarlo: "))
        print()
        print("RIVALES")
        for elem in buscar_informacion(datos,seleccion):
            print(elem)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 4
    if opcion==4:
        print("Has seleccionado la opción 4:")
        print("BUSCAR INFORMACIÓN RELACIONADA: Mostrar los partidos que han terminado con un resultado dado.")
        time.sleep(1)
        print()
        gol1=int(input("Goles locales: "))
        gol2=int(input("Goles visitantes: "))
        lista_locales,lista_visitantes=buscar_informacion_relacionada(datos,gol1,gol2)
        print()
        print("PARTIDOS ",gol1,"-",gol2,"")
        for loc,vis in zip(lista_locales,lista_visitantes):
            print(" ",loc,"-",vis)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 5
    if opcion==5:
        print("Has seleccionado la opción 5:")
        print("ÚLTIMO PARTIDO: Mostrar el último partido que jugó en esta competición una selección dada. Tiene que mostrar la fecha y la hora en que se disputó, la selección rival y el resultado final del encuentro.")
        time.sleep(1)
        print()
        print("ATENCIÓN: Debes introducir el nombre de la selección en inglés.")
        seleccion=str(input("Selección: "))
        while validar_selecciones(datos,seleccion)!=True:
            seleccion=str(input("No existe esta selección. Vuelva a intentarlo: "))
        lista_fecha,lista_partido,lista_goles_descanso,lista_goles=ejercicio_libre(datos,seleccion)
        print()
        print("FECHA")
        print(" ",lista_fecha[0],lista_fecha[1])
        print("PARTIDO")
        print(" ",lista_partido[0],"-",lista_partido[1],)
        print("DESCANSO")
        print(" ",lista_goles_descanso[0],"-",lista_goles_descanso[1])
        print("RESULTADO FINAL")
        print(" ",lista_goles[0],"-",lista_goles[1],)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #Salir
    if opcion==6:
        print("Has seleccionado la opción 6:")
        print("SALIR")
        time.sleep(1)
        print("FIN DEL PROGRAMA")
        break