from ronda import Ronda
from categoria import Categoria
import random
from pregunta import Pregunta
from opciones import Opciones
from evaluador import Evaluador
from premio import Premio
from baseDatos import Base

print('''
Bienvenido al juego "Pon a prueba tus matematicas de sexto grado"
Juego dirigido a niños entre la edad de 11 y 13. 
Consta de 5 rondas con niveles de dificultades ascendentes,
las preguntas pueden variar y son de opcion multiple 
con unica respuesta, tambien contiene una
opcion adicional de rendirse.
Si al finalizar el juego sacas un puntaje inferior al que ya tenias,
el "SCORE" no se actualizara ya que el "SCORE" guarda tu mejor puntaje.
Al finalizar se te mostrara el "SCORE" donde podras ver tu
mejor puntuacion y compararla con otros competidores.
Buena suerte!! 

''')
nombre=input("Ingresa tu nombre:\n").upper()
for cont in range(5):
    ronda=Ronda(cont+1)
    NRonda=ronda.n_ronda()
    print("--"*20)
    print("Ronda numero: "+str(NRonda))
    categoria=Categoria(NRonda)
    seccion=categoria.nomCategoria()
    print("Nivel de dificultad: "+seccion)
    if NRonda==1:
        nuevoPuntaje=0
    puntuacion=0+nuevoPuntaje
    print("Puntaje actual: "+str(puntuacion))
    premio=Premio(seccion,puntuacion)
    numAleatorio=random.randint(0,4)
    pregunta=Pregunta(seccion,numAleatorio)
    cuestion=pregunta.preguntaAleatoria()
    print("Pregunta:   "+cuestion)
    opciones=Opciones(seccion,numAleatorio)
    posibilidades=opciones.opcionesPregunta()
    print(posibilidades)
    eleccion=input("Elige la opcion correcta:\n").upper()
    evaluador=Evaluador(seccion,numAleatorio,eleccion)
    resultado=evaluador.evaluar()
    if resultado==1:
        nuevoPuntaje=premio.valorar()
    else:
        print("\nFIN DEL JUEGO\nTU PUNTAJE ES DE "+str(puntuacion)+" Y SERA GUARDADA EN EL SCORE.\n")
        base=Base(nombre,puntuacion)
        base.evalua()
        base.mostrarScore()
        exit(0)
puntuacion=1500
print("FELICITACIONES, SUPERASTE TODAS LAS RONDAS.\nTU PUNTAJE ES DE "+str(puntuacion)+" Y QUEDARA GUARDADO EN EL SCORE.\nGRACIAS POR JUGAR.\n")
base=Base(nombre,puntuacion)
base.evalua()
base.mostrarScore()