import random
import parametros as p

class Deportista:

    def __init__(self, nombre, velocidad, resistencia, flexibilidad, moral, lesionado, precio):
        self.nombre = nombre
        self.__velocidad = int(velocidad)
        self.__resistencia = int(resistencia)
        self.__flexibilidad = int(flexibilidad) 
        self.__moral = int(moral)
        self.lesionado = lesionado
        self.precio = int(precio)
    
    @property
    def moral(self):
        return self.__moral
    
    @moral.setter
    def moral(self, nuevo_valor):
        if nuevo_valor < p.MIN_MORAL:
            self.__moral = p.MIN_MORAL
        elif nuevo_valor > p.MAX_MORAL:
            self.__moral = p.MAX_MORAL
        else:
            self.__moral = nuevo_valor
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, nuevo_valor):
        if nuevo_valor < p.MIN_VELOCIDAD:
            self.__velocidad = p.MIN_VELOCIDAD
        elif nuevo_valor > p.MAX_VELOCIDAD:
            self.__velocidad = p.MAX_VELOCIDAD
        else: 
            self.__velocidad = nuevo_valor

    @property
    def resistencia(self):
        return self.__resistencia
    
    @resistencia.setter
    def resistencia(self, nuevo_valor):
        if nuevo_valor < p.MIN_RESISTENCIA:
            self.__resistencia = p.MIN_RESISTENCIA
        elif nuevo_valor > p.MAX_RESISTENCIA:
            self.__resistencia = p.MAX_RESISTENCIA
        else:
            self.__resistencia = nuevo_valor

    @property
    def flexibilidad(self):
        return self.__flexibilidad
    
    @flexibilidad.setter
    def flexibilidad(self, nuevo_valor):
        if nuevo_valor < p.MIN_FLEXIBILIDAD:
            self.__flexibilidad = p.MIN_FLEXIBILIDAD
        elif nuevo_valor > p.MAX_FLEXIBILIDAD:
            self.__flexibilidad = p.MAX_FLEXIBILIDAD
        else:
            self.__flexibilidad = nuevo_valor

    def entrenar(self, atributo):
        if atributo == "velocidad":
            self.velocidad += p.PUNTOS_ENTRENAMIENTO
        elif atributo == "resistencia":
            self.resistencia += p.PUNTOS_ENTRENAMIENTO
        elif atributo == "flexibilidad":
            self.flexibilidad += p.PUNTOS_ENTRENAMIENTO

    def lesionarse(self):
        self.lesionado = True

class Deporte:

    def validez_de_competencia(self, deportista1, deportista2, del1, del2):
        validez1 = True
        validez2= True
        if deportista1.lesionado == True:
            validez1 = False
        if deportista2.lesionado == True:
            validez2 = False
        if self.implemento == True:
            if del1.imp_dep < p.NIVEL_IMPLEMENTOS:
                validez1 = False
            if del2.imp_dep < p.NIVEL_IMPLEMENTOS:
                validez2 = False
        return [validez1,validez2]

    def calcular_ganador(self):
        pass

class Atletismo(Deporte):

    def __init__(self):
        super().__init__()
        self.implemento = p.IMP_ATLETISMO
        self.riesgo = p.RIESGO_ATLETISMO

    def calcular_ganador(self, dep1, dep2):
        vel_dep1 = p.PONDERACION_VEL_ATLETISMO*dep1.velocidad
        res_dep1 = p.PONDERACION_RES_ATLETISMO*dep1.resistencia
        mor_dep1 = p.PONDERACION_MOR_ATLETISMO*dep1.moral
        formula_dep1 = vel_dep1 + res_dep1 + mor_dep1
        if p.PUNTAJE_MINIMO > formula_dep1:
            formula_dep1 = p.PUNTAJE_MINIMO
        vel_dep2 = p.PONDERACION_VEL_ATLETISMO*dep2.velocidad
        res_dep2 = p.PONDERACION_RES_ATLETISMO*dep2.resistencia
        mor_dep2 = p.PONDERACION_MOR_ATLETISMO*dep2.moral
        formula_dep2 = vel_dep2 + res_dep2 + mor_dep2
        lesionado1 = random.uniform(0, 1)
        if lesionado1 >= self.riesgo:
            dep1.lesionarse()
        lesionado2 = random.uniform(0, 1)
        if lesionado2 >= self.riesgo:
            dep2.lesionarse()
        if p.PUNTAJE_MINIMO > formula_dep2:
            formula_dep2 = p.PUNTAJE_MINIMO
        if formula_dep2 < formula_dep1:
            return dep1
        elif formula_dep2 > formula_dep1:
            return dep2
        else:
            return "Empate"

class Ciclismo(Deporte):
  
    def __init__(self):
        super().__init__()
        self.implemento = p.IMP_CICLISMO
        self.riesgo = p.RIESGO_CICLISMO
    
    def calcular_ganador(self, dep1, dep2):
        vel_dep1 = p.PONDERACION_VEL_CICLISMO*dep1.velocidad
        res_dep1 = p.PONDERACION_RES_CICLISMO*dep1.resistencia
        flex_dep1 = p.PONDERACION_FLEX_CICLISMO*dep1.flexibilidad
        formula_dep1 = vel_dep1 + res_dep1 + flex_dep1
        if p.PUNTAJE_MINIMO > formula_dep1:
            formula_dep1 = p.PUNTAJE_MINIMO
        vel_dep2 = p.PONDERACION_VEL_CICLISMO*dep2.velocidad
        res_dep2 = p.PONDERACION_RES_CICLISMO*dep2.resistencia
        flex_dep2 = p.PONDERACION_FLEX_CICLISMO*dep2.flexibilidad
        formula_dep2 = vel_dep2 + res_dep2 + flex_dep2
        lesionado1 = random.uniform(0, 1)
        if lesionado1 >= self.riesgo:
            dep1.lesionarse()
        lesionado2 = random.uniform(0, 1)
        if lesionado2 >= self.riesgo:
            dep2.lesionarse()
        if p.PUNTAJE_MINIMO > formula_dep2:
            formula_dep2 = p.PUNTAJE_MINIMO
        if formula_dep2 < formula_dep1:
            return dep1
        elif formula_dep2 > formula_dep1:
            return dep2
        else:
            return "Empate"

class Gimnasia(Deporte):

    def __init__(self):
        super().__init__()
        self.implemento = p.IMP_GIMNASIA
        self.riesgo = p.RIESGO_GIMNASIA
    
    def calcular_ganador(self, dep1, dep2):
        flex_dep1 = p.PONDERACION_FLEX_GIMNASIA*dep1.flexibilidad
        res_dep1 = p.PONDERACION_RES_GIMNASIA*dep1.resistencia
        mor_dep1 = p.PONDERACION_MOR_GIMNASIA*dep1.moral
        formula_dep1 = flex_dep1 + res_dep1 + mor_dep1
        if p.PUNTAJE_MINIMO > formula_dep1:
            formula_dep1 = p.PUNTAJE_MINIMO
        flex_dep2 = p.PONDERACION_FLEX_GIMNASIA*dep2.flexibilidad
        res_dep2 = p.PONDERACION_RES_GIMNASIA*dep2.resistencia
        mor_dep2 = p.PONDERACION_MOR_GIMNASIA*dep2.moral
        formula_dep2 = flex_dep2 + res_dep2 + mor_dep2
        lesionado1 = random.uniform(0, 1)
        if lesionado1 >= self.riesgo:
            dep1.lesionarse()
        lesionado2 = random.uniform(0, 1)
        if lesionado2 >= self.riesgo:
            dep2.lesionarse()
        if p.PUNTAJE_MINIMO > formula_dep2:
            formula_dep2 = p.PUNTAJE_MINIMO
        if formula_dep2 < formula_dep1:
            return dep1
        elif formula_dep2 > formula_dep1:
            return dep2
        else:
            return "Empate"

class Natacion(Deporte):

    def __init__(self):
        super().__init__()
        self.implemento = p.IMP_NATACION
        self.riesgo = p.RIESGO_NATACION
    
    def calcular_ganador(self, dep1, dep2):
        vel_dep1 = p.PONDERACION_VEL_NATACION*dep1.velocidad
        res_dep1 = p.PONDERACION_RES_NATACION*dep1.resistencia
        flex_dep1 = p.PONDERACION_FLEX_NATACION*dep1.flexibilidad
        formula_dep1 = vel_dep1 + res_dep1 + flex_dep1
        if p.PUNTAJE_MINIMO > formula_dep1:
            formula_dep1 = p.PUNTAJE_MINIMO
        vel_dep2 = p.PONDERACION_VEL_NATACION*dep2.velocidad
        res_dep2 = p.PONDERACION_RES_NATACION*dep2.resistencia
        flex_dep2 = p.PONDERACION_FLEX_NATACION*dep2.flexibilidad
        formula_dep2 = vel_dep2 + res_dep2 + flex_dep2
        lesionado1 = random.uniform(0, 1)
        if lesionado1 >= self.riesgo:
            dep1.lesionarse()
        lesionado2 = random.uniform(0, 1)
        if lesionado2 >= self.riesgo:
            dep2.lesionarse()
        if p.PUNTAJE_MINIMO > formula_dep2:
            formula_dep2 = p.PUNTAJE_MINIMO
        if formula_dep2 < formula_dep1:
            return dep1
        elif formula_dep2 > formula_dep1:
            return dep2
        else:
            return "Empate"
