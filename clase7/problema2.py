"""
	problema 2 en lenguaje Python
	autor:@ricardoifc
"""
# ingreso de datos
x = input("Ingrese X\n")
y = input("Ingrese Y\n")
z = input("Ingrese Z\n")
x = float(x) # se declaran float en x, y, z
y = float(y)
z = float(z)
m = x+(y/z)/x-(y/z) # salida en pantalla de datos
# ahora se muestra en pantalla
print("El valor de m, en base a las variables:\nx = %.1f\n\ty"
" = %.1f\n\t\tz = %.1f\nda como resultado:\n\tm = %.2f" % (x,y,z,m))

