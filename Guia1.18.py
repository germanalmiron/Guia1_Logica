#Ejercicio 18

"""
Dada las tres mediciones que realizó un pluviómetro en un día, cada vez que el mismo se vacía,
determinar cuántos milímetros llovió ese día.
"""

medicion1 = float (input ("Ingrese la medicion 1 en mm: "))
medicion2 = float (input ("Ingrese la medicion 2 en mm: "))
medicion3 = float (input ("Ingrese la medicion 3 en mm: "))

cantidad_lluvia = round ((medicion1 + medicion2 + medicion3), 2)

print ("La lluvia del día total es: " , cantidad_lluvia, "milimetros")
