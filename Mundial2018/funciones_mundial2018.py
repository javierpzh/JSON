#EJERCICIO 1
def listar_informacion(datos):
    lista_selecciones=[]
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            lista_selecciones.append(elem["team1"]["name"])
    return lista_selecciones

#EJERCICIO 2
def contar_informacion(datos):
    lista_selecciones=[]
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            lista_selecciones.append(elem["team1"]["name"])
    return len(lista_selecciones)

#EJERCICIO 3
def buscar_informacion(datos,seleccion):
    lista_partidos_locales=[]
    lista_partidos_visitantes=[]
    lista_partidos=[]
    lista=[]
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            local=(elem["team1"]["name"])
            visitante=(elem["team2"]["name"])
            lista_partidos.append(local)
            lista_partidos.append(visitante)
            lista_partidos_locales.append(local)
            lista_partidos_visitantes.append(visitante)
            if seleccion==elem["team1"]["name"]:
                visitante=(elem["team2"]["name"])
                lista.append(visitante)
            elif seleccion==elem["team2"]["name"]:
                local=(elem["team1"]["name"])
                lista.append(local)
    return lista

#EJERCICIO 4
def buscar_informacion_relacionada(datos,gol1,gol2):
    lista_locales=[]
    lista_visitantes=[]
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            if gol1==elem["score1"] and gol2==elem["score2"]:
                local=(elem["team1"]["name"])
                visitante=(elem["team2"]["name"])
                lista_locales.append(local)
                lista_visitantes.append(visitante)
    return lista_locales,lista_visitantes

#EJERCICIO 5
def ejercicio_libre(datos,seleccion):
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            if seleccion in elem["team1"]["name"] or seleccion in elem["team2"]["name"]:
                lista_fecha=[]
                fecha=(elem["date"])
                hora=(elem["time"])
                lista_fecha.append(fecha)
                lista_fecha.append(hora)
                local=(elem["team1"]["name"])
                visitante=(elem["team2"]["name"])
                lista_partido=[]
                lista_partido.append(local)
                lista_partido.append(visitante)
                lista_goles_descanso=[]
                descansolocal=(elem["score1i"])
                descansovisitante=(elem["score2i"])
                lista_goles_descanso.append(descansolocal)
                lista_goles_descanso.append(descansovisitante)
                gollocal=(elem["score1"])
                golvisitante=(elem["score2"])
                lista_goles=[]
                lista_goles.append(gollocal)
                lista_goles.append(golvisitante)
    return lista_fecha,lista_partido,lista_goles_descanso,lista_goles


#VALIDACIONES

def validar_selecciones(datos,seleccion):
    lista_partidos=[]
    for rondas in datos["rounds"]:
        for elem in rondas["matches"]:
            local=(elem["team1"]["name"])
            visitante=(elem["team2"]["name"])
            lista_partidos.append(local)
            lista_partidos.append(visitante)
    if seleccion in lista_partidos:
        return True