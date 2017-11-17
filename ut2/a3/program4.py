import sys

numero = int(sys.argv[1])

if numero <= 0:
	print('Error, número no válido... Saliendo del programa')
else:
	for i in range(1, numero + 1):
		factorial = 1
		for e in range(1, i + 1):
			factorial *= e
		print(i, "!=", factorial)
