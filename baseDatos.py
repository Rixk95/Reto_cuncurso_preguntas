import sqlite3

class Base:
    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
    def identifica(self):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute("SELECT * FROM PUNTUACION")
        score=miCursor.fetchall()
        miConexion.commit()
        miConexion.close()
        if len(score)==0:
            return "VACIO"
    def evalua(self):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute("SELECT * FROM PUNTUACION")
        score=miCursor.fetchall()
        miConexion.commit()
        miConexion.close()
        if self.identifica()=="VACIO":
            self.guardarDato(self.puntaje)
        else:
            bandera=0
            for registro in score:
                if registro[0]==self.nombre:
                    bandera=1
            if bandera==0:
                self.guardarDato(self.puntaje)
            elif bandera==1:
                if self.puntaje>self.consultaVictorias():
                    self.actualizaDato(self.puntaje)             
    def guardarDato(self,puntaje):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute(f'INSERT INTO PUNTUACION VALUES("{self.nombre}",{self.puntaje})')
        miConexion.commit()
        miConexion.close()
    def actualizaDato(self,nuevoValor):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute(f'UPDATE PUNTUACION SET PUNTAJE={nuevoValor} WHERE NOMBRE="{self.nombre}"')
        miConexion.commit()
        miConexion.close()
    def consultaVictorias(self):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute(f'SELECT PUNTAJE FROM PUNTUACION WHERE NOMBRE="{self.nombre}"')
        anticipo=miCursor.fetchall()
        for victorias in anticipo:
            valorVictorias=victorias[0]
        miConexion.commit()
        miConexion.close()
        return valorVictorias
    def mostrarScore(self):
        miConexion=sqlite3.connect("baseDatos")
        miCursor=miConexion.cursor()
        miCursor.execute(f'SELECT * FROM PUNTUACION ORDER BY PUNTAJE DESC')
        tablaScore=miCursor.fetchall()
        miConexion.commit()
        miConexion.close()
        print("----------SCORE----------")
        num=1
        for x in tablaScore:
            print(f'Puesto No.{num} ... {x[0]} ... Puntaje: {x[1]}')
            num+=1