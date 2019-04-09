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

count = 0
def passwordCheck(password):
    password_check = input("Enter your password: ")
    check_list = list(password_check)
    pass_list = list(password)
    global count
    if count == 2:
        print("You have entered your password incorrect three times! ")
    elif len(check_list) == len(pass_list):
        for i in range(0,len(check_list)):
            if check_list[i] == pass_list[i]:
                i += 1
                if i == len(check_list):
                    print("Password is correct! ")
            else:
                count += 1
                print("You have entered the wrong password. Please try again.")
                return passwordCheck(password)
    else:
        count += 1
        print("You have entered the wrong password. Please try again.")
        return passwordCheck(password)

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
        passwordCheck(password)
    else:
        return main()
main()