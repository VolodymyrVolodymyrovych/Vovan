# def my_str(word):
#     rounds = []
#     q = 0
#     w = 0
#     word_l = list(word)
#     for i in word_l:
#         if i == '(' or i == ')':
#             rounds.append(i)
#         else:
#             i += i
#
#     for i in rounds:
#         if i == '(':
#             q += 1
#         if i == ')':
#             w += 1
#         else:
#             i += i
#
#     print(rounds)
#     print(q, w)
#
#     if q == w:
#         c = 0
#         v = 0
#         for i in range(0, len(rounds)):
#             if rounds[i] == '(':
#                 c += 1
#             else:
#                 v += 1
#                 if c == v:
#                     print(str(word), "-> True")
#                 else:
#                     print(str(word), "-> False")
#     else:
#         print(str(word), "-> False")
#
#
# str_word = str(input("Print the string: "))
# print(my_str(str_word))

################################################################


def my_str(word):
    rounds = []
    q = 0
    w = 0
    word_l = list(word)
    for i in word_l:
        if i == '(' or i == ')':
            rounds.append(i)
        else:
            i += i

    for i in rounds:
        if i == '(':
            q += 1
        if i == ')':
            w += 1
        else:
            i += i

    print(rounds)
    print(q, w)

    if q == w:
        c = 0
        v = 0
        for i in range(0, len(rounds)):
            if rounds[i] == '(':
                c += 1
            else:
                v += 1
                if c == v:
                    print(str(word), "-> True")
                    break
                else:
                    print(str(word), "-> False")
                    break
    else:
        print(str(word), "-> False")


str_word = str(input("Print the string: "))
print(my_str(str_word))

################################################################


