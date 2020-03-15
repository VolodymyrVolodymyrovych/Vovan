# 0 4 8 2 6 0

Check_leap = 0

while Check_leap != ValueError:
    try:
        Check_leap = int(input("Write year: "))
        break
    except ValueError:
        print("Isn't integer. Please write integer")

#if Check_leap % 4 == 0:
if (Check_leap % 4 == 0 and Check_leap % 100 != 0) or (Check_leap % 100 == 0 and Check_leap % 400 == 0):
    print(Check_leap, "'s - this is the leap year!")
else:
    print(Check_leap, "'s - is not leap year!!!")

