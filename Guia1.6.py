#Ejercicio 6

"""
Una pinturería debe elaborar el presupuesto para un cliente 
y necesita calcular el costo total, este se deriva de la cantidad de pintura requerida 
y de la mano de obra, teniendo encuenta lo siguiente: 
se requiere un litro de pintura por m2 y el costo de 
mano de obraes del 45 % del precio total de pintura. 

"""


superficie = float (input ("Ingrese la cantidad de m2 a pintar:" ))

precio_pintura = float (input ("Ingrese el precio del litro de pintura:" ))

pintura = superficie * precio_pintura

mano_obra = pintura * 0.45

print ("El presupuesto total es: " , pintura + mano_obra, "pesos")