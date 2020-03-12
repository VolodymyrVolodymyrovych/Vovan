import random
import string

a = random.randrange(1000,1000000,1)
a = str(a)
a_sec = a[::-1]
print('This your random value: ' +a )
print("This is the fourth character of your number: " ,a_sec[3])