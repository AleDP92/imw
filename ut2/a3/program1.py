import sys

numero = int(sys.argv[1])

if numero <= 0:
	print('Error, número no válido... Saliendo del programa')
else:
	for i in range(2, numero):
		if numero % i == 0:
			print('El número no es primo')
			break
	else:
		print('Es número primo')