#Ejercicio 12

"""

Una empresa distribuidora de energía le cobra a sus abonados el consumo de kW por hora, pero además
debe sumarle el 0,21 % de impuesto, pero actualmente todos los cliente están dentro de un plan de
promoción que les descuenta el 3,7 % del monto total apagar.
"""

kw = float (input ("Ingrese la cantidad de kw: "))

hora = float (input ("Ingrese la cantidad de horas: "))

consumo = kw * hora

impuesto = (0.21 / 100) * consumo

descuento = round (3.7 / 100) * (consumo + impuesto)

total_consumo = consumo + impuesto - descuento

print ("El importe a cobrar al cliente es de: " , total_consumo, "pesos")









