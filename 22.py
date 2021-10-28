a = int(input("Значение a: "))
b = int(input("Значение b: "))
c = int(input("Значение с: "))
x = int(input("Значение x: "))
y = int(input("Значение y: "))
if a>b:
	r =a;a=b;b=r 
if b>c:
	r=b;b=c;c=r
if a>b:
	r=a;a=b;b=r
if x>y:
	r=x;x=y;y=r 
if a<x and b<y:
	print("Пройдёт")
else:
	print("Не пройдёт")
