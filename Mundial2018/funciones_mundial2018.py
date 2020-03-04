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

def buscar_informacion(datos,cadena):
    lista_partidos_locales=[]
    lista_partidos_visitantes=[]
    lista_partidos=[]
    lista=[]
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            local=(seleccion["team1"]["name"])
            visitante=(seleccion["team2"]["name"])
            lista_partidos.append(local)
            lista_partidos.append(visitante)
            lista_partidos_locales.append(local)
            lista_partidos_visitantes.append(visitante)
            if cadena==seleccion["team1"]["name"]:
                visitante=(seleccion["team2"]["name"])
                lista.append(visitante)
            elif cadena==seleccion["team2"]["name"]:
                local=(seleccion["team1"]["name"])
                lista.append(local)
    return lista

def buscar_informacion_relacionada(datos,cadena,cadena2):
    lista1=[]
    lista2=[]
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            if cadena==seleccion["score1"] and cadena2==seleccion["score2"]:
                local=(seleccion["team1"]["name"])
                visitante=(seleccion["team2"]["name"])
                lista1.append(local)
                lista2.append(visitante)
    return lista1,lista2