a = int(input("Значение а: "))
b = int(input("Значение b: "))
while True:
	if a == b:
		print(a)
		break
	elif a >b:
		a = a-b
	else:
		b = b-a
