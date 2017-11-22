import sys

number = int(sys.argv[1])
phrase = sys.argv[2]
count = 0

words = phrase.split(" ")
for i in words:
	if len(i) == number:
		count += 1
print("hay", count, "palabras de", number, "letras")

