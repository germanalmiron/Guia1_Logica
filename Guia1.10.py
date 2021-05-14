#Ejercicio 10

"""

Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo que esta se
mueve a una velocidad constante y se conocen la cantidad de kilómetros del camino.

"""

velocidad = int (input ("Ingresen la velocidad del recorrido en bicicleta en Km/h: "))

km = int (input ("Ingrese la cantidad de KM recorridos: "))

tiempo = velocidad / km * 60

print ("El tiempo del recorrido es: " , tiempo, "minutos")

