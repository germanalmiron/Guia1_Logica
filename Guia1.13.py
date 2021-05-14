#Ejercicio 13

"""
Un supermercado está estableciendo el precio de venta para nuevos productos, de estos productos desean
generar el 27 % de ganancia.

"""

precio_producto = float (input("Ingrese el precio del producto: "))

ganancia = precio_producto * 27 / 100

nuevo_producto = precio_producto + ganancia

print ("El nuevo precio del producto es de: " , nuevo_producto, "pesos")
