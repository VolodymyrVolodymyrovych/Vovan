# while True:
#     if lst[-1] > lst[-2]:
#         val.append(lst[-2])
#         break


def count(lst):
    lst = lst.split(',')
    lst = ''.join(lst)
    lst = lst.split()
    lst.sort(key=int)
    print("lst = ", lst)
    val = []
    for i in range(0, len(lst)):
        if lst[-1*(i+2)] < lst[-1*(i+1)]:
            val.append(lst[-1*(i+2)])
            break
        else:
            i += 1

    return val


lst = input("Write counts: ")

print(count(lst))

