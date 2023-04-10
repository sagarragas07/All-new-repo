#project problem statements:- cows and bulls 
#firstly 3 digit number randomly selected
#we have to guess that number with limited no.of chances 
#8chances is limit, no repeat numbers, 
#cows: 162 = 921 (1:1) this is digit matching
#bulls: 623 = 921 (2:2) this is place matching#
#you should ask the name at 1st 
#hi "name","lets start"
#generate a no. randomly of 3digits(must be non-ve no.)
#after ask the user to guess the no.
#x cows, y bulls. (if 3bulls comes the ans is correct)
#tell the user that younhave k chances are left
#do you want to restart?





from random import *
def random():
    while True:
        n = str(randint(100,999))
        if not(n[0] == n[1] or n[1] == n[2] or n[0] == n[2]):
            return n

name = input("welcome to the cows and bulls game\nplease enter your name.")
print("Hi",name)
chances = 5
cows = 0
bulls = 0
num = str(random())
while chances>0:
    print("You have",chances,"chances left.")
    n = str(input("Enter your guess"))
    if num == n:
        print("Great! You got it right.")
        break
    else:
        for i in range(0,3):
            if n[i] == num[i]:
                bulls = bulls + 1
            elif n[i] in num:
                cows = cows + 1
        print("keep going. you have",bulls,"bulls and",cows,"cows.")
        bulls = 0
        cows = 0
        chances = chances - 1

print("The correct answer is",num)        



'''
print('*')
for i in range(0,5):
    print('*',end=' ')              #*****

                                    #*
print('*')                          #*
for i in range(0,5):                #*
    print('*')                      #*
                                    #*

for j in range(0,5):                 #5*
   for i in range(0,5):              #5*                    #inner loops-i colum outer loops-j rows 
     print('*',end=' ')              #5*                    #looks like square 
   print('',end='\n')                #5*
                                     #5*
print("sagar's laptop")                #sagar's laptop
print('This is sagar "note book" ')    #This is sagar "note book"

for j in range(0,5):                 #*
    for i in range(0,j+1):           #**
        print('*',end=' ')           #***
    print('',end='\n')               #*****
                                     #*****

for j in range(0,5):                 #     *
    for k in range(0,5-1-j):         #    **
        print(' ',end=' ')           #   ***
    for i in range(0,j+i):           #  ****
        print('*',end=' ')           # *****
    print('',end='\n')                                             
'''    