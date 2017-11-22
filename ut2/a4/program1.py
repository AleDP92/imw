import sys

ident_docu = int(sys.argv[1])

rest = (ident_docu % 23)
num_ident = "TRWAGMYFPDXBNJZSQVHLCKE"
letter = num_ident[rest]
print(ident_docu, "-", letter)
