def menu():
	phone_book = {}
	choose = 0
	while choose != 4:
		print("(1)Lista de contactos")
		print("(2)Añadir contacto")
		print("(3)Borrar contacto")
		print("(4)Salir")
		choose = int(input('¿Qué operación quiere realizar? '))
		if choose == 1:
			show_contacts(phone_book)
		if choose == 2:
			name = input("Inserta tu nombre ")
			phone = input("Inserta tu número de teléfono ")
			add_contact(phone_book, name, phone)
		if choose == 3:
			name = input("inserta el nombre ")
			remove_contact(phone_book, name)
		if choose == 4:
			break


def add_contact(phone_book, name, phone):
	if name in phone_book:
		print("el nombre ya existe")
	else:
		phone_book[name] = phone


def remove_contact(phone_book, name):
	if name in phone_book:
		del (phone_book[name])


def show_contacts(phone_book):
	for name, phone in phone_book.items():
		print(name, phone)

menu()
