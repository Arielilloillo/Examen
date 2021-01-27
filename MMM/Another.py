fibonacci=[]
x=0
y=1
numbers= int(input("How many numbers do you want?: "))
#Supuesto intento de rango
#exeption_1=int(input("Write the first range of number you don't want: "))
#exeption_2=int(input("Write the last range of number you don't want: "))
#ex=range[exeption_1:exeption_2]
for n in range(numbers):
    fibonacci.append(x+y)
    z = x + y
    x = y
    y = z
print(fibonacci)