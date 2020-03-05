import json

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

def ejercicio_libre(datos,cadena):
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            if cadena in seleccion["team1"]["name"] or cadena in seleccion["team2"]["name"]:
                lista_fecha=[]
                fecha=(seleccion["date"])
                hora=(seleccion["time"])
                lista_fecha.append(fecha)
                lista_fecha.append(hora)
                local=(seleccion["team1"]["name"])
                visitante=(seleccion["team2"]["name"])
                lista_partido=[]
                lista_partido.append(local)
                lista_partido.append(visitante)
                lista_goles_descanso=[]
                descansolocal=(seleccion["score1i"])
                descansovisitante=(seleccion["score2i"])
                lista_goles_descanso.append(descansolocal)
                lista_goles_descanso.append(descansovisitante)
                gollocal=(seleccion["score1"])
                golvisitante=(seleccion["score2"])
                lista_goles=[]
                lista_goles.append(gollocal)
                lista_goles.append(golvisitante)
    return lista_fecha,lista_partido,lista_goles_descanso,lista_goles
