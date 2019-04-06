def lengthCheck(password):
    if len(password) >= 8 :
        return True
    else:
        return False
def letterCheck(password):
    l = 0
    for i in password:
        if i in list("abcdefghijklmnopqrstuvwxyz"
                     "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            l += 1
    if l > 0:
        return True
    else:
        return False
def numCheck(password):
    n = 0
    for j in password:
        if j in list("0123456789"):
            n += 1
    if n > 0:
        return True
    else:
        return False
def main():
    password = input("Passwords must contain at least eight characters, "
                     "including at least 1 letter and 1 number.\n"
                     "Please enter your new password: ")
    flag = 0
    if lengthCheck(password) == True:
        flag += 1
    if letterCheck(password) == True:
        flag += 1
    if numCheck(password) == True:
        flag += 1
    if flag == 3:
        print("The password is saved.")
    else:
        return main()
main()