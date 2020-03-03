from funciones_mundial2018 import *

menu=print('''OPCIONES:
1- LISTAR INFORMACIÓN: Listar de todos los partidos, las selecciones que han jugado como locales este mundial.
2- CONTAR INFORMACIÓN: Mostrar los partidos y el resultado que tiene cada uno, además indica que selección ha ganado el mundial.
3- BUSCAR O FILTRAR INFORMACIÓN: Mostrar todos los partidos de la selección dada.
4- BUSCAR INFORMACIÓN RELACIONADA: Mostrar los partidos que han terminado con un resultado dado, y la lista de sus goleadores.
5- ÚLTIMO PARTIDO: Mostrar el último partido que jugó en esta competición una selección dada. Tiene que mostrar la fecha en que se disputó, junto con su resultado final, su resultado al descanso y sus goles, es decir, el minuto del gol y su autor.
6- SALIR
''')
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
    print(buscar_informacion(datos,cadena))

#EJERCICIO 4
if opcion==4:
    cadena=int(input("Goles locales: "))
    cadena2=int(input("Goles visitantes: "))
    print(buscar_informacion_relacionada(datos,cadena,cadena2))

#EJERCICIO 5
if opcion==5:
    cadena=str(input("Selección: "))
    print(ejercicio_libre(datos,cadena))

#Salir
if opcion==6:
    print("FIN DEL PROGRAMA")