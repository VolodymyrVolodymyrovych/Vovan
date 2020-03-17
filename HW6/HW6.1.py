

def my_def(str_):
    str_new = ''
    new = ''
    str_list = str_.split()
    j = len(str_list)
    for i in range(j):
        str_new = str_list[i][0].upper()
        new = new + str_new
    return new


a = input(":")

print(my_def(a))
print(type(my_def(a)))
