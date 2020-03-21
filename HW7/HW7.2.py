
# def my_str(word):
#     rounds = []
#     q = 0
#     w = 0
#     word_l = list(word)
#
#     for i in word_l:
#         if i == '(' or i == ')':
#             rounds.append(i)
#         else:
#             i += i
#
#     for i in rounds:
#         if i == '(':
#             q += 1
#         elif i == ')':
#             w += 1
#     print(q, w)
#     if q == w:
#         print(str(word), "-> True")
#     else:
#         print(str(word), "-> False")
#
#
# str_word = str(input("Print the string: "))
# print(my_str(str_word))
################################################################


def my_str(word):
    rounds = []
    q_ro = 0
    w_ro_b = 0
    q_sque = 0
    w_sque_b = 0
    q_fig = 0
    w_fig_b = 0
    word_l = list(word)

    for i in word_l:
        if i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}':
            rounds.append(i)
        else:
            i += i

    for i in rounds:
        if i == '(':
            q_ro += 1
        elif i == ')':
            w_ro_b += 1
        elif i == '[':
            q_sque += 1
        elif i == ']':
            w_sque_b += 1
        elif i == '{':
            q_fig += 1
        elif i == '}':
            w_fig_b += 1
        else:
            i += 1

    if q_ro == w_ro_b and q_sque == w_sque_b and q_fig == w_fig_b:
        print(str(word), "-> True")
    else:
        print(str(word), "-> False")


str_word = str(input("Print the string: "))
print(my_str(str_word))

