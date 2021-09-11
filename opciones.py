from pregunta import Pregunta

class Opciones(Pregunta):
    def __init__(self,seccion,numAleatorio):
        super().__init__(seccion,numAleatorio)
       
        
    def opcionesPregunta(self):
        a=["A. 37\nB. 27\nC. 29\nD. 39\nE. Rendirse",
        "A. 65\nB. 68\nC. 66\nD. 56\nE. Rendirse",
        "A. 70\nB. 78\nC. 80\nD. 88\nE. Rendirse",
        "A. 149\nB. 127\nC. 137\nD. 159\nE. Rendirse",
        "A. 101\nB. 111\nC. 222\nD. 202\nE. Rendirse"]
        b=["A. 51\nB. 71\nC. 61\nD. 52\nE. Rendirse",
        "A. 11\nB. 21\nC. 31\nD. 22\nE. Rendirse",
        "A. 22\nB. 12\nC. 32\nD. 11\nE. Rendirse",
        "A. 11\nB. 1\nC. 22\nD. 2\nE. Rendirse",
        "A. 20\nB. 21\nC. 10\nD. 11\nE. Rendirse"]
        c=["A. 95\nB. 96\nC. 85\nD. 86\nE. Rendirse",
        "A. 71\nB. 72\nC. 81\nD. 82\nE. Rendirse",
        "A. 61\nB. 62\nC. 81\nD. 82\nE. Rendirse",
        "A. 131\nB. 132\nC. 141\nD. 142\nE. Rendirse",
        "A. 246\nB. 248\nC. 242\nD. 240\nE. Rendirse"]
        d=["A. 1\nB. 3\nC. 6\nD. 9\nE. Rendirse",
        "A. 3\nB. 9\nC. 27\nD. 81\nE. Rendirse",
        "A. 2\nB. 4\nC. 8\nD. 12\nE. Rendirse",
        "A. 1\nB. 5\nC. 10\nD. 15\nE. Rendirse",
        "A. 5\nB. 6\nC. 7\nD. 8\nE. Rendirse"]
        e=["A. 8\nB. 9\nC. 18\nD. 19\nE. Rendirse",
        "A. 8\nB. 9\nC. 18\nD. 19\nE. Rendirse",
        "A. 6\nB. 7\nC. 8\nD. 9\nE. Rendirse",
        "A. 5\nB. 6\nC. 15\nD. 16\nE. Rendirse",
        "A. 8\nB. 9\nC. 18\nD. 19\nE. Rendirse"]
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