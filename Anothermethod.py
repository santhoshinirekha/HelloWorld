a = int(input('first number? '))
b = int(input('second number? '))
c = int(input('third number? '))
d = int(input('fourth number? '))
print(type(a))
e = str(a + b + c + d)
print(e)
f = str(e[0:1])
print(f)
g = str(e[1:])
print(g)
h = int(f)
i = int(g)
j = print(h+i)




a = input('first numbers? ') + input('second number? ') + input('third number? ') + input('fourth number? ')
print(type(a))
b = str((a[0:1]) + (a[1]) + (a[2]) + (a[3]))
print(type(b))
print(b)
c = int(b[0:1]) + int(b[1]) + int(b[2]) + int(b[3])
print(c)
print(type(c))