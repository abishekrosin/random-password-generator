import random
print("welcome to random password generattor")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&"
nbrofpwds = int(input("enter the no of password to be generated:")
                pwdlen = int(input("please enter the lenght of the password needed:"))
print("here are your random passwords:")
for x in range (nbrofpwds):
    pwd=""
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)
                    