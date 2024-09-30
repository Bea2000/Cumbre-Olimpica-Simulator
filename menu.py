from campeonato import Campeonato
from deportes import Deporte, Deportista, Atletismo, Natacion, Gimnasia, Ciclismo
from delegaciones import IEEEsparta, DCCrotona, Delegacion
import parametros as p
import random

def menu_inicio(delegaciones, deportistas, campeonato):
    print("*** Menu de Inicio ***\n")
    print("[0] Comenzar partida")
    print("[1] Salir")
    print("\nSeleccione una opcion: ", end="")
    opcion = input()
    if opcion == "0":
        print("\nSeleccione un nombre de usuario: ", end="")
        usuario = input()
        while not usuario.isalpha():
            print("Opción no valida. Intente nuevamente\n")
            print("\nSeleccione un nombre de usuario: ", end="")
            usuario = input()
        print("\nSeleccione un nombre para tu rival: ", end="")
        rival = input()
        while not rival.isalpha():
            print("Opcion no valida. Intente nuevamente\n")
            print("\nSeleccione un nombre para tu rival: ", end="")
            rival = input()
        print("\n[0] DCCrotona")
        print("[1] IEEEsparta")
        print("\nElija una delegación: ",end="")
        delegacion = input()
        while delegacion != "0" and delegacion != "1":
            print("Opción no válida. Intente nuevamente\n")
            print("[0] DCCrotona")
            print("[1] IEEEsparta")
            print("Elija una delegación: ",end="")
            delegacion = input()
        if delegacion == "0":
            delegacion_jugador = delegaciones[0]
            delegacion_jugador.entrenador = usuario
            delegacion_rival = delegaciones[1]
            delegacion_rival.entrenador = rival
        elif delegacion == "1":
            delegacion_jugador = delegaciones[1]
            delegacion_jugador.entrenador = usuario
            delegacion_rival = delegaciones[0]
            delegacion_rival.entrenador = rival
        return menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    if opcion == "1":
        return "salir"
    else:
        print("Opción no válida. Intente nuevamente\n")
        return menu_inicio(delegaciones, deportistas, campeonato)

def menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato):
    print("\n*** Menu Principal ***")
    print("[0] Menu entrenador")
    print("[1] Simular competencia")
    print("[2] Mostrar estado")
    print("[3] Salir")
    print("\nSeleccione una opción: ", end="")
    opcion = input()
    if opcion == "0":
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "1":
        if campeonato.dia_actual != p.DIAS_COMPETENCIA-1:
            print("\nDebes elegir a tus cuatros competidores")
            jug_propios = []
            for persona in delegacion_jugador.equipo:
                print(persona.nombre)
            print("\nSeleccione un jugador para la competencia de Atletismo: ")
            jugador = input()
            existe = False
            while existe == False:
                for persona in delegacion_jugador.equipo:
                    if jugador == persona.nombre:
                        existe = True
                        jug_propios.append(persona)
                if existe == False:
                    print("Seleccione una opción correcta: ")
                    jugador = input()
            print("\nSeleccione un jugador para la competencia de Ciclismo: ")
            jugador = input()
            existe = False
            while existe == False:
                for persona in delegacion_jugador.equipo:
                    if jugador == persona.nombre:
                        existe = True
                        jug_propios.append(persona)
                if existe == False:
                    print("Seleccione una opción correcta: ")
                    jugador = input()
            print("\nSeleccione un jugador para la competencia de Gimnasia: ")
            jugador = input()
            existe = False
            while existe == False:
                for persona in delegacion_jugador.equipo:
                    if jugador == persona.nombre:
                        existe = True
                        jug_propios.append(persona)
                if existe == False:
                    print("Seleccione una opción correcta: ")
                    jugador = input()
            print("\nSeleccione un jugador para la competencia de Natación: ")
            jugador = input()
            existe = False
            while existe == False:
                for persona in delegacion_jugador.equipo:
                    if jugador == persona.nombre:
                        existe = True
                        jug_propios.append(persona)
                if existe == False:
                    print("Seleccione una opción correcta: ")
                    jugador = input()
            jug_rivales = []
            for i in range(0,4):
                jugador = random.choice(delegacion_rival.equipo)
                jug_rivales.append(jugador)
            del_propia = delegacion_jugador
            del_rival = delegacion_rival
            campeonato.realizar_competencia(jug_propios, jug_rivales, del_propia, del_rival)
            return menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato)
        elif campeonato.dia_actual == p.DIAS_COMPETENCIA-1:
            campeonato.mostrar_estado(delegacion_jugador, delegacion_rival)
            resultados = open('resultados,txt','w')
            resultados.write(f"Medallas {delegacion_jugador} = {delegacion_jugador.medallas}")
            resultados.write(f"Medallas {delegacion_rival} = {delegacion_rival.medallas}")
            resultados.close()
            print("\n¡Ha terminado el campeonato!")
            print("[0] Salir")
            print("[1] Nueva simulación")
            print("\nSeleccione una opción: ", end="")
            opcion = input()
            while opcion != "0" and opcion != "1":
                print("\nSeleccione una opción válida: ", end="")
                opcion = input()
            if opcion == "0":
                return "salir"
            elif opcion == "1":
                delegaciones = cargar_datos('delegaciones.csv')
                deportistas = cargar_datos('deportistas.csv')
                delegaciones = formar_delegaciones(delegaciones, deportistas)
                deportistas = clase_deportista(deportistas)
                campeonato = Campeonato()
                return menu_inicio(delegaciones, deportistas, campeonato)
    elif opcion == "2":
        campeonato.mostrar_estado(delegacion_jugador, delegacion_rival)
        print("\n [0] Volver")
        print("\nSeleccione una opción: ", end="")
        opcion = input()
        while opcion != "0":
            print("\nSeleccione una opción válida: ", end="")
            opcion = input()
        if opcion == "0":
            return menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "3":
        return "salir"
    else:
        print("Opción no válida. Intente nuevamente\n")
        return menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato)   

def menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato):
    print("\n*** Menu Entrenador ***")
    print("[0] Fichar")
    print("[1] Entrenar")
    print("[2] Sanar")
    print("[3] Comprar tecnología")
    print("[4] Usar habilidad especial")
    print("[5] Volver al menú principal")
    print("[6] Salir del programa")
    print("\nSeleccione una opción: ", end="")
    opcion = input()
    if opcion == "0":
        delegacion_jugador.fichar_deportistas(deportistas)
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "1":
        delegacion_jugador.entrenar_deportistas()
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "2":
        delegacion_jugador.sanar_lesiones()
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "3":
        delegacion_jugador.comprar_tecnologia()
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "4":
        if delegacion_jugador.habilidad_especial == False:
            delegacion_jugador.utilizar_habilidad_especial()
        else:
            print("Ya has usado tu habilidad especial")
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "5":
        return menu_principal(delegacion_jugador, delegacion_rival, deportistas, campeonato)
    elif opcion == "6":
        return "salir"
    else:
        print("Opción no válida. Intente nuevamente")
        return menu_entrenador(delegacion_jugador, delegacion_rival, deportistas, campeonato)

#asigna clase a cada jugador de la delegacion
def formar_delegaciones(delegaciones, deportistas):
    if delegaciones[0][1] == 'IEEEsparta':
        ieee = delegaciones[0]
        dcc = delegaciones[1]
    else:
        ieee = delegaciones[1]
        dcc = delegaciones[0]
    equipoIEEE = ieee[2].split(";")
    lista_equipo = []
    for persona in equipoIEEE:
        for n in deportistas:
            if n[0] == persona:
                deportista = Deportista(n[0], n[1] ,n[2] ,n[3] , n[4], n[5], n[6])
                lista_equipo.append(deportista)
    equipoIEEE = IEEEsparta(None, ieee[0], lista_equipo, ieee[3], ieee[4])
    equipoDCC = dcc[2].split(";")
    lista_equipo = []
    for persona in equipoDCC:
        for n in deportistas:
            if n[0] == persona:
                deportista = Deportista(n[0], n[1] ,n[2] ,n[3] , n[4], n[5], n[6])
                lista_equipo.append(deportista)
    equipoDCC = DCCrotona(None, dcc[0], lista_equipo, dcc[3], dcc[4])
    return [equipoIEEE, equipoDCC]

#carga archivos csv
def cargar_datos(path):
    arc = open(path)
    archivo = arc.readlines()
    arc.close()
    data = [info.strip().split(", ") for info in archivo]
    data = data[1:]
    lista = []
    for info in data:
        info = info[0].split(",")
        lista.append(info)
    return lista

#crea una lista con la clase deportista para cada deportista en deportistas.csv
def clase_deportista(deportistas, delegaciones):
    lista = []
    for dep in deportistas:
        agregar = True
        for dep2 in delegaciones[0].equipo:
            if dep2.nombre == dep[0]:
                agregar = False
        for dep2 in delegaciones[1].equipo:
            if dep2.nombre == dep[0]:
                agregar = False
        if agregar == True:
            deportista = Deportista(dep[0], dep[1], dep[2], dep[3], dep[4], dep[5], dep[6])
            lista.append(deportista)
    return lista
