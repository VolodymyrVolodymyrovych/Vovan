import math

a = int(input("Write new count: "))
b = int(input("write new count2: "))
c = str(input("write operation(/,*,+,-,**,sqrt)"))

if c == '+':
    print(a+b)
if c == '-':
    print(a-b)
if c == '*':
    print(a*b)
if c == '/':
    print(a/b)
if c == '**':
    print("a**b = ",a**b)
if c =='sqrt':
    print("sqrt(a) = ",math.sqrt(a), "sqrt(b) = ", math.sqrt(b) )

if c != '+' and c != '-' and c != '*' and c != '/' and c != '**' and c != 'sqrt':
    print("bad operation!!!")