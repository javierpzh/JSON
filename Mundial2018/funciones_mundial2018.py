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
            local=(seleccion["team1"]["name"])
            visitante=(seleccion["team2"]["name"])
            gollocal=(seleccion["score1"])
            golvisitante=(seleccion["score2"])
            print("",local,"-",visitante,"")
            print("",gollocal,"-",golvisitante,"")
    print("GANADOR")
    return local

def buscar_informacion(datos,cadena):
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            if cadena in seleccion["team1"]["name"] or cadena in seleccion["team2"]["name"]:
                local=(seleccion["team1"]["name"])
                visitante=(seleccion["team2"]["name"])
                gollocal=(seleccion["score1"])
                golvisitante=(seleccion["score2"])
                print("",local,"-",visitante,"")
                print("",gollocal,"-",golvisitante,"")
    return ""

def buscar_informacion_relacionada(datos,cadena,cadena2):
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            if cadena==seleccion["score1"] and cadena2==seleccion["score2"]:
                lista_goleadores_local=[]
                lista_goleadores_visitante=[]
                local=(seleccion["team1"]["name"])
                visitante=(seleccion["team2"]["name"])
                gollocal=(seleccion["score1"])
                golvisitante=(seleccion["score2"])
                print("",local,"-",visitante,"")
                print("",gollocal,"-",golvisitante,"")
                for goleadores in seleccion["goals1"]:
                    lista_goleadores_local.append(goleadores["name"])
                print("   ",local,"")
                for goles in lista_goleadores_local:
                    print(goles)
                for goleadores in seleccion["goals2"]:
                    lista_goleadores_visitante.append(goleadores["name"])
                print("   ",visitante,"")
                for goles in lista_goleadores_visitante:
                    print(goles)
                print()
    return ""

def ejercicio_libre(datos,cadena):
    for rondas in datos["rounds"]:
        for seleccion in rondas["matches"]:
            if cadena in seleccion["team1"]["name"] or cadena in seleccion["team2"]["name"]:
                lista_goleadores_local=[]
                lista_goleadores_visitante=[]
                fecha=(seleccion["date"])
                hora=(seleccion["time"])
                print(fecha,hora)
                local=(seleccion["team1"]["name"])
                visitante=(seleccion["team2"]["name"])
                gollocal=(seleccion["score1"])
                golvisitante=(seleccion["score2"])
                print("",local,"-",visitante,"")
                print("",gollocal,"-",golvisitante,"")
                descansolocal=(seleccion["score1i"])
                descansovisitante=(seleccion["score2i"])
                print("Descanso: ",descansolocal,"-",descansovisitante,"")
                if gollocal>0:
                    for goleadores in seleccion["goals1"]:
                        lista_goleadores_local.append(goleadores["name"])
                    print("   ",local,"")
                    for goles in lista_goleadores_local:
                        print(goles)
                if golvisitante>0:
                    for goleadores in seleccion["goals2"]:
                        lista_goleadores_visitante.append(goleadores["name"])
                    print("   ",visitante,"")
                    for goles in lista_goleadores_visitante:
                        print(goles)
                print()
    return ""
