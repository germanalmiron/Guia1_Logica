#Ejercicio 17

"""
Convertir un valor entero de horas a segundos.
"""

horas = int (input ("Ingrese el valor entero expresados en horas: "))

segundos = round ((horas * 3600 / 1), 2)

print ("El valor entero expresado en horas es: " , segundos, "segundos")
