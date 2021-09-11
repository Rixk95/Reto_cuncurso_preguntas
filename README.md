# Reto_cuncurso_preguntas
Prueba técnica para la convocatoria de desarrollador.
Mi nombre es Jorge Español y acontunuacion explicare de forma breve su funcionamiento y modo de uso.
Tiene un proceso muy intuitivo en su funcionamiento por lo que no entrare a explicar a fondo.
Se desarrollo en lenguaje python y la clase principal que actua como ejecutable se llama "jugador.py".
Se cumple con todos los items de criterio para la calificacion, como lo es el manejo de POO,
la creacion de entidades solicitadas de manera especifica, se mantiene una estructura y sintaxis
coherente durante todo el proyecto, se realiza una persistencia de los resultados utilizando una base
de datos implementada en python con "sqlite3"(Se evidencian dos registros en el "SCORE" los cuales
fueron hechos durante la implementacion con el fin de realizar pruebas). Tambien cabe destacar que se
integraron mas clases necesarias como lo fueron "evaluador.py" y "baseDatos.py". Durante la ejecucion 
del codigo se evidenciaran instrucciones claras para el correcto uso del juego.

Para finalizar dare una descripcion de lo que hace cada clase,  de igual forma nombrare todos los archivos
que tiene el proyecto:

-"README.md": Instructivo que debe ser leido antes de ejecutarse el codigo.
-"baseDatos": Base de datos donde contiene la informacion del "SCORE" para uso de "baseDatos.py".
-"baseDatos.py": Archivo python que contiene los metodos necesarios para el sumistro de informacion guardada en la base de datos.
-"categoria.py": Archivo python que indica la dificultad de las preguntas.
-"evaluador.py": Archivo python que evalua si la opcion seleccionada por el usuario es la correcta o no.
-"jugador.py": Archivo python que actua como clase principal, contiene el nombre del jugador y es el que relaciona todas las clases.
-"opciones.py": Archivo python que contiene las opciones de respuesta en relacion con la pregunta sumistrada en el archivo "pregunta.py".
-"pregunta.py": Archivo python que suministra una pregunta aleatoria deacuerdo a la categoria en la que se encuentre el jugador.
-"premio.py": Archivo python que valora el puntaje recibido por una respuesta correcta, teniendo en cuenta su categoria.
-"ronda.py": Archivo python que indica en cual de las cinco rondas se encuentra el jugador.