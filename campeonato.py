import random
import parametros as p
from deportes import Deporte, Deportista, Atletismo, Ciclismo, Natacion, Gimnasia
from delegaciones import Delegacion, IEEEsparta, DCCrotona

class Campeonato:
    
    def __init__(self):
        self.dia_actual = p.DIA_INICIO
        self.medallero = {'Atletismo_jugador':0}
        self.medallero['Atletismo_rival'] = 0
        self.medallero['Ciclismo_jugador'] = 0
        self.medallero['Ciclismo_rival'] = 0
        self.medallero['Gimnasia_jugador'] = 0
        self.medallero['Gimnasia_rival'] = 0
        self.medallero['Natacion_jugador'] = 0
        self.medallero['Natacion_rival'] = 0

    def realizar_competencia(self, jugadores_propios, jugadores_rivales, del_propia, del_rival):
        resultados = open('resultados.txt','a')
        if self.dia_actual != p.DIAS_COMPETENCIA-1:
            print(f"\n***** Día {self.dia_actual}: Atletismo *****")
            resultados.write(f'Ganador dia {self.dia_actual}, ')
            resultados.write(f'competencia de atletismo = ')
            jugador1 = jugadores_propios[0]
            jugador2 = jugadores_rivales[0]
            valido = Atletismo().validez_de_competencia(jugador1, jugador2, del_propia, del_rival)
            if valido[0] == False and valido[1] == True:
                resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                ganador = True
                self.medallero['Atletismo_rival'] += 1
                self.premiar(jugador2, jugador1, del_rival, del_propia)
            elif valido[1] == False and valido[0] == True:
                resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                self.medallero['Atletismo_jugador'] += 1
                ganador = True
                self.premiar(jugador1, jugador2, del_propia, del_rival)
            elif valido[0] == False and valido[1] == False:
                resultados.write(f'empate')
                ganador = "empate"
                print("Ha habido un empate")
            else:
                ganador = False
            if ganador == False:
                ganador = Atletismo().calcular_ganador(jugador1, jugador2)
                if ganador == jugador1:
                    resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                    self.medallero['Atletismo_jugador'] += 1
                    self.premiar(jugador1, jugador2, del_propia, del_rival)
                elif ganador == jugador2:
                    resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                    self.medallero['Atletismo_rival'] += 1
                    self.premiar(jugador2, jugador1, del_rival, del_propia)
                else:
                    resultados.write(f'empate')
                    print("Ha habido un empate")
            print(f"\n***** Día {self.dia_actual}: Ciclismo *****")
            resultados.write(f'\nGanador dia {self.dia_actual}, ')
            resultados.write(f'competencia de ciclismo = ')
            jugador1 = jugadores_propios[1]
            jugador2 = jugadores_rivales[1]
            Ciclismo().validez_de_competencia(jugador1, jugador2, del_propia, del_rival)
            if valido[0] == False and valido[1] == True:
                resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                ganador = True
                self.medallero['Ciclismo_rival'] += 1
                self.premiar(jugador2, jugador1, del_rival, del_propia)
            elif valido[1] == False and valido[0] == True:
                resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                ganador = True
                self.medallero['Ciclismo_jugador'] += 1
                self.premiar(jugador1, jugador2, del_propia, del_rival)
            elif valido[0] == False and valido[1] == False:
                ganador = "empate"
                resultados.write('empate')
                print("Ha habido un empate")
            else:
                ganador = False
            if ganador == False:
                ganador = Ciclismo().calcular_ganador(jugador1, jugador2)
                if ganador == jugador1:
                    resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                    self.medallero['Ciclismo_jugador'] += 1
                    self.premiar(jugador1, jugador2, del_propia, del_rival)
                elif ganador == jugador2:
                    resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                    self.medallero['Ciclismo_rival'] += 1
                    self.premiar(jugador2, jugador1, del_rival, del_propia)
                else:
                    resultados.write('empate')
                    print("Ha habido un empate")
            print(f"\n***** Día {self.dia_actual}: Gimnasia *****")
            resultados.write(f'\nGanador dia {self.dia_actual}, ')
            resultados.write(f'competencia de gimnasia = ')
            jugador1 = jugadores_propios[2]
            jugador2 = jugadores_rivales[2]
            Gimnasia().validez_de_competencia(jugador1, jugador2, del_propia, del_rival)
            if valido[0] == False and valido[1] == True:
                resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                ganador = True
                self.medallero['Gimnasia_rival'] += 1
                self.premiar(jugador2, jugador1, del_rival, del_propia)
            elif valido[1] == False and valido[0] == True:
                resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                ganador = True
                self.medallero['Gimnasia_jugador'] += 1
                self.premiar(jugador1, jugador2, del_propia, del_rival)
            elif valido[0] == False and valido[1] == False:
                resultados.write('empate')
                ganador = "empate"
                print("Ha habido un empate")
            else:
                ganador = False
            if ganador == False:
                ganador = Gimnasia().calcular_ganador(jugador1, jugador2)
                if ganador == jugador1:
                    resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                    self.medallero['Gimnasia_jugador'] += 1
                    self.premiar(jugador1, jugador2, del_propia, del_rival)
                elif ganador == jugador2:
                    resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                    self.medallero['Gimnasia_rival'] += 1
                    self.premiar(jugador2, jugador1, del_rival, del_propia)
                else:
                    resultados.write('empate')
                    print("Ha habido un empate")
            print(f"\n***** Día {self.dia_actual}: Natación *****")
            resultados.write(f'\nGanador dia {self.dia_actual}, ')
            resultados.write(f'competencia de natación = ')
            jugador1 = jugadores_propios[3]
            jugador2 = jugadores_rivales[3]
            Natacion().validez_de_competencia(jugador1, jugador2, del_propia, del_rival)
            if valido[0] == False and valido[1] == True:
                resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                ganador = True
                self.medallero['Natacion_rival'] += 1
                self.premiar(jugador2, jugador1, del_rival, del_propia)
            elif valido[1] == False and valido[0] == True:
                resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                ganador = True
                self.medallero['Natacion_jugador'] += 1
                self.premiar(jugador1, jugador2, del_propia, del_rival)
            elif valido[0] == False and valido[1] == False:
                resultados.write('empate')
                ganador = "empate"
                print("Ha habido un empate")
            else:
                ganador = False
            if ganador == False:
                ganador = Natacion().calcular_ganador(jugador1, jugador2)
                if ganador == jugador1:
                    resultados.write(f'{jugador1.nombre} del equipo {del_propia}')
                    self.medallero['Natacion_jugador'] += 1
                    self.premiar(jugador1, jugador2, del_propia, del_rival)
                elif ganador == jugador2:
                    resultados.write(f'{jugador2.nombre} del equipo {del_rival}')
                    self.medallero['Natacion_rival'] += 1
                    self.premiar(jugador2, jugador1, del_rival, del_propia)
                else:
                    print("Ha habido un empate")
                    resultados.write('empate')
            self.dia_actual += 1
        resultados.write("\n")
        resultados.close()

    def premiar(self, ganador, perdedor, delegacion_ganadora, delegacion_perdedora):
        print(f"Felicidades a {ganador.nombre} y a {delegacion_ganadora}!")
        delegacion_ganadora.medallas += 1
        if delegacion_ganadora == "DCCrotona":
            ganador.moral += p.PONDERACION_GANADOR_MORAL*p.AUMENTO_MORAL_GANADOR
        else:
            ganador.moral += p.AUMENTO_MORAL_GANADOR
        delegacion_ganadora.calcular_moral()
        perdedor.moral -= p.PERDIDA_MORAL_PERDEDOR
        delegacion_perdedora.calcular_moral()
        delegacion_perdedora.ex_resp -= p.PERDIDA_EX_RESP_PERDEDOR
        delegacion_ganadora.dinero += p.AUMENTO_DINERO_GANADOR


    def mostrar_estado(self, delegacion_jugador, delegacion_rival):
        print("*** ESTADO DE LAS DELEGACIONES Y DEPORTISTAS ACTUAL ***\n")
        print(delegacion_jugador)
        print(f"Entrenador: {delegacion_jugador.entrenador}")
        delegacion_jugador.calcular_moral()
        print(f"Moral del equipo: {delegacion_jugador.moral}")
        print(f"Medallas: {delegacion_jugador.medallas}")
        print(f"Dinero: {delegacion_jugador.dinero}")
        print(f"Excelencia y respeto: {delegacion_jugador.ex_resp}")
        print(f"Implementos médicos: {delegacion_jugador.imp_med}")
        print(f"Implementos deportivos: {delegacion_jugador.imp_dep}")
        print("\n Equipo deportivo")
        for dep in delegacion_jugador.equipo:
            print("Nombre deportista    Velocidad    Resistencia   Flexibilidad     Lesión")
            res = dep.resistencia
            flex = dep.flexibilidad
            print(f"{dep.nombre: <19}{dep.velocidad: <22}{res: <13}{flex: ^10}{dep.lesionado: <12}")
        print("************************************************************************\n")
        print(delegacion_rival)
        print(f"Entrenador: {delegacion_rival.entrenador}")
        delegacion_rival.calcular_moral()
        print(f"Moral del equipo: {delegacion_rival.moral}")
        print(f"Medallas: {delegacion_rival.medallas}")
        print(f"Dinero: {delegacion_rival.dinero}")
        print(f"Excelencia y respeto: {delegacion_rival.ex_resp}")
        print(f"Implementos médicos: {delegacion_rival.imp_med}")
        print(f"Implementos deportivos: {delegacion_rival.imp_dep}")
        print("\n Equipo deportivo")
        for dep in delegacion_rival.equipo:
            print("Nombre deportista    Velocidad    Resistencia   Flexibilidad     Lesión")
            res = dep.resistencia
            flex = dep.flexibilidad
            print(f"{dep.nombre: <19}{dep.velocidad: <22}{res: <13}{flex: ^10}{dep.lesionado: <12}")
        print("************************************************************************\n")
        print(f"\nDía {self.dia_actual} : Entrenamiento")
        print("Medallero")
        print(f"\n*** {delegacion_jugador} ***")
        print(f"Atletismo: {self.medallero['Atletismo_jugador']}")
        print(f"Ciclismo: {self.medallero['Ciclismo_jugador']}")
        print(f"Gimnasia: {self.medallero['Gimnasia_jugador']}")
        print(f"Natación: {self.medallero['Natacion_jugador']}")
        print(f"\n*** {delegacion_rival} ****")
        print(f"Atletismo: {self.medallero['Atletismo_rival']}")
        print(f"Ciclismo: {self.medallero['Ciclismo_rival']}")
        print(f"Gimnasia: {self.medallero['Gimnasia_rival']}")
        print(f"Natación: {self.medallero['Natacion_rival']}")
