#Ejercicio 11

"""
Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente, para esto les cobra por
tiempo de llamada (por minuto) pero además le adiciona un 0,5 % del monto total de la llamada.

"""

tiempo_llamada = float (input ("Ingrese cantidad de minutos de la llamada: "))

valor_minuto = float (input ("Ingrese el valor del minuto: "))

costo = tiempo_llamada * valor_minuto

adicional = costo * 0.005

print ("El costo total de la llamada a facturar es de: " , costo + adicional, "$")
