import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
a = 0
g = 0
c = 0
t = 0
for char in range(0, DNA_SIZE):
    if sequence[char] == "A":
		a += 1
	if sequence[char] == "G":
		g += 1
	if sequence[char] == "C":
		c += 1
	if sequence[char] == "T":
		t += 1
print("Adenine:", a)
print("Thymine:", t)
print("Cytosine:", c) 
print("Guanine:", g)

