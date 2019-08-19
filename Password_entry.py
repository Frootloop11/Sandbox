""""well hello there obi wan kenobi, we meet at last. i am the great Thomas Bennett"""
password = input("enter a password:")

while len(password) < 10:
    print("password is not long enough")
    password = input("re-enter a password:")

for i in range(len(password)):
    print('*', end='')

