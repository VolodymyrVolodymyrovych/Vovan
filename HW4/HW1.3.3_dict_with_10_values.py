import string
import random


Users_all = {
    'admin':['qwert', random.randrange(10000000000,100000000000000000,1)],
    'vova':['avov', random.randrange(10000000000,100000000000000000,1)],
    'katya':['2345', random.randrange(10000000000,100000000000000000,1)],
    'root':['toor', random.randrange(10000000000,100000000000000000,1)],
    'alex':['xela', random.randrange(10000000000,100000000000000000,1)],
    'oleg':['gelo', random.randrange(10000000000,100000000000000000,1)],
    'tom':['mot', random.randrange(10000000000,100000000000000000,1)],
    'jerry':['mouse', random.randrange(10000000000,100000000000000000,1)],
    'dog':['notCat', random.randrange(10000000000,100000000000000000,1)],
    'alisa':['wonderworld', random.randrange(10000000000,100000000000000000,1)],
}

CHECK_LOGIN = str(input("login:"))
if CHECK_LOGIN in Users_all:
    CHECK_PASS = str(input(CHECK_LOGIN+"'s pass:"))
    if CHECK_PASS in Users_all.get(CHECK_LOGIN,CHECK_PASS):
        SECRET = Users_all[CHECK_LOGIN]
        print("Your login and pass is true!. Your secret it's:", SECRET[1])

else:
    print("new pass for",CHECK_LOGIN,"'s:")
    NEW_USER_PASS=input()
    Users_all.update({CHECK_LOGIN:[NEW_USER_PASS, random.randrange(10000000000,100000000000000000,1)]})
    SECRET = Users_all[CHECK_LOGIN]
    print("New user '",CHECK_LOGIN,"', pass '",NEW_USER_PASS,"' and secret '",SECRET[-1],"'")
    print(Users_all)