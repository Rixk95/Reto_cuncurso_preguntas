class Premio:
    def __init__(self,seccion,puntuacion):
        self.seccion=seccion
        self.puntuacion=puntuacion
    def valorar(self):
        if self.seccion=="Muy facil":
            return self.puntuacion+100
        elif self.seccion=="Facil":
            return self.puntuacion+200
        elif self.seccion=="Promedio":
            return self.puntuacion+300
        elif self.seccion=="Dificil":
            return self.puntuacion+400
        elif self.seccion=="Muy dificil":
            return self.puntuacion+500            