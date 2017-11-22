import sys

number = sys.argv[1:]
plus = 0
nc = len(number)

for i in number:
	i = float(i)
	plus += i  
result = plus / nc
print(f"La media de lo valores es: {result}")


