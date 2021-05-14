#Ejercicio 16

"""
Calcular el promedio de temperatura y presión recolectado por una estación meteorológica en una
semana, considerando que realiza solo una medición al día.
"""

from statistics import mean

temperatura1 = float (input ("Ingrese la temperatura dia 1: "))
temperatura2 = float (input ("Ingrese la temperatura dia 2: "))
temperatura3 = float (input ("Ingrese la temperatura dia 3: "))
temperatura4 = float (input ("Ingrese la temperatura dia 4: "))
temperatura5 = float (input ("Ingrese la temperatura dia 5: "))
temperatura6 = float (input ("Ingrese la temperatura dia 6: "))
temperatura7 = float (input ("Ingrese la temperatura dia 7: "))

presion1 = float (input ("Ingrese la presion dia 1: "))
presion2 = float (input ("Ingrese la presion dia 2: "))
presion3 = float (input ("Ingrese la presion dia 3: "))
presion4 = float (input ("Ingrese la presion dia 4: "))
presion5 = float (input ("Ingrese la presion dia 5: "))
presion6 = float (input ("Ingrese la presion dia 6: "))
presion7 = float (input ("Ingrese la presion dia 7: "))

promedio_temp = round (mean ([temperatura1, temperatura2, temperatura3, temperatura4, temperatura5, 
temperatura6, temperatura7]), 2)

promedio_presion = round (mean ([presion1, presion2, presion3, presion4, presion5, presion6, presion7]), 2)

print ("Promedio semanal de la temperatura: " , promedio_temp, "°C")
print ("Promedio semanal de la presion." , promedio_presion, "PA" )
