#Ejercicio 15

"""
Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos de la siguiente
manera:
a. Iván paga el 40 %
b. German paga el 33 %
c. Esteban paga el 55 % de lo que pago Iván
d. Hernán paga el resto
Determinar cuánto debe pagar cada uno.
"""

hospedaje = float (input ("Ingrese el valor total a pagar: "))

ivan = round ((hospedaje * 40 / 100), 2)
german = round ((hospedaje * 33 / 100), 2)
esteban = round ((ivan * 55 / 100), 2)
hernan = round ((hospedaje - ivan - german - esteban), 2)

print ("Ivan debe pagar: " , ivan, "pesos")
print ("German debe pagar: " , german, "pesos")
print ("Esteban debe pagar: " , esteban, "pesos")
print ("Hernan debe pagar: " , hernan, "pesos")