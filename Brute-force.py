import random
import string

jawab = 'y'
while(jawab == "y"):

    chars = "0123456789"

# chars = string.printable
    chars_list = list(chars)


    password = input("Enter a password : ")
    guess_password = ""
    hitung = 0
    while(guess_password != password):
        hitung += 1
        guess_password = random.choices(chars_list, k=len(password))
        print("Cracking password"+ str(guess_password))

        if(guess_password == list(password)):
            print("Your password is : "+ "".join(guess_password))
            break
    print("percobaan ke"+ "-"+ str(hitung))
    jawab = input("ingin memulai lagi?[y/t] : ")
