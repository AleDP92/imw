from math import pi

import sys

radio = float(sys.argv[1])

if radio >= 0:
	print('(1)Cálculo del diámetro de la circunferencia')
	print('(2)Cálculo del perímetro de la circunferencia')
	print('(3)Cálculo del área del círculo')
	print('(4)Salir del programa')

option = int(input('¿Qué operación quiere realizar? '))
if option >= 1 and option <= 4:
	if option == 1:
		print('Diámetro: ', 2 * radio)
	if option == 2:
		print('Perímetro: ', 2 * pi * radio)
	if option == 3:
		print('Área: ', pi * radio ** 2)
	if option == 4:
		sys.exit()

else:
	print('Error, opción no válida')

