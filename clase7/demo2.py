"""
	Ejemplo 2 de lenguaje Python
	autor:@ricardoifc
"""

import sys

nombre_archivo = sys.argv [0]
valor1 = sys.argv [1]
valor2 = sys.argv [2]
print ("variable argv[0]:	%s" % nombre_archivo)
print ("variable argv[1]:	%s" % valor1)
print ("variable argv[2]:	%s" % valor2)
suma = int(valor1) +int (valor2) # aqui realizo la suma
print("La suma es :%d" % suma)

