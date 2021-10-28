a = int(input("Введите a :"))
b = int(input("Введите b :"))
if a==0:
	if b ==0:
		print("X любое")
	else:
		print("Нет решений")
else:
	c = b/a 
	if a>0:
		print("x > c")
	else:
		print("x < c")
			
