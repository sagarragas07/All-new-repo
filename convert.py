"""
import csv
import json
data = open("C:\\Users\\SMUTHYALA\\Desktop\\nextcsv.csv").readlines()
print(json.dumps(list(csv.reader(data))))                                        #more nextcsv.csv     #this will show the data in csv formate data

#this will aviod the duplicate values
num = [1,2,3,4,5,5,6,4]
unique = []

for i in num:
    if i in unique:
        continue
    else:
        unique.append(i)
print(unique)                              #[1,2,3,4,5,6]

#this will aviod the duplicate values
a = set(num)                               #{1,2,3,4,5,6}
a = list(a)                             
print(a)                                   ##[1,2,3,4,5,6]           

#this will avoid the duplicate values
a = 'apple'
b = ''
for i in a:
    if i in b:
        continue
    else:
        b += i
print(b)                     #aple

#converting int str
a = 123
print(type(a))                     #int
b = str(a)
print(type(b))                     #str



#printing by iter method           #this will print only the print given word in str
a = "apple"
b = iter(a)
print(next(b))           #a
print(next(b))           #p
print(next(b))           #p
print(next(b))           #l
print(next(b))           #e

#print revers order
txt = "Hello World"[::-1]
print(txt)                           #dlroW olleH

#finding the largest number from given list
list =  [6,5,1,2,3,4,8,9]
list.sort()
print ("first largest element is:", list[-1])         #9

                          #or

#ex:program in loops    #finding the max value in the given list
avg_marks = [45,76,85,87,98,87,67,90,89,78,85]

max_value = -1
n =len(avg_marks)

for i in range(0,n):
     if avg_marks[i]>max_value:
         max_value= avg_marks[i]   
                                           #98 will be printed
print('Max value : ',max_value)
                        #or

#finding largest noin list:
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)                          #10


#printing unique values (by list comperhension)
list =  [6,5,1,2,3,4,9,6,5,1]
unique = []

for i in list:
	if i in unique:
		continue
	else:
		unique.append(i)
print(unique)                             #(6,5,1,2,3,4,9)

a = 1
s = 1
if a == 1:
    print(s)
else: 
    print(y)                                  #1

#converting int to string
a = 1
print(a)
b = str(a)
print(type(b))                            #str


#printing by iter method
a = "apple"
b = iter(a)
print(next(b))           #a
print(next(b))           #p
print(next(b))           #p
print(next(b))           #l
print(next(b))           #e

#print revers order
txt = "Hello World"[::-1]
print(txt)                           #dlroW olleH


#finding the duplicate values in list
a = [1,2,3,4,5,6,3,4]
duplicates = []
for i in a:
    if a.count(i) > 1 and i not in duplicates:
         duplicates.append(i)
print(duplicates)                                    #[3, 4]

#printing str to list
a = "a,b,c,d"
print([a])                                               #['a,b,c,d']

#printing 3rd index value
a = [1,2,3,4,5,6,3,4]
print(a[3])                                            #4

#converting int to str 
a = 23232
b = str(a)
print(type(b))                                          #str

#printing the next list1
list = [1,2,3,4,5,6]
list1 = [1,5,9,6]
list2 = [1,2+3,4+5,6]
print(list2)                               #[1, 5, 9, 6]

#printing the odd numbers
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 != 0:
       print(num, end=" ")                #21 45 93


#List comprehension:-it is a type of method of creation of list (shortly)
#before this list comperhension we done by like this:
#l = [1,2,3,4,5,6]
#new_list = []
#for i in range(0,len(l)):
#   new_list.append(l[i]*5)
#print(new_list)                                                             #[5, 10, 15, 20, 25, 30]
#
#after coming list comperhension we done by like this: this method using with for loop
#l = [1,2,3,4,5,6]
#new_list = [x*5 for x in l]
#print(new_list)                                                             #[5,10,15,20,25,30] came sm output but the list of code is less compared to previous method
#
#list comprehenstion and for loop and if condition:
#even_list = [x for x in range(20) if x%2==0]
#odd_list = [x for x in range(20) if x%2==1]
#print(even_list)                                          #[0,2,4,6,8,10,12,14,16,18] this code will print 1 to 20 even nmbrs by using if condition
#print(odd_list)                                           #[1,3,5,7,9,11,13,15,17,19] this code will print 1 to 20 odd nmbrs by using if condition       

class Amazon:      #(not printed code)(static method)
#      #class variables                              class method:-(is common for the data that working on functions)
       overall_discount = 5
#-------space
def __init__(self,p_id,p_name,p_price,p_discount):         #constructor             #self will be call by using objecct name
       self.id = p_id
       self.name = p_name                                      #variables
       self.price = p_price
       self.discount = p_discount
def get_final_price(self):                     #function
       return self.price - self.price*self.discount/100 - amazon.overall_discount*self.price/100
#--------space
def print_data(self):
     print('--------------')
     print('id : ',self.id)
     print('name : ',self.name)
     print('final price : ',self.get_finnal_price())           #---------------------
#-------------space                                              #id :   1
p1 = Amazon(1,'product1',500,8)                                 #name :  product
p2 = Amazon(2,'product2',800,11)                                #final price  : 436.0
#------space                                                      ----------------
p1.print_data()                                                #id  : 2
p2.print_data()                                                #name : product2
#(not printed amazon code)                                      #final price  : 672.0

#1)frontlinesmedia by 
x =(1,2,3)
y = []
for i in enumerate(x):
    y.append(i)
print(y)
z = [a+b for a,b in y]
print(z)                  #z = [1,3,5]
               #(or)
x = (1,2,3)
y = list(enumerate(x))
#this gives,tuple of index and element
y =[(0,1),(1,2),(2,3)]
z =[a+b for a,b in y]
#this is list comprehension on tuple
z =[0+1, 1+2, 2+3]  
print(z)                           #z = [1,3,5]
"""
"""
#2)x = 5 if float(10+10) == 20 eles 0   y = [1,2]+[x]   z = y [::-1] [-3]   print(z)
if float(10+10) == 20:
    print(True)             #True    
else:
    0
x = 5
y = [1,2]+[x]
y = [1,2,5]
z = y[::-1]#(reverse list)
z = [5,2,1][-3]#(negative indexing)
print(z)                                      #5

#
x = 'flm'                     #x having 3 elements
y = 2 and len(x)              #y having 2 elements and x passed to y
z = y or 5                    #or function is used here for 3 or 5
print(z)                      #3

# 
x = 3**3                #27
y = 3^2                 #1
z = x//y                #27
print(x)
print(y)
print(z)


#calculatIing the age of person by python codes:-
from datetime import date

def calculateAge(birthDate):
	days_in_year = 365.2425
	age = int((date.today() - birthDate).days / days_in_year)
	return age                                                #24 years
                     #OR
# Driver code
print(calculateAge(date(1998, 12, 13)), "years")

from dateutil.relativedelta import relativedelta
from datetime import date

def calculate_age(birth_date):
	today = date.today()
	age = relativedelta(today, birth_date)
	return age.years

#Test the function
birth_date = date(1999, 2, 3)
age = calculate_age(birth_date)
print(f"Age in years: {age}")                       #Age in years: 23.
                #OR
year = input('enter your birth year')
print(type(year))                         #<class 'str'>
age = 2023 -int(year)                     #enter your birth year 1999
print(age)                                #24
 
#finding the list,a by passing 2 parameters to the function by using if,elif,else statements and for loop output:-asc,desc,none
def myfunc(list,a):
    ls = list
    if a == 'asc':
        rev = False
    elif a == 'desc':
        rev = True
    elif a == 'none':
        print(list)
    if a == 'asc' or a == 'desc':
        ls.sort(reverse = rev)
        print(ls)                                 #[7, 1, 2, 6, 22]  #none
                                                  #[1, 2, 6, 7, 22]  #asc
myfunc([7,1,2,6,22],'desc')                       #[22, 7, 6, 2, 1]  #desc

#adding the elements
#la = [10,20,30,40,50]
#s = 0
#for value in la:                        
#       s = s + value
#print('answer : ',s)                           #150
#
#stable printing
#to create a 5table by forloop
#t = int(input('Enter table number : '))
#for i in range(1,21):
#       print(t,'x',i,'=',t*i)  select no what table u want to print     #5 x 1=5....5 x 20=100 
#
#range function:  print(list(range(1,10)))    #(0,1,2,3,4,5,6,7,8,9)    #range(start,end,gap):   print(list(range(1,16,2)))   #(1,3,5,7,9,11,13,15)
#
#
#32)without parameters, with return value
#def some_of_first_10_number()
#       sum = 0
#       for i in range(1,11)
#               sum = sum + i
#       return sum                    #(function creation)         
#----space
#answer = some_of_first_10_numberp()
#print(answer)                          #(function calling) #55
#
#
##4)with parameter, with return value 
#def get_count(arr,size,target_value):
#       cnt = 0
#       for i in range(0,size):                            functions ki values kavalinte parameters estham and
#           if arr[i] == target_value:                     function adhana value return chesthadhi ante return value estham
#               cnt = cnt + 1                              #(function creation)
#       return cnt
#---------space
#my_list = [1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,3,3,3,2,1,1,1]
#print('1 occurance : ',get_count(my_list,len(my_list),1))
#print('2 occurance : ',get_count(my_list,len(my_list),2))           #this will show how many times the nmbr will be repeated
#print('3 occurance : ',get_count(my_list,len(my_list),3))           #(function calling)
#print('4 occurance : ',get_count(my_list,len(my_list),4))
#
#
##recursion in python: is calling a function with in the sm function this is powerful (recursion works same as loops) is a stack this works backward calculation after base condition. loops works in forward and recursive is backward 
#1)base condition
#2)function should parameters + return
#def my_function():
#       print('Hello')
#       my_function                           #this will print nmbr of times  so don't  do this
#--------space
#my_function()                                 #hello hello helo hello hello
#ex:- 
#def my_function(n):
#      if n == 0:                                     #give the input value 10
#           return 0
#       return my_function(n-1)+n => f(9)+10 =55
#                                    f(8)+9  =45                     
#                                    f(7)+8  =36
#                                    f(6)+7  =28
#                                    f(5)+6  =21          #final output is 55
#                                    f(4)+5  =15
#                                    f(3)+4  =10
#                                    f(2)+3  =6
#                                    f(1)+2  =3
#                                    f(0)+1  =1
#-------space
#n = int(input('enter n value : '))                             #10
#answer = my_function(n)         #10give input                  #55
#print(answer)
#
###ex:program in loops    ##finding the max value in the given list
#avg_marks = [45,76,85,87,98,87,67.90,89,78,85]
#-----space
#max_value = -1
#n =len(avg_marks)
#----space
#for i in range(0,n):
#     if avg_marks[i]>max_value:
#         max_value= avg_marks[i]                            #98 will be printed
#print('max value : ',max_value)
#
##split and join                                          #split method is used for string to list
#s = 'hello how is it going'                              #join method is used for list to string
#print(list(s.split(' ')))                                #['hello', 'how', 'is', 'it', 'going']
#result_strng = ' '.join(l)
#print(result_string)                                     #how are you?
#
#2)type conversions
#l = [1,2,3,4,5]
#print(type(1))                                           #<class 'list'>
#t = tuple(1)
#print(type(t)) 
#
#l = [1,2,3,4]                                     
#s = "hello world!"
#print(len(l))                           #4
#print(len(s))                           #12
#write a programe take a positive integer as an input and print the sum of all the digits
num = int(input("Enter a number"))
digit_sum = 0
while num !=0:
    digit_sum += (num%10)                       
    num = num // 10                             #Enter a number234
print("sum of digits:",digit_sum)               #sum of digits: 9
#print all the combinatin of 2 tuples
tup1 = (4,5)
tup2 = (7,8)
li = [(a,b) for a in tup1 for b in tup2]
li += [(a,b) for a in tup2 for b in tup2]
print(li)                                   #[(4, 7), (4, 8), (5, 7), (5, 8), (7, 7), (7, 8), (8, 7), (8, 8)]

#print the number of occurence of all the elements in the given list along with the element itself
li = ['a','b','c','a','c']
occ = []
di = {}
for i in li:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1 
for k,v in di.items():
    occ.append(str(v)+k)
print(occ)                            #['2a', '1b', '2c']

#number of positive and negative numbers in the given list 
nums = [1,2,-1,-1,-2,3,4]
negative = 0
positive = 0
for i in nums:
    if i < 0:
        negative += 1
    elif i > 0:
        positive += 1
print("number of negative numbers:",negative)                  #number of negative numbers: 3
print("number of negative numbers:",positive)                  #number of negative numbers: 4

#one containing all letters in the input and another conntaining the numbers
inp = input ("")
letter = []
num = []
for i in inp:
    if i.isalpha():
        letter.append(i)
    elif i.isnumeric():
        num.append(i)                 #enter qwe @ 123
print("letters:", letter)             #letters: ['q', 'w', 'e']
print("numbers:", num)                #numbers: ['1', '2', '3']

#sentence as an input and print the number of spaces in thet sentence
int = input ("Enter a sentence:")
count = 0
for i in int:
    if i == ' ':
        count += 1                           #Enter a sentence:this is a sentence
print("number of spaces:",count)             #number of spaces: 3

#sentence as an input and print out the secound of the sentence
inp = input("Enter a sentence:").split()               #Enter a sentence:i love python
print("The second word is:", inp[1])                   #The second word is: love

#printthe sum of every 2nd element of the given list
li = [1,2,3,4,5]
summ = 0
for i in range (0,len(li),2):
    summ += li[i]            #1+3+5
print(summ)                  #9

#positive integer as input and print its reverse
num = int(input("Enter a number:"))
li = []
li_sum = 0
while num != 0:
    li.append (num%10)
    num = num//10                     #234
print (*li, sep = '')                 #432

#print the value against the key 3 in the given dictionary
di = {1:'orange',2:'mango',3:'apple'}
for key, val in di.items():
    if key == 2:
        print(val)                      #mango

#programme to take name of three fruits as an input,store it in a dictionary and print it
fruit = {}
i = 1
while i != 4:
    inp = input("Enter a fruit's name:")
    fruit [i]
    i += 1
print(fruit)                  #not cmng output

#rmove the last 2 elements from the given list
li = [1,2,3,4,5]
li.pop()
li.pop()
print(li)                 #[1, 2, 3]

#paragraph/multiple sentences as an input separated by '.' and print out the nmbr of sentences in the input
inp = input()
count = 0
for i in inp:
    if i == '.':
        count += 1                                     #this is sentence 1.this is sentence 2.
print("There are %d sentences in that paragraph."%count)#There are 2 sentences in that paragraph.

#print series of numbers and letter as an input and print seperate
inp = list(input("Enter:"))
alp = []
num = []
for i in inp:
    try:
        int(i)
        num.append(int(i))
    except:
        alp.append(i)           #abc123
print (alp,num)                 #['a', 'b', 'c'] [1, 2, 3]

#printing the elements                                             #helium
elements = ['helium','neon','argon','krypton','xenon','redon']     #neon
print("following are the 6 noble gases:")                          #argon
for i in elements:                                                 #krypton
    print(i)                                                       #xenon
                                                                   #redon

#list of shoping items as an input and print the list as a numbered list
num = int(input("number of inputs:"))            #number of inputs:3
di = {}                                          #milk
print ("Enter list items:")                      #bread
for i in range (num):                            #salt
    inp = input()                                #1.milk
    di [i+1] = inp                               #2.bread
for k,v in di.items():                           #3.salt
    print("%d. %s" %(k,v))

#    
num = 118
fact = "The periodic table has %d elements as of today."
print(fact%num)                                       #The periodic table has 118 elements as of today.

#
li = ['Mariana trench','Pacific ocean','earth']
fact = "the %s, in the %s, is the deepest location on %s."
print (fact %(li[0], li[1],li[2]))                           #the Mariana trench, in the Pacific ocean, is the deepest location on earth.

#Take a sentence as an input and print out the number of spaces in that sentence
inp = list(input("Enter a sentence:"))
count = 0
for i in inp:
    if i == ' ':
        count +=1                     #this is python
print(count)                          #2

#
mountain = "Mount Everest"
num = 8849
fact = "%s is %d meters tall"
print (fact %(mountain, num))                #Mount Everest is 8849 meters tall

#the Android version when it was hosted date printing
import datetime
os = 'Android'
x = datetime.datetime (2008, 9, 23)
date = x.strftime ("%B %d, %Y")
fact = "The first commercial version, %s 1.0 was releasedd on"
print (fact %os + date)                  #The first commercial version, Android 1.0 was releasedd onSeptember 23, 2008

#password validate.length of a valid password <=6,and one upper case,one lower case,one nmbr,one spcl char
inp = list(input("Enter your password:"))
di = {'up':0, 'lo':0, 'num':0, 'sc':0}
flag = True
for i in inp:
    if i.isupper():
        di['up'] += 1
    elif i.islower():
        di['lo'] += 1
    elif i.isdigit():
        di['num'] += 1
    else:
        di['sc'] += 1

if len(inp) >=6:
    for k, v in di.items():
        if v == 0:
            flag = False
            break
else:
    flag = False
if flag:                              #Abc@12
    print("valid")                    #valid
else:                                 #ertsfd
    print("invalid")                  #invalid

#this will print the launced date of microsoft
import datetime
os = ['Microsoft','Windows']
x = datetime.datetime(1995, 8, 24)
date = x.strftime ("%d %B %y")
fact = "%s launched %s 95 on"
print (fact %(os[0], os[1])+ date)         #Microsoft launched Windows 95 on24 August 95

#this will print the bought date of wts app
li = [16,2014]
social = ['facebook','whatsapp']
fact = "%s bought %s in %d for $%d billion."
print(fact % (social[0], social[1], li[1], li[0]))     #facebook bought whatsapp in 2014 for $16 billion.

#take input containing letters,integers and spcl char and print 'True' if the nmbr of spcl char is <=3 and 'False' if its less than3
inp = list(input('Enter:'))
count = 0
for i in inp:
    if i.isalnum() == False:
        count += 1
if count >= 3:
    print('True')
else:                  #bcd?@12
    print('False')     #False

#this will print the terms in a sentence  
di = {'amazon':'books'}
fact = "%s used to sell only %s when it started."
for k, v in di.items():
    print(fact %(k, v))                     #amazon used to sell only books when it started.

#this will print the terms in a sentence
forest = 'Amazon Raniforest'
fact = "The %s the largest thr tropical rainforest."
print(fact %forest)                       #The Amazon Raniforest the largest thr tropical rainforest.

#this will print the running sum of an array as running sum[i] sum (nums[0].....nums[i])
nums = [3,1,2,10,1]                  #[3]
ans = []                             #[3,4]
for i in range (len(nums)):          #[3,4,6]
    ans.append (sum(nums[0:i+1]))    #[3,4,6,16]
    print(ans)                       #[3,4,6,16,17]


#this will print terms in a sentence
hashtags = ['#love','#fashion','photooftheday']
fact = "as of december 2017, the most widely used hashtag on instagram was %s"    
print(fact %hashtags[0])                             #as of december 2017, the most widely used hashtag on instagram was #love
print("followed by %s & %s"%(hashtags[1], hashtags[2]))#followed by #fashion & photooftheday


#This was filling collage with no.of students
colleges = {'IIT':23, 'NIT':31, 'IIIT':25}
print("following are the number of IIT,NIT and IIIT colleges in India:")
for k, v in colleges.items():              #IIT: 23
    print("%s: %d" %(k, v))                #NIT: 31 
                                           #IIIT:25

#
li = [5, 1, 2, 3, 4]
li_dup = []
for i in li:
    li_dup.append (i)

li_dup.sort()

if li == li_dup:
    print(li ==_dup)
elif li == li_dup[::-1]:
    print(False)          #False    [5, 4, 3, 2]
else:
    print(None)           #None     [5, 1, 2, 3, 4]


#this will add in form of sentence
num = 5900
di = {'e': 'Engineering', 'c': 'Colleges', 'country': 'India'}
fact = "There are more than %d %s %s in %s."
print(fact %(num, di['e'], di['c'], di['country']))      #There are more than 5900 Engineering Colleges in India.

#this will fill in the sentences
species = ['seahorses','pipefishes','seadragons']
fact = "%s, %s & %s are the only animals where the males get pergnent."
print (fact %(species[0], species[1], species[2]))               #seahorses, pipefishes & seadragons are the only animals where the males get pergnent.

#total amount and no.of people in a group as an input and print out the amount each person has to pay. it pays =to eash other
amt = int(input("Enter the total amount: "))
num = int(input("Enter thr number of people: "))       #1000
each = amt / num                                       #2
print ("Each person pays: %d" %each)                   #500

#
num = [100, 200, 300]
time = ['hour', 'minute', 'second']
fact = "Lighting strikes earth about  %d times every %s."
print(fact %(num[2], time[1]))                   #Lighting strikes earth about  300 times every minute.

#
num = [1, 20, 500, 7000]
time = ['hours','minute','seconds']
fact = "%d %s of video is uploaded to YOUTUBE every %s"
print (fact %(num[2], time[0],time[1]))            #500 hours of video is uploaded to YOUTUBE every minute

#list of integers and string, remove all the string element and print the same list
li = [1, 2, 'a', 3, 'b', 'abc', 4]
li_copy = []
for i in li:
    li_copy.append(i)

for i in li_copy:
    try:
        int(i)
    except:
        li.remove(i)
print(i)                  #4

#program of pattern
print ('*' * 14)
for _ in range (4):
    print('*            *')

print('*' * 28)

for _ in range (4):
    print("             *             *") 
print("             " + "*" * 15)
**************
*            *
*            *
*            *
*            *
****************************
             *             *
             *             *
             *             *
             *             *
             ***************               

#add 2 list of int
l1 =[1,2,3]
l2 =[4,5,6]
ans =[]
num1 = 0 
num2 = 0
#converting list l1 into a number = 123
for i in l1:
    num1 = num1 * 10 + i
#converting list 12 into a number = 456
for j in l2:
    num2 = num2 * 10 + j
summ = num1 + num2
#converting 'ans' into a list
while summ != 0:
    ans.append(summ % 10)
    summ = summ // 10                #[5, 7, 9]
print (ans[::-1])

##this will fill in the sentences
words = ['Taj', 'Mahal']
year = 1632
fact = "%s %s's construction was started in %d."
print (fact %(words[0], words[1],year))            #Taj Mahal's construction was started in 1632.

#program of pattern
spacea = 8
spaceb = 0
while spacea != 0:
    print (' ' * spacea + '*' + ' ' * spaceb + '*')
    spacea -= 2
    spaceb += 4
for _ in range (4):
    print('*' + ' ' * 16 + '*')
print('* ' * 9 )
        **
      *    *
    *        *
  *            *
*                *
*                *
*                *
*                *
* * * * * * * * *

#this will show the sum of all input ints
inp =input("Input: ")
li = inp.split()
summ = 0
for i in li:
    try:
        summ += int(i)
    except:
        pass                                                    #abc a 5 10 def !@ 5  
print("the sum of all the numbers in the input is",summ)        #the sum of all the numbers in the input is 20
"""
#this will print the m index value 
x = 'flmFLM'
y = x.title()                #FlMfim
z = y.rfind('m')             #this search the position of element
print(z)                     #5
 
#mosh program(receiving inputs )
Name = input('what is your name? ')
print('Hi ' + name)            #hi sagar

#
Name = input('what is your name? ')
fav_colour = input('what is you fav_colour')
print(name + 'likes ' + fav_colour)                   #sagar likes black

#type conversion:-
birth_year = input('birth year: ')    #1999
print(type(birth_year))                #'str'
age = 2023 - int(birth_year)
print(type(age))                        #'int' 
print(age)                              #24

#converting ponds to kgs weight:
weight_lbs = input('weight(lbs): ')     #160
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)                         #72.0

#strings
course = "python's course for Beginners"
print(course)                 #this print 1 line
course2 = 'python for "Beginners"'
print(course2)                 #this print 1 line
course3 = '''            
Hi jhon,
Here is our first email to you.
Thank you,
the support team
'''
print(course3)                  #this print all lines
course4 = 'Python for Beginners'
print(course4[0])               #p first word
print(course4[-1])              #s last word
print(course4[0:3])             #pyt
print(course4[0:])              #this will print all line
print(course4[:5])              #pytho
another = course4[:]
print(another)                  #this will print all line 
name = 'sagarragas'
print(name[1:-1])               #agarraga

#formated strings:-
first = 'john'
last = 'smith'
message = first + ' [' +last + ']  is a coder'
print(message)                  #john [smith] is a coder
msg = f'{first} [{last}] is a coder'
print(msg)                      #john [smith] is a coder

#string methods:-
print(len(course4))             #20
print(course4.upper())          #this will print in upper case
print(course4.lower())          #this will print in lower case
print(course4.title())          #this will print as title format  
print(course4.find('p'))        #0 (shows the index value in string)
print(course4.find('O'))        #we get -1 bcz we dont have that letter in variable
print(course4.find('Beginners'))  #11
print(course4.replace('Beginners', 'Absolute Beginners'))    #this will replace the words
print(course.replace('P', 'J'))        #jython
print('Python' in course4)             #True
print('python' in course4)             #False   lower case

#arthematic opp:-
x = 10
x = x + 3
print(x)                   #13
x -= 3
print(x)                   #7 
y = 10 + 3 * 2             #16      *6 +10
x = 10 + 3 * 2 ** 2        #22      **4  *12 +10
x = (2 + 3) * 10 - 3       #47      () * -
x = 2.9
print(round(x))            #3
x = 2.9
print(abs(-2.9))           #2.9      it always returns the positive no
import math                #this is a module
print(math.ceil(2.9))      #3
print(math.floor(2.9))     #2

#if statements:-
is_hot = True                                       #False
if is_hot:
    print("its a hot day")  #its a hot day
print("enjoy your day")     #enjoy your day         #enjoy your day

is_cold = True                                                    #False
if is_cold:
    print("its a cold day")
    print("drink hot water")
else:
    print("its a hot day")                                        #its a hot day
    print("wear loose clothes")        #its a cold day            #wear loose clothes
print("enjoy your day")                #drink hot wate            #enjoy your day

is_hot = False                                                #False                      #true
is_cold = True                                               #False                       #False
if is_hot:
    print("its a hot day")                                                                 #its a hot day
    print("drink plenty of water")                                                         #drink plenty of water
elif is_cold:
    print("its a cold day")          #its a cold day
    print("wear warm clothes")       #wear warm clothes
else:                                #enjoy your day
    print("its a lovely day")                                #its a lovely day
print("enjoy your day")                                      #enjoy your day

#logical opp:-
#comparison opp:-
name = " sagar ragas"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")     #Name looks good!          

#converting
weight = int(input('weight'))
unit = input('(l)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")        #160
else:                                          #l
    converted = weight / 0.45                  #72
    print(f"you are {converted} pounds")       #k

#while condition:-   #1                    i = 1                      *
while i <= 5:        #3                    while i <= 5:              **
    print(i)         #5                        print('*' * i)         ***
    i = i +1         #Done                     i = i +1               ****
print("Done")        #                     print("Done")              *****

#secret no game:-
secret_number = 9
guess_count = 0                                      #3 chances of guessing the number
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1                      
    if guess == secret_number:
        print('you won!')
              #(or)
guess_count = 0                            
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))                #3 chances of guessing the number
    guess_count += 1                            
    if guess == secret_number:
        print('You won!')
        break
else:
    print('sorry, you failed!') 

#for loop
for item in ['Mosh', 'John','Sarah']:   #mosh
    print(item)                         #john
                                        #Sarah
for item in range(10):
    print(item)                         #1 to 10
for item in range(5,10):
    print(item)                         #5 t0 9  
for item in range(5,10,2):
    print(item)                         #5 7 9 
#
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:                    #x
    output = ''                            #xx
    for count in range(x_count):           #xxx
        output += 'x'                      #xxxx
    print(output)                          #xxxxx
#lists:-
names = ['sagar','ragas','raju','ramu']
print(names)                     #al printed
print(names[1])                  #ragas
#finding largest noin list:
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)                          #10

#