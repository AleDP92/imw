import sys

numero = int(sys.argv[1])
numero2 = int(sys.argv[2])

if numero < 0:
	print('Error, números no válidos... Saliendo del programa')
elif numero < numero2:
	for i in range(numero, 0, -1):
		if numero % i == 0 and numero2 % i == 0:
			print(i)
			break
elif numero > numero2:
	numero, numero2 = numero2, numero
	for i in range(numero, 0, -1):
		if numero % i == 0 and numero2 % i == 0:
			print(i)
			break
			