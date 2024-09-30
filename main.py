from campeonato import Campeonato
from menu import menu_inicio, formar_delegaciones, clase_deportista, cargar_datos

delegaciones = cargar_datos('delegaciones.csv')
deportistas = cargar_datos('deportistas.csv')
delegaciones = formar_delegaciones(delegaciones, deportistas)
deportistas = clase_deportista(deportistas, delegaciones)
campeonato = Campeonato()
menu_inicio(delegaciones, deportistas, campeonato)