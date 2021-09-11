class Pregunta:
    def __init__(self,seccion,numAleatorio):
        self.seccion=seccion
        self.numAleatorio=numAleatorio
    def preguntaAleatoria(self):
        a=["¿13+24?","¿14+52?","¿38+42?","¿63+96?","¿24+87?"]
        b=["¿76-15?","¿23-12?","¿15-3?","¿28-27?","¿29-19?"]
        c=["¿12x8?","¿8x9?","¿3x27?","¿12x11?","¿24x10?"]
        d=["¿9/3?","¿81/3?","¿24/2?","¿100/10?","¿40/5?"]
        e=["¿raiz cuadrada de 81?","¿raiz cuadrada de 64?","¿raiz cuadrada de 49?","¿raiz cubica de 125?","¿raiz cubica de 512?"]
        if self.seccion=="Muy facil":
            return a[self.numAleatorio]
        elif self.seccion=="Facil":
            return b[self.numAleatorio]
        elif self.seccion=="Promedio":
            return c[self.numAleatorio]
        elif self.seccion=="Dificil":
            return d[self.numAleatorio]
        elif self.seccion=="Muy dificil":
            return e[self.numAleatorio]