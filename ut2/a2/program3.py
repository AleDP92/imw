import sys

nota = float(sys.argv[1])

if nota >= 0 and nota <= 10:
    if nota < 5:
        print('Suspenso')
    if 5 <= nota < 7:
        print('Aprobado')
    if 7 <= nota < 9:
        print('Notable')
    if 9 <= nota < 10:
        print('Sobresaliente')
    if nota == 10:
        print('Matrícula de honor')
else:
    print('Error, número no válido')
