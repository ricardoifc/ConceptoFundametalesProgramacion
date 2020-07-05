"""
	Ejemplo 3 de lenguaje Python
	autor:@ricardoifc
"""

valor1 = input("Porfavor ingrese valor 1:\n")
valor2 = input("Porfavor ingrese valor 2:\n")


print ("variable argv[1]:	%s" % valor1)
print ("variable argv[2]:	%s" % valor2)

suma = int(valor1) +int (valor2) # aqui realizo la suma
resta = int(valor1) - int (valor2) # aqui realizo la resta
multiplicacion = int(valor1) * int (valor2) # aqui realizo la multiplicacion

print("La suma es :%d\tLa resta es :%d\tLa multiplicacion es :%d\t" % (suma,resta,multiplicacion))
 
 