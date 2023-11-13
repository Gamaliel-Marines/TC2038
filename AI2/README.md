## Alta demanda para los Proveedores de Servicios de Internet (ISP) 

Durante el año 2020 todo el mundo se vio afectado por un evento que nadie esperaba: la pandemia ocasionada por el COVID-19. En todos los países del planeta se tomaron medidas sanitarias para intentar contener la pandemia. Una de estas medidas fue el mandar a toda la población a sus casas, moviendo gran parte de las actividdaes presenciales a un modelo remoto en el que las empresas proveedoras de servicios de Intenet (ISP por sus siglas en inglés de Intenet Service Provider) tomaron un papel más que protagónico. Mucha gente se movió a la modalidad de trabajo remoto, o home-office, también la mayoría de instituciones educativas optaron por continuar sus operaciones bajo un modelo a distancia aumentando de gran forma la transmisión de datos en Internet.

Si estuviera en nuestras manos mejorar los servicios de Internet en una población pequeña,
¿Podríamos decidir como cablear los puntos más importantes de dicha población de tal forma que se utilice la menor cantidad de fibra óptica?

Asumiendo que tenemos varias formas de conectar dos nodos en la población,

Para una persona que tiene que ir a visitar todos los puntos de la red, ¿Cuál será la forma óptima de visitar todos los puntos de la red y regresar al punto de origen?

¿Podríamos analizar la cantidad máxima de información que puede pasar desde un nodo a otro ?

¿Podríamos analizar la factibilidad de conectar a la red un nuevo punto (una nueva localidad) en el mapa ?

# Instrucciones

En equipos de máximo 3 personas, escribe un programa en C++ que ayude a una empresa que quiere incursionar en los servicios de Internet respondiendo a la Situación Problema 2.

### El programa debe:

1. Leer un archivo de entrada que contiene la información de un grafo representado en forma de una matriz de adyacencias con grafos ponderados.
    - El peso de cada arista es la distancia en kilómetros entre colonia y colonia, por donde es factible meter cableado.
    - El programa debe desplegar cuál es la forma óptima de cablear con fibra óptica conectando colonias de tal forma que se pueda compartir información entre cualesquiera dos colonias.
2. Debido a que las ciudades apenas están entrando al mundo tecnológico, se requiere que alguien visite cada colonia para ir a dejar estados de cuenta físicos, publicidad, avisos y notificaciones impresos. por eso se quiere saber ¿cuál es la ruta más corta posible que visita cada colonia exactamente una vez y al finalizar regresa a la colonia origen?
    - El programa debe desplegar la ruta a considerar, tomando en cuenta que la primera ciudad se le llamará A, a la segunda B, y así sucesivamente.
3. El programa también debe leer otra matriz cuadrada de N x N datos que representen la capacidad máxima de transmisión de datos entre la colonia i y la colonia j. Como estamos trabajando con ciudades con una gran cantidad de campos electromagnéticos, que pueden generar interferencia, ya se hicieron estimaciones que están reflejadas en esta matriz.
- La empresa quiere conocer el flujo máximo de información del nodo inicial al nodo final. Esto debe desplegarse también en la salida estándar.
Por último, investiga un algoritmo que te permite realizar lo siguiente:

4. Teniendo en cuenta la ubicación geográfica de varias "centrales" a las que se pueden conectar nuevas casas, la empresa quiere contar con una forma de decidir, dada una nueva contratación del servicio, cuál es la central más cercana geográficamente a esa nueva contratación. No necesariamente hay una central por cada colonia. Se pueden tener colonias sin central, y colonias con más de una central.

Entrada:

Un número entero N que representa el número de colonias en la ciudad.
matriz cuadrada de N x N que representa el grafo con las distancias en kilómetros entre las colonias de la ciudad.
matriz cuadrada de N x N que representa las capacidades máximas de flujo de datos entre colonia i y colonia j.
lista de N pares ordenados de la forma (x,y) que representan la ubicación en un plano coordenado de las centrales, junto con la ubicación de la nueva central.
Salida:
1. Forma de cablear las colonias con fibra (lista de arcos de la forma (A,B)).
2. ruta a seguir por el personal que reparte correspondencia, considerando inicio y fin en al misma colonia.
3. valor de flujo máximo de información del nodo inicial al nodo final.
4. la salida será la distancia más corta entre dos puntos: el de la ubicación de la nueva central con respecto al más cercano.



Ejemplo de entrada:
4                      // Un número entero N que representa el número de colonias en la ciudad.

 0 16 45 32    // grafo con las distancias en kms entre las colonias de la ciudad
16  0 18 21
45 18  0  7
32 21  7  0

 0 48  12  18   // capacidades máximas de flujo de datos entre colonia i y colonia j
52  0 42 32
18 46  0 56
24 36 52  0

(200,500)       // pares ordenados que representan la ubicación en un plano de las centrales
(300,100)
(450,150)
(520,480)

(325,200)       // par ordenado que representa la ubicación en un plano de la nueva central