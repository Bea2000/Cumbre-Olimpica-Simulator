import parametros as p
import random

class Delegacion:

    def __init__(self, entrenador, moral, equipo, medallas, dinero):
        self.entrenador = entrenador
        self.equipo = equipo #lista de deportistas
        self.medallas = int(medallas)
        self.__moral = float(moral)
        self.__dinero = int(dinero)
        self.__ex_resp = None
        self.__imp_dep = None
        self.__imp_med = None
        self.habilidad_especial = False
    
    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, nuevo_monto):
        if nuevo_monto < 0:
            self.__dinero = 0
        else:
            self.__dinero = nuevo_monto
    
    @property
    def moral(self):
        return self.__moral
    
    @moral.setter
    def moral(self, nueva_moral):
        if nueva_moral < 0:
            self.__moral = 0
        else:
            self.__moral = nueva_moral
    
    def fichar_deportistas(self, deportistas):
        if self.moral > p.VALOR_MIN_MORAL:
            print("Deportistas disponibles para fichar:")
            for deportista in deportistas:
                print(deportista.nombre)
            print("\nSeleccione uno: ")
            opcion = input()
            for deportista in deportistas:
                if opcion == deportista.nombre:
                    print("\nEl precio por este deportista es", deportista.precio)
                    print("¿Desea fichar?")
                    print("[0] Si")
                    print("[1] No")
                    opcion = input()
                    while opcion != "0" and opcion != "1":
                        print("\nOpción inválida. Intente nuevamente")
                        print("\nEl precio por este deportista es", deportista.precio)
                        print("¿Desea fichar?")
                        print("[0] Si")
                        print("[1] No")
                        opcion = input()
                    if opcion == "0":
                        if self.dinero >= deportista.precio:
                            self.equipo.append(deportista)
                            print("¡Se ha fichado deportista con éxito!")
                            self.dinero = self.dinero - deportista.precio
                        else:
                            print("No cuentas con el dinero suficiente para realizar esta acción")
                    elif opcion == "1":
                        pass
        else:
            print("No cuentas con la moral suficiente para realizar esta acción.")

    def entrenar_deportistas(self):
        if p.COSTO_ENTRENAR > self.dinero:
            print("No cuenta con el dinero para realizar esta acción")
        else:
            for deportista in self.equipo:
                print(deportista.nombre)
            print("¿Que deportista quisiera entrenar?: ", end="")
            opcion = input()
            for deportista in self.equipo:
                if deportista.nombre == opcion:
                    print("[0] Velocidad")
                    print("[1] Resistencia")
                    print("[2] Flexibilidad")
                    print("¿Que atributo quisiera entrenar?: ")
                    opcion = input()
                    while opcion != "0" and opcion != "1" and opcion != "2":
                        print("Opcion no válida")
                        print("¿Que atributo quisiera entrenar?: ")
                        opcion = input()
                    if opcion == "0":
                        deportista.entrenar("velocidad")
                    if opcion == "1":
                        deportista.entrenar("resistencia")
                    if opcion == "2":
                        deportista.entrenar("flexibilidad")
                    deportista.moral += p.AUMENTO_MORAL
                    print("¡Se ha entrenado deportista con éxito!")
                    self.dinero = self.dinero - p.COSTO_ENTRENAR 

    def sanar_lesiones(self):
        if p.COSTO_SANAR > self.dinero:
            print("No cuenta con el dinero para realizar esta acción")
        else:
            deportistas_lesionados = 0
            for deportista in self.equipo:
                if deportista.lesionado == True:
                    print(deportista.nombre)
                    deportistas_lesionados += 1
            if deportistas_lesionados == 0:
                print("No hay deportistas lesionados.")
            else:
                print("Seleccione deportista que quiera sanar.")
                opcion = input()
                for deportista in self.equipo:
                    if deportista.nombre == opcion:
                        prob_sanar = deportista.moral * (self.imp_med + self.ex_resp) / p.DIV_PROB_SANAR
                        if p.MIN_VALOR_SANAR > prob_sanar:
                            prob_sanar = p.MIN_VALOR_SANAR
                        if p.MAX_VALOR_SANAR < prob_sanar:
                            prob_sanar = p.MAX_VALOR_SANAR
                        prob_sanar = round(prob_sanar, 1)
                        sanar = random.uniform(0, 100)
                        if sanar > prob_sanar or prob_sanar == 0:
                            print("Deportista no ha podido sanarse")
                        else:
                            print("¡El deportista se ha sanado!")
                            self.dinero = self.dinero - p.COSTO_SANAR
                            deportista.lesionado = False

    def comprar_tecnologia(self):
        if p.VALOR_TECNOLOGIA > self.dinero:
            print("No cuentas con el dinero suficiente para realizar esta acción")
        else:
            self.imp_med += self.imp_med*(p.AUMENTO_EFECTIVIDAD/100)
            self.imp_dep += self.imp_dep*(p.AUMENTO_EFECTIVIDAD/100)
            print(f"Se ha aumentado la efectividad de tus implementos en un {p.AUMENTO_EFECTIVIDAD}%")
            self.dinero = self.dinero - p.VALOR_TECNOLOGIA

    def utilizar_habilidad_especial(self):
        pass

    def calcular_moral(self):
        total_moral = 0
        for persona in self.equipo:
            total_moral += persona.moral
        self.moral = total_moral/len(self.equipo)

class IEEEsparta(Delegacion):
    
    def __init__(self, entrenador, moral, equipo, medallas, dinero):
        super().__init__(entrenador, moral, equipo, medallas, dinero)
        self.__ex_resp = round(random.uniform(p.MIN_EX_RESP_IIIE, p.MAX_EX_RESP_IIIE), 2)
        self.__imp_dep = round(random.uniform(p.MIN_IMP_DEP_IIIE, p.MAX_IMP_DEP_IIIE), 2)
        self.__imp_med = round(random.uniform(p.MIN_IMP_MED_IIIE, p.MAX_IMP_MED_IIIE), 2)
        self.habilidad_especial = False
    
    @property
    def ex_resp(self):
        return self.__ex_resp
    
    @ex_resp.setter
    def ex_resp(self, nuevo_valor):
        if self.__ex_resp < p.MIN_EX_RESP_IIIE:
            self.__ex_resp = p.MIN_EX_RESP_IIIE
        elif self.__ex_resp > p.MAX_EX_RESP_IIIE:
            self.__ex_resp = p.MAX_EX_RESP_IIIE
        else:
            self.__ex_resp = nuevo_valor
    
    @property
    def imp_dep(self):
        return self.__imp_dep
    
    @imp_dep.setter
    def imp_dep(self, nuevo_valor):
        if self.__imp_dep < p.MIN_IMP_DEP_IIIE:
            self.__imp_dep = p.MIN_IMP_DEP_IIIE
        elif self.__imp_dep > p.MAX_IMP_DEP_IIIE:
            self.__imp_dep = p.MAX_IMP_DEP_IIIE
        else:
            self.__imp_dep = nuevo_valor

    @property
    def imp_med(self):
        return self.__imp_med
    
    @imp_med.setter
    def imp_med(self, nuevo_valor):
        if self.__imp_med < p.MIN_IMP_MED_IIIE:
            self.__imp_med = p.MIN_IMP_MED_IIIE
        elif self.__imp_med > p.MAX_IMP_MED_IIIE:
            self.__imp_med = p.MAX_IMP_MED_IIIE
        else:
            self.__imp_med = nuevo_valor
    
    def entrenar_deportistas(self):
        if p.COSTO_ENTRENAR > self.dinero:
            print("No cuenta con el dinero para realizar esta acción")
        else:
            for deportista in self.equipo:
                print(deportista.nombre)
            print("¿Que deportista quisiera entrenar?: ", end="")
            opcion = input()
            for deportista in self.equipo:
                if deportista.nombre == opcion:
                    deportista.moral += p.AUMENTO_MORAL*p.PONDERACION_ENTRENAMIENTO_IIIE
                    print("¡Se ha entrenado deportista con éxito!")
                    self.dinero = self.dinero - p.COSTO_ENTRENAR 

    def utilizar_habilidad_especial(self):
        self.habilidad_especial = True
        print("Haz usado tu grito de guerra")
        for deportista in self.equipo:
            deportista.moral = deportista.max_moral
        print("Todos han aumentado su moral al máximo")
    
    def __str__(self):
        return "IEEEsparta"

class DCCrotona(Delegacion):
    def __init__(self, entrenador, moral, equipo, medallas, dinero):
        super().__init__(entrenador, moral, equipo, medallas, dinero)
        self.__ex_resp = round(random.uniform(p.MIN_EX_RESP_DCC, p.MAX_EX_RESP_DCC), 2)
        self.__imp_dep = round(random.uniform(p.MIN_IMP_DEP_DCC, p.MAX_IMP_DEP_DCC), 2)
        self.__imp_med = round(random.uniform(p.MIN_IMP_MED_DCC, p.MAX_IMP_MED_DCC), 2)
        self.habilidad_especial = False

    @property
    def ex_resp(self):
        return self.__ex_resp
    
    @ex_resp.setter
    def ex_resp(self, nuevo_valor):
        if self.__ex_resp < p.MIN_EX_RESP_DCC:
            self.ex_resp = p.MIN_EX_RESP_DCC
        elif self.__ex_resp > p.MAX_EX_RESP_DCC:
            self.__ex_resp = p.MAX_EX_RESP_DCC
        else:
            self.__ex_resp = nuevo_valor
    
    @property
    def imp_dep(self):
        return self.__imp_dep
    
    @imp_dep.setter
    def imp_dep(self, nuevo_valor):
        if self.__imp_dep < p.MIN_IMP_DEP_DCC:
            self.__imp_dep = p.MIN_IMP_DEP_DCC
        elif self.__imp_dep > p.MAX_IMP_DEP_DCC:
            self.__imp_dep = p.MAX_IMP_DEP_DCC
        else:
            self.__imp_dep = nuevo_valor

    @property
    def imp_med(self):
        return self.__imp_med
    
    @imp_med.setter
    def imp_med(self, nuevo_valor):
        if self.__imp_med < p.MIN_IMP_MED_DCC:
            self.__imp_med = p.MIN_IMP_MED_DCC
        elif self.__imp_med > p.MAX_IMP_MED_DCC:
            self.__imp_med = p.MAX_IMP_MED_DCC
        else:
            self.__imp_med = nuevo_valor
    
    def utilizar_habilidad_especial(self):
        self.habilidad_especial = True
        print(f"Felicidades DDCrotona, han ganado una medalla")
        self.medallas += 1
        self.dinero += 100

    def sanar_lesiones(self):
        if (p.COSTO_SANAR*p.PONDERACION_PAGO_SANAR_DCC) > self.dinero:
            print("No cuenta con el dinero para realizar esta acción")
        else:
            deportistas_lesionados = 0
            for deportista in self.equipo:
                if deportista.lesionado == True:
                    print(deportista.nombre)
                    deportistas_lesionados += 1
            if deportistas_lesionados == 0:
                print("No hay deportistas lesionados.")
            else:
                print("Seleccione deportista que quiera sanar.")
                opcion = input()
                for deportista in self.equipo:
                    if deportista.nombre == opcion:
                        prob_sanar = deportista.moral * (self.imp_med + self.ex_resp) / p.DIV_PROB_SANAR
                        if p.MIN_VALOR_SANAR > prob_sanar:
                            prob_sanar = p.MIN_VALOR_SANAR
                        if p.MAX_VALOR_SANAR < prob_sanar:
                            prob_sanar = p.MAX_VALOR_SANAR
                        prob_sanar = round(prob_sanar, 1)
                        sanar = random.uniform(0, 100)
                        if sanar > prob_sanar or prob_sanar == 0:
                            print("Deportista no ha podido sanarse")
                        else:
                            print("¡El deportista se ha sanado!")
                            self.dinero = self.dinero - (p.COSTO_SANAR*p.PONDERACION_PAGO_SANAR_DCC)
                            deportista.lesionado = False
    def __str__(self):
        return "DCCrotona"
