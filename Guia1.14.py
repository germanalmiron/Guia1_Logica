#Ejercicio 14

"""
Un profesor desea calcular el promedio de un alumno a lo largo de los cuatro parciales que rindió.
"""

primer_parcial = float (input ("Ingrese la nota del 1° parcial: "))
segundo_parcial = float (input ("Ingrese la nota del 2° parcial: "))
tercer_parcial = float (input ("Ingrese la nota del 3° parcial: "))
cuarto_parcial = float (input ("Ingrese la nota del 4° parcial: "))

promedio = round (((primer_parcial + segundo_parcial + tercer_parcial + cuarto_parcial) / 4), 2)

print ("El pomedio del alumno es: " , promedio)