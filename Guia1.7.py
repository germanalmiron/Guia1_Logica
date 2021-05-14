#Ejercicio 7

#Se desea calcular cuántos metros se deben recorreré para atravesar una plaza en diagonal, pero solo se
#conocen las distancia de las cuadras de ambos lados.

from math import sqrt

cuadra_A = float (input ("Ingrese el lado de la cuadra A en mts: "))

cuadra_B = float (input ("Ingrese el lado de la cuadra B en mts. "))

diagonal = sqrt (cuadra_A **2 + cuadra_B **2)

print ("Distancia para atravezar la plaza en diagonal: ", diagonal , "mts")