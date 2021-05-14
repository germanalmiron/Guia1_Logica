#Ejercicio 9

"""

Una empresa de transportes les cobra a sus pasajeros por kilómetros recorridos, 
y necesita poder calcular el monto a cobrar a un cliente cuando se baja. 

"""

km_recorridos = float (input ("Ingrese la cantidad de Km recorridos del pasajero:"))

valor_km = float (input ("Ingrese el valor del Km: "))

total_cobrar = km_recorridos * valor_km

print ("Valor a cobrar al pasajero por Km recorrido: " , total_cobrar, "$")
