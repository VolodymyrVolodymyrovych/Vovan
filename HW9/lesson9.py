import string


def encrypt(string_):
    string_ = list(string_)
    low = list(string.ascii_lowercase)
    index = 0
    encr = []
    for i in range(0, len(string_)):
        for j in range(0, len(low)):
            if string_[i] == low[j]:
                if low[j+3] >= low[len(low)-1]:
                    encr.append(low[j+3 - len(low) - 1])
                else:
                    encr.append(low[j+3])

            else:
                j += 1
    return encr


string_ = input("Write your message: ")
print(encrypt(string_))

