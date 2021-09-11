class Categoria:
    def __init__(self,NRonda):
        self.Nronda=NRonda
    def nomCategoria(self):
        categorias=["Muy facil","Facil","Promedio","Dificil","Muy dificil"]
        return categorias[self.Nronda-1]