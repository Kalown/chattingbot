#Project 1 Chatting bot KALOWN
a=input("language : American , Mexican , French")

"""Greeting"""

def greet (lang):
     if lang=='Mexican':
        print('hola')
     elif lang=='French':
        print('bonjure')
     elif lang=='American':
        print('hello , how u doin buddy')
greet(a)
print("I am kalown")
print("I was created on 2021")

""" Asking about age"""

def year(age):
    if age<=16:
        print('you are a kid dumbass')
    elif age>=17:
        print('wasssup buddy')
    elif age>=27:
        print('HELLO MASTER')
    else:pass
b=int(input("what year was u born "))
print()
print("what you was born on ",b," Really")
c=2021
if b>=2021:
    print('You must be joking!')
else:
    d=c-b
    print(d)
    year(d)
print()

"""After age equation"""

age=str(d)
if age<="16":
        print('so what you watch cartoon or tv shows\n')
        e=input(">")
        if e=="cartoon":
         f=input(print("what cartoon do you watch? \n"))   #level 2

        elif e=="tv shows":
            g=input(print("what tv show you like to watch \n")) #level 2

elif age>="17":
 print('So what school u in? \n')
 school=input("")

elif age>="27":
  print("okk! so what's new going on ?")

else:pass
