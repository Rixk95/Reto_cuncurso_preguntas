from pregunta import Pregunta

class Evaluador(Pregunta):
    def __init__(self,seccion,numAleatorio,eleccion):
        super().__init__(seccion,numAleatorio)
        self.eleccion=eleccion
    def evaluar(self):
        a=["A","C","C","D","B"]
        b=["C","A","B","B","C"]
        c=["B","B","C","B","D"]
        d=["B","C","D","C","D"]
        e=["B","A","B","A","A"]
        if self.seccion=="Muy facil":
            if a[self.numAleatorio]==self.eleccion:
                return 1
            else:
                return 0
        elif self.seccion=="Facil":
            if b[self.numAleatorio]==self.eleccion:
                return 1
            else:
                return 0
        elif self.seccion=="Promedio":
            if c[self.numAleatorio]==self.eleccion:
                return 1
            else:
                return 0
        elif self.seccion=="Dificil":
            if d[self.numAleatorio]==self.eleccion:
                return 1
            else:
                return 0
        elif self.seccion=="Muy dificil":
            if e[self.numAleatorio]==self.eleccion:
                return 1
            else:
                return 0