import string


def encrypt(string_, key):
    string_ = list(string_)
    low = list(string.ascii_lowercase)
    index = 0
    encr = []
    for i in range(0, len(string_)):
        if string_[i] == ' ':
            encr.append(' ')
        elif string_[i] == '.':
            encr.append('.')
        for j in range(0, len(low)):
            if string_[i] == low[j]:
                if low[j - key] <= low[len(low) - 1]:
                    encr.append(low[j + key - len(low)])
                else:
                    encr.append(low[j + key])

            else:
                j += 1
    encr = ''.join(encr)
    return encr


def decrypt(encrypted_str, key):
    encrypted_str = list(encrypted_str)
    low = list(string.ascii_lowercase)
    decr = []

    for i in range(len(encrypted_str)):
        if encrypted_str[i] == ' ':
            decr.append(' ')
        elif encrypted_str[i] == '.':
            decr.append('.')
        for j in range(len(low)):
            if encrypted_str[i] == low[j]:
                if low[j - key] >= low[len(low)-1]:
                    decr.append(low[j - key + len(low)])
                else:
                    decr.append(low[j - key])
            else:
                j += 1
    decr = ''.join(decr)
    return decr

