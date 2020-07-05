"""
	problema 1 en lenguaje Python
	autor:@ricardoifc
"""
# ingreso de datos
horas = input("Por favor ingrese las horas trabajadas:\n")
costo = input("Por favor ingrese el costo oficial:\n")
resultado = int(horas) * int(costo) # se declaran enteros
descuento = float(resultado) * 0.10 # se declara float
total = resultado- float(descuento)
# salida en pantalla de datos
print("Su sueldo es: %.2f \nEl descuento es:%.2f\nTotal: %.2f"
 % (resultado,descuento,total))

