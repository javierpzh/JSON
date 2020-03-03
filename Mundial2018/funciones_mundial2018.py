import json

with open("mundial2018.json") as fichero:
    datos=json.load(fichero)

def listar_informacion(datos):
    lista_selecciones=[]
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            lista_selecciones.append(seleccion["team1"]["name"])
    return lista_selecciones

def contar_informacion(datos):
    lista_selecciones=[]
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            lista_selecciones.append(seleccion["team1"]["name"])
    return len(lista_selecciones)