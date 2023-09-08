#Beliver01:-youtube       computer only knows programming language.     #python is a dynamically typed programming.         #python -m pip install boto3 (to install a boto3 in visual studio)   we can append,update & access the values in list. but in tuple we cant update,append & we can only access the values. in sets we can add but we cant update & access. in dic we can add,access by key & we cant update.    (str and tuple is imutable).list and tuple has indexing to access but set dont support for accessing.  
#python:- is a type of programming language.Pyhthon is a general purpose high level programming language. is a set of extensions that given to computer to complete the task.
#in python indentation is very imp                                                                                             #conditional statements (if,elif,else,nested if),   Number System(ex: Converting Decimal to Binary format and Converting Binary to Decimal format)
#Applications of python programming language:-we can create web apps,web development,game development,m/c learning and Ai,data science & data visualization,business app,audio & video app     the file must contain last .py extention for conventing running code.        commenting:-#(single line) """"""(multi lines)
##1) variables(is as container which used to store the data):- a variable name can be started with: lower case,upper case,under socre_,one2,One3,_one, (variable will store the elements (or) data values in it) age=18 variable names can be written multi words in camelCase,pascalcase,snake_case(good to use) sagarRagas. dont give python keywords as variable name,varible name dont start with numbers dont use symbols.
#print and input in python:-input taking data from users(scan off), output is displaying data to user(print off)                                                         print(age)18
#
#data types:-1)nmbrs-int(1,2,4,5),2)words-string'sagar'"",3)bool(true or false) this is basic Dt or primitive Dt
#array type Dt (or) secquencial Dt(group of data storing):4)set{} 5)tuple() 6)list[group of data] this store group of values    (list,tuple,set,str)
#7)dictionary: this store pair of key values {}                   float=1.2,3.4. complex3+2j,1+4j.
#8)user defined Dt is also knowns as classes by this python got the name as object oriented programming language(according to our requirement)
#in list functions:-[]in(certain element),index(element index),len(),append(element added last),max(),min(),sort(assending order),remove()
#in tuple:-() is sm like list but cannot be changed once data assigned to it(immutable nature) print(type(t)). this will run fastly compared to list functions:-len(),max(),min(),index() 
#in sets:-{}this is decleared by variables s r a. this wont assign duplicate values or remove duplicate values or repeated values. in sets there will not be indexes like list&tuple by this we cant update elements sm like tuple.in set they wont print in given order this will store by itself to become faster & it changes always the element spaces.function:-max(),min(),len(),remove(),add()
#dictionaries:-{}stores pair of values key:value d = {'name':'sagar80','nationality':'india'} print(d['name']) in this we use key as a index to run adding 2types,printer access2types function:-   max(),min(),len()    
#indentation:-maintaining space. in if,elif,else we have give a tab or 4spaces to go inside statement.
#operators in python:-arithmetic operators(+add)(-sub)(*mul)(/divied)(%reminder(modules))(2**3=8 or 2e3 2power3 power calculation)(5/2=2.5float)(5//2=2int)
#                     conditional operators (==equal)(<lessthan)(>grt)(<=lessequal)(>=grtequal)(!=not equal)
#                     logical operators(this are used in between conditional operators) (and , or , not) (in , not in checking a element in or not in list) 
#                     Bitwise operators(is used in compler to run) (& and, | or, ^ xor)

#lan =['sagar','vmc']
#if len(lan) == 3:
#    print("3 persons = 3 names")       #'sagar','vmc','yash'         #3 persons = 3 names
#elif len(lan) >= 3:
#    print("len of list is more")       #'sagar','vmc','yash','navi'  #len of list is more
#else:
#    print("3 persons != 3 names")       #'sagar','vmc'                #3 persons <= 3 names

#convert Decimal to Binary:-By using 2^01234568....(1,2,,4,8,16,32,64,128,256)              #convert Binary to Decimal:- 1    0    1     0   
#339-256=83   1    16    #256+64+16+2+1 = 339                                                                            2^3  2^2  2^1  2^0   =8 + 2 =10   
#128          0           #16**2
#83-64=19     1     8     #8**2                                                                                                    1     0      0     1       0
#32           0                                                                                                                 2^4    2^3    2^2   2^1     2^0  =16 + 2 =18
#19-16=3      1     4     #4**2
#8            0                                                                                                           1       1       0          0      .1       0         1
#4            0                                                                                                          2^3     2^2      2^1        2^0     2^-1    2^-2     2^-3   =8+4+1/2+1/8  =12+0.5+0.125 = 12.625
#3-2=1        1     1      #1**2                                                                                                    
#1-1=0        1     0      #0**2

#name = input()                                     #by default the input function takes every thing as a string format.
#print(name)                                        #give input  sagar                                   
#commrenting #single, """multiple"""
#name = 'sagar'                                      #this is Declaring variable
#print(name)                                         #sagar
#name = input()                                      #while giving input it take it as string whether ur given int also. 
#print(name,'welcome to our channel')                #sagar welcome to our channel            #this is input method
#name = input('Enter your name:')                    #we have to give our name sagar          #this say enter your name
#print('Hello',name,'welcome to our channel')        #Hello sagar welcome to our channel      #print is output statement

#print('hello world',end=' ')
#print('hello world')                         #hello world hello world  #this will give output in same line. by using end function.
#print("sagar",end=' ')
#print("python")                                #sagar python
#print("sagar \nragas")                         #sagar
#                                               #ragas

#v1 = 10 
#v2 ='sagar'
#v3 = 4.8
#v4 = true                               #parmitive data type (or basic Dt)
#print(type(v1))                         #int
#print(type(v2))                         #str
#print(type(v3))                         #float
#print(type(v4))                         #bool


                #changeable & access bcz it has index values.
#list:-[]Square Brackets              #group of data values (type of variable)  is a array or sequencial Dt.
#     0,1,2,3,   4 ,    5             #index values
#arr=[1,2,3,4.3,'sagar','mine']           #List Functionalities
#print(arr)                               #and it prints sm as we given
#print(type(arr))                         #list         
#print(len(arr))                          #this will print length    #6
#print(3 in arr)                          #checking the value in list or not      #True
#print(15 in arr)                                                                 #False
#length_list = len(arr)
#print(length_list)                      #6
#print(arr[0])                           #1         arr[2]      #3
#print(arr.index(4.3))                   #3 this will show the 4.3 index value
#req_index = arr.index(3)
#print(req_index)                       #this will show the 3 value index  #2
#arr.append(15)                         #In append method we can add only one str (or) int (or) float. 
#arr.append(12)                  
#print(arr)                            #this will add 15,12 in last of the list values.
#print(max(arr))                       #this will print max value in list(15)
#print(min(arr))                       #this will print min value in list(1)
#arr1 = [1,8,9,8,5,3,5]                #for sorting we have take only one Dt (int).
#print('before sorting : ',end="")
#print(arr1)                                 #this will show before sorting : [1, 8, 9, 8, 5, 3, 5]
#arr1.sort()
#print('after sorting : ',end="")
#print(arr1)                                #this will show ascending order after sorting : [1, 3, 5, 5, 8, 8, 9]
#arr.remove(3)
#print(arr)                                #this will remove 3 from the list [1, 2, 4.3, 'sagar', 'mine']
#arr[0]= 10 
#print(arr)                                #now the 0index is replaced by 10 (updated by index)  [10, 2, 3, 4.3, 'sagar', 'mine']

#tuple;-()Parenthuses     immutable it doesn't change the values once it assigned the data value      #fixed(can not be updated)(but we can access through index) (this is fast compared to list) we cant sort in tuple.
#t = (1,2,3,4)                     #used to work fast no need to update again
#print(type(t))                    #'tuple' we cant update the values 
#print(len(t))                     #this will show length 4.
#print(min(t))                     #this will show min value 1
#print(max(t))                     #this will show max value 4
#print(t.index(4))                 #this will show index value of 4. we can see the index value but we cant update.#3
#t[0] = 10               #bcz tuple can not be updated or not supported for item assignment. bcz it is immutable.  
#print(t[1])             #2

#sets:-{}curely brackets        #remove duplicate values in set #this will save the values according itself.sets dont have indexes(bcz they dont have order). we cant update the data to it.
#s = {3,3,3,2,2,1,1}    
#print(s)                        #{1,2,3} there dont have indexes in sets & no order.  it also sort directly 
#print('set data : ',s)          #set data :  {1, 2, 3}
#s.add(8)                #adding new value in set.  {8, 1, 2, 3}    
#print(s)                #{1,2,3,8}   (no order,no duplicate values,)
#print(len(s))           #this will show length 4
#print(max(s))           #this will show max value 8
#print(min(s))           #this will show min value 1
#s.remove(2)
#print(s)                  #this will remove the 2 from set. {8, 1, 3}


#dictionaries:-{}key value pairs & don't allow to print duplicate values.   a - 90  b - 80  c - 70  #key:value
#d ={'name':'sagar','nationality':'india'}
#print(d['name'])         #sagar       #(key is given by us)
#two ways of inserting data into the dic:-
#d['edu']='Btech'
#print(d)                                      #{'name': 'sagar', 'nationality': 'india', 'edu': 'Btech'}
#d.__setitem__('nationality','india')         #2 types of methods this will be added to sets

#this two types we access the values in dic:-
#print(d['name'])          #sagar          
#print(d.get('name'))      #sagar  #this will access the dic by using key we get values. 

#dic = {1:10,2:20,3:30,4:40}
#print(len(dic))                   #lenth  4
#print(max(dic))                    #max   4
#print(min(dic))                    #min   1
#Add
#dic[4] = 50                        #add 
#dic.__setitem__(4,50)              #add
#print(dic)                         #{1: 10, 2: 20, 3: 30, 4: 50}    {1: 10, 2: 20, 3: 30, 4: 50}
#print(dic[1])                       #10


#indentation:-4spaces have to give
#akan = True               #conditional operator
#if akan == True:
#    print('hello world')
#else:
#    print('not hello world!')           #hello world
 
#if akan == False:
#    print('hello world')
#else:
#    print('not hello world!')           #not hello world!      


#arthematic operators:-
#a = 4
#b = 3
#add = a+b
#sub = a-b
#mul = a*b
#div = a/b     #(quatient)
#modules = a%b #(reminder)
#power = a**b (power calculations)
#integer_div = a//b(this will remove the decimals)
#print('Addtion : ',add)                  #7
#print('sub : ',sub)                      #1
#print('mult : ',mul)                     #12
#print('div : ',div)                      #1.3333
#print('modules : ',modules)               #1
#print('power : ',p)                      #64
#print('Interger div : ',integer_div)     #1


#conditional operators:-This returns Boolen values.
#a = 10
#b = 11
#print(a == b)          #false
#print(a<b)             #true
#print(a>b)             #false
#print(a!=b)            #true
#print(a<=b)            #true  
#print(a>=b)            #false


#logical operators: used between condition operators (and,or,in,not in,is,is not)
#print(10<11 and 15<16) #true and true = true     print(10<11 or 15<16) true or true =true
#false and true =false                            false or true =true                  
#true and false =false                            true or false =true                  
#false and false = false                          false or false =false

#c = True                         c = False
#print(not c)      #False         print(not c)   #True

#in,not in
#l=[1,2,3,4,5]
#print(4 in l)        #True
#print(4 not in l)    #False bcz 4 is inside the list

#is ,is not
#a = 10
#b = 11
#print(a is b)            #False                                          #int('30') = 30
#    print('not hello')              #18 hello       12 not hello                 #float('30') = 30.0
 
#1)voter_age = int(input('enter your age:' ,))
#if  voter_age > 18:
#    print("you are elligeble to vote")
#elif voter_age == 18:
#    print("You are perfect to vote")    
#else:
#    print("your are not eligable to vote")              #if you given 20 you are elligeble to vote. 18 You are perfect to vote. 12 your not eligable to vote.
#                                                        #str(30) = 30   int('30')=30  
#name = input('enter your name:')                           #sagar
#age = int(input('enter your age:'))                        #17, 21
#if age <= 18:                                              #sagar sorry you are not eligible!           (lessthen<)
#      print(name,'sorry you are not eligible!')            #hello sagar you are welcome!
#else:  
#     print('hello',name,', you are welcome!')
#after run we have to give name and age then the output will be printed    sagar,17,sagar,21

#check = int(input("enter a number : "))             #even or odd.  pass only one data value.
#if check % 2 == 0:
#    print("this number is even")                   #68428if we given even values this print. this number is even        
#else:
#    print("this number is odd")                    #1357if we given odd values this print. this number is odd
                                                    
#nmbr = int(input("enter a number :"))
#if nmbr % 7 == 0:
#    print("this divisible by seven")           #14 this divisible by seven
#else:    
#    print("this is not divided by seven")      #55  this is not divided by seven

         
#age = int(input("enter your age :"))
#if age > 18:
#    print("you are old enough to drive")                    #19  you are old enough to drive
#elif age < 18:
#    z = 18 - age
#    print("you need",z,"more yers to learn to drive")        #17 you need 1 more years to learn to Drive
#else:
#     print("your perfect to drive")                          #18 your perfect to drive

#my_age = int(input("enter my age:"))         #Nested if
#your_age = int(input("enter your age:"))
#if my_age <  your_age:
#    diff = (your_age - my_age)
#    if diff == 1:
#        print("you are one year elder then me")                #32 33 you are one year ealder then me
#    else:
#        print("You are ", diff, "years elder than me")         #24 34 You are  10 years ealder than me
#else:
#    print("our age is equal")                                  #45 45 our age is equal.

#if my_age > your_age:
#    diff = (my_age - your_age)
#    if diff == 1:
#        print("I am one year ealder then you")                  #33 32 I am one year ealder then you
#    else:
#        print("I am ", diff, "years ealder than you")           #34 24 I am  10 years ealder than you
#else:
#    print("Our age is equal")                                   #33 33 Our age is equal
#           (or)
#a = int(input("enter my age:"))
#b = int(input("enter your age:"))
#if a == b:
#    print("ages are equal")                          #10 10 ages are equal
#elif a > b:
#    z = a - b
#    print("i am",z,"years elder than you")            #i am 10 years older than you
#elif a < b:
#    k = b - a
#    print("you are",k,"years elder than me")         #24 34 you are 10 years older than me
#else:
#    print("there is no age")

##if elif else (if multiple conditions are there we use elif statement)
#marks = float(input('Enter your marks:'))
#if marks >= 90:
#   print('your grade is : A')                           #98    #'your grade is : 'A'
#elif marks >=80 and marks <90:                         
#   print('your grade is : B')                           #82    #'your grade is : 'B'
#elif marks >=70 and marks <80:                         
#   print('your grade is : c')                           #75    #'your grade is : 'c'                
#else: 
#   print('sorry, you are failed!')                      #50    #'sorry, you are failed!'
#we have to give marks by printing that we can grade

#name = input("enter your name :")
#if name == "sagar":
#    print("Btech mechanical")
#elif name == "yash":
#    print("btech mechanical")
#elif name == "vamsi":
#    print("Btech EEE")
#elif name == "Dillip":     
#    print("Btech Instrumention")
#else:
#    print("the person is not in our data")

#learn = ["apple", "Banana", "Kiwi", "Orange"]
#fruit = input("give a fruit name :" )
#if fruit in learn:
#    print("this is in the list" )            #apple   this is in the list     
#else:
#    print("this is not in the list")         #mango    this is not in the list    ['apple', 'Banana', 'Kiwi', 'Orange', 'mango']
#    learn.append(fruit)
#    print(learn)  
  
#Nested if statement using of if conditions inside multiple if conditions (n no.of blocks used)
#name = input('enter your name:')              #sagar
#age = int(input('enter your age:'))           #23
#gender = input('enter your gender(M/F):')     #M
# -------space
#if age >=18:
#    if gender == 'M':
#        print('hello Mr.',name,', welcome!')
#     else:
#         print('hello Mrs.',name,', welcome!')
#else:
#   print('you are not Eligible!')                            #virat 25 M(#hello Mr.virat , welcome!)    anushka 24 F(#hello Mrs.anushka , welcome!)   user 15 M(#you are not Eligible!)

#a='hello'             #h
#for i in a:           #e  #we get in line by line.
#    print(i)          #l

#a= 'h'
#b= 'l'
#c= 'o'
#for i in a,b,c:
#    print(i,end="")         #hlo

#a = 'h\ne\nl\nl\no'
#print(a)

#name = input("enter your name : ")
#age = int(input("enter your age : "))
#Branch = input("enter your branch: ")
#rank = int(input("enter your rank : "))
#if age >= 18:
#    if Branch ==("mechanical"):                    
#        if rank == (1):  
#            print( "Hello welcome!", name, "mechanical engineer!")            #sagar,18,mechanical,1  #Hello welcome! sagar mechanical engineer!
#        else:
#            print("your rank was not elligable")                                  #sagar,18,mechanical,8  #your rank was not elligable
#    else:
#        print("eee")                                                              #sagar,18,cse,1       #eee
#else:
#    print("Hello welcome!" ,name, "you are from another branch!")                #sagar,9,ece,78  #Hello welcome! sagar you are from another branch!


#If main in python:-python will work on modules. each python file is called module.
#first.py file                        #second.py file
#import second                         #a=10
#modules                              -------space
#print(second.a)                        
#------space                             #if __name__ == '__main__':        #this says only when sencode file calls at that  moment it have to run.
# if __name__ == '__main__':                print('secondfile')
#       print('first file')  4y5

#loops introduction (if any work we have to do n number of times then we use loops):-    1)for loop(is used mostly)(run for range) 2)while loop(it is continues for true or false)
#while using forloop we use range function. range function:-  print(list(range(1,11)))    #[1,2,3,4,5,6,7,8,9,10]    #range(start,end,gap):   print(list(range(1,16,2)))   #[1,3,5,7,9,11,13,15]   print(list(range(0,21,2))) [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#marks = [99,90,85,67,95,90]          #for loop
#sum = 0
#for i in marks:
#    sum = sum + i
#print(sum)             #526
#n = 6
#avg = sum/n
#print('Average : ',avg)    #this will show the avg value #87.66666 by using for loop
  

#salary = [1,2,3,4,5,6]               
#suk = 0
#for i in salary:      
# suk = suk + i
#print(suk)                    #21
#print(sum(salary))             #21

#la = [10,20,30,40,50]
#s = 0
#for i in la:                        
#       s = s + i
#print('answer : ',s)                     #150 sum of all

#kk = [1,2,3,4,5,6,7,8,9]
#d = sum(kk)
#print(d)                 #45

#a = [1,2,3,4,5,6,7,8]
#h = []
#n = []
#for i in a:
#    if i % 2 == 0:
#        h.append(i)
#    else:
#       n.append(i)
#print(h)              #[2, 4, 6, 8]even numbers
#print(n)              #[1, 3, 5, 7]odd numbers


"""
x = (input("enter values: "))
y =x.split(",")                        #string to list by using split method
b = []
k = []
for i in y:
    j = int(i)                        #moving str to integer.
    if j % 2 == 0:
        b.append(j)
    else:
        k.append(j)
print(b)            #[2, 4, 6, 8] #even number
print(k)            #[1, 3, 5, 7] #odd number
print(y)            #['1', '2', '3', '4', '5', '6', '7', '8']
"""
 
#no = (input("enter a value: "))
#my_list = no.split(",")                            #str to list split is used
#print(my_list)                 
#new = int(my_list[-1])
#if new % 3 ==  0:
#    print("it is divisable")         #['33', '66', '99']    #it is divisable
#else:
#    print("not divisable")           #['33','41','22']      #it is  not divisable

#k = ["sagar","ragas","python"]
#s = ' '.join(k)                                    
#print(s)              #sagar ragas python
#print(type(s))         #str                  #list to str by using join method.
#k ="sagar,ragas,python"
#s = k.split(",")
#print(s)              #['sagar', 'ragas', 'python']
#print(type(s))        #list
                 
"""

#for i in range(1,11):                                                                     #1st type for i in range(1,21):
#       print(i,"sagar01")  #1 sagar01 2 sagar01 3 sagar01 4 sagar01 5 sagar01 10 sagar01   #this will print 10times               //some code
#
#la = [1,2,3,4,5]    #1                                                                #2nd type la = [4,5,5]
#for i in la:        #2                                                                   for value in la:
#       print(i)     #3   #this printed line by line.                                     //some code


#to create a 5table by forloop
#t = int(input('Enter table number : '))
#for i in range(1,21):
#       print(t,'x',i,'=',t*i)  #select number what table u want to print     #5 x 1=5....5 x 20=100 

#ta = int(input("enter the table valu: "))
#for i in (range(1,21)):
#    print(ta,'x',i,'=',t*i)             #give the value 12 we get 12 table

#for loop said 2types        (1)range & 2)sequence)
#1)for i in range(start,end,gap):        #2)l = [4,5,5]
#       //some code                    #for value in l:
                                           #//some code

#ky = [10,20,30,40,66,88,27]
#if ky[-1] % 3 == 0:
#    print("this is divisiable by three")        #27    this is divisiable by three 
#else:
#    print("this is not divisible by three")     #32  this is not divisible by three


#aa = int((input("enter the value: ")))
#if 100<=aa<=999:
#    print("this value is three digit")        #333 this value is three digit
#else:
#    print("this value is not a three digit")    #22  this value is no a three digit

#ak = (input("enter a value : "))
#l = len(ak)
#if l == 3:
#    print("there is 3 digit" )             #777  there is 3 digit
#elif l>3:
#    print("this value is more than 3 digit")  #1234 this value is more than 3 digit
#else:
#    print("this value is lessthan 3 digit")    #11  this value is no a 3 digit

#i = input("enter a number : ")
#k = i[-1]
#j= int(k)
#if j % 2 == 0:
#    print("value is divisable 2")            #44  value is divisable 2
#else: 
#    print("value is not divisiable 2")       #43 value is not divisiab1e 2


#while loop (sm as for loop)
#i = 0                                                                           #whileloopcondition:
#while i<11:                                                              
#     print(i,'Hello')                                    #whileloop            #//some code
#     i = i+1                   #(0 Hello............10 Hello tyms printed)     #//increment statement or decrement statement   (this line is imp whileloop)

#for i in range(0,11):                                      #forloop
#    print(i,'hello')             #(0 Hello............10 Hello tyms printed)     


#Break and continue and pass(pass statements only used in py.)  (if we want to stop suddenly our loop we use) this must be used inside if
#lan = ['user1','user2','user3','user4','user5']
#is_present = False
#for name in lan:
#       if name == 'user3':                       #checking weather 3 present or not
#           is_present = True
#           break                                   #breaking the loop when we found our needy(time will be saved. performance increased)
#if is_present == True:
#     print('user3 is present in the list!')        #user3 is present in the list!
#else:           
#     print('user9 is not present in the list!')      #user9 is not present in the list!  


#continue statement: this must used inside if (this is used to skip one nmbr and print another nmbr)
#for i in range (1,11):
#      print(i)               #this print all 1 to 10 nmbrs 
#      if i == 5:
#           continue
#      print(i)              #this print 1 to 10 but removes 5 (1,2,3,4,6,7,8,9,10)
#            break
#      print(i)               #1 2 3 4

#pass statement: this says there is no code but stay empty
#if condition:
#       pass             #(creating a empty statement)
 

#functions in python:1)funtions is used to prevent the duplicate code,well structured or (organaized way)  
#functions syntax:- 1)function creation  2)function calling (print(hello)) 
#def function_name(parameters):                    #def:-(short form for define a function)
#       //code
#       return some_result

##ex:- a company 3 categories
#manager = [34,56,78,98]                         #lists #arr
#developer = [32,45,34,67,98]
#support_staff = [12,54,67,89,90,45,32]
#-----space 
#def get_avg(arr):                               #function creation  #passing nem and parameter. 
#       n = len(arr)
#       sum = 0
#       for i in range(0,n):
#               sum = sum + arr[i]
#       return  sum/n                             #(by using this we get avgs of 3 categires)
#---space                                                     
#print('Manger Avg : ',get_avg(manager))                      #66.5   #calling the function
#print('Developer Avg : ',get_avg(developer))                 #55.2
#print('support Avg : ',get_avg(support_staff))               #55.5714287 
 
#def function_name(parameters):
#    //some
#    return some_result

#type of functions:- 1)function creation 2)function calling
#1)without parameters, without return value
#def welcome_msg():                               #welcome_msg()  = this is name.
#       print('hello, Nice to see you!')       #(function creation)   def= define a function. 
#       print('welcome to our application!')
# ----space
#welcome_msg() 
#welcome_msg()           #(function calling)                        #hello, Nice to see you!
#welcome_msg()           #just a msgs will be printed for 4 times   #welcome to our application!
#welcome_msg() 

#2)without parameters, with return value
#def sum_of_first_10_number():                          #name      
#       sum = 0
#       for i in range(1,11):
#               sum = sum + i
#       return sum                    #(function creation)     #for loop        with return value & function calling by name. 
#----space
#answer = sum_of_first_10_number()
#print(answer)                        #(function calling) #55 just like forloop

#3)with parameter, without return value
#def welcome_user(name,gender):                                 #name and gender are parameters
#       if gender == 'M':
#           print('welcome Mr.',name,', Have a nice day!')
#       else:
#           print('welcome Mrs.',name,',Have a nice day!')         #(function creation) if,else conditional statements. 
#------space
#name = input('Enter your name:')
#gender = input('Enter your gender(M/F)')         #run the code by giving the name and gender one M and one F by using if else statement.

#welcome_user(name,gender)                        #(function calling)                    #welcome mr. virat , have a nice day     #welcome mrs. Anushka , have a nice day

#4)with parameter, with return value 
#def get_count(arr,size,target_value):          #name #parameter.
#       cnt = 0
#       for i in range(0,size):                            # functions ki values kavalinte parameters estham and
#            if arr[i] == target_value:                    # function adhana value return chesthadhi ante return value estham
#               cnt = cnt + 1                              #(function creation)
#       return cnt                                         
#---------space
#my_list = [1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,3,3,3,2,1,1,1]
#print('1 occurance : ',get_count(my_list,len(my_list),1))       #1 occurance :  4
#print('2 occurance : ',get_count(my_list,len(my_list),2))       #2 occurance :  4   #this will show how many times the nmbr will be repeated
#print('3 occurance : ',get_count(my_list,len(my_list),3))       #3 occurance :  7   #(function calling)
#print('4 occurance : ',get_count(my_list,len(my_list),4))       #4 occurance :  4

"""
#recursion in python:- is calling a function with in the sm function this is powerful (recursion works same as loops) is a stack this works backward calculation after base condition. (loops works on forward and recursion works on backward)
#1)base condition
#2)function should parameters + return
#def my_function():
#       print('Hello')
#       my_function                           #this will print nmbr of times  so don't  do this
#--------space
#my_function()                                 #hello hello hello hello hello     #this is looped infinite times.

#ex:- sum of first n natural numbers using recursion.    
#def my_function(n):
#      if n == 0:                                 #base condition    #give the input value 10
#           return 0 
#      return my_function(n-1)+n      #=>f(9)45+10 =55                 #first this do recursive calls for condition satisfy once it satisfied. then it calculate backword. this works in backword.
#                                    #=>f(8)36+9  =45                     
#                                    #=>f(7)28+8  =36
#                                    #=>f(6)21+7  =28
#                                    #=>f(5)15+6  =21          #final output is 55
#                                    #=>f(4)10+5  =15
#                                    #=>f(3)6+4  =10
#                                    #=>f(2)3+3  =6
#                                    #=>f(1)1+2  =3
#                                    #=>f(0)0+1  =1
#-------space
#n = int(input('enter n value : '))                             #10
#answer = my_function(n)         #10give input                  #55            #function calling
#print(answer)

#no = int(input('enter a value : ')) 
#def fun(no):
#    if no == 0:
#        return 0
#    return no + fun(no-1)        #return n*fact(n-1)
#print(fun(no))          #55      #print(fact(10))      #3628800
"""

##ex:program in loops    ##finding the max value in the given list
#marks = [45,76,85,87,98,87,67,90,89,78,85]
#max_value = -1
#n =len(marks)
#for i in range(0,n):
#     if marks[i]>max_value:
#         max_value = marks[i]                            
#print('max value : ',max_value)                   #98 will be printed
          #or                         #without creating the function  #98
#print(max(marks))             #98
     # (or)
#for i in marks:
#    if i == max(marks):
#        print(i)               #98
#         (or)
#marks.sort()               #acsending
#print(marks)
#print(marks[-1])          #98
#print(marks[0])            #45
#            (or)
#marks.sort(reverse=True)     #desending
#print(marks)
#print(marks[0])           #98
#print(marks[-1])          #45
#             (or)
#ma = [45,76,85,87,98,87,67,90,89,78]
#min = ma[0]
#for i in ma:
#    if i < min:
#        min = i
#print(min)                                  #45
#max = ma[0]
#for i in ma:
#    if i > max:
#        max = i
#print(max)                                  #98


#def main():                     #function
#    print("Hello world!")

#if __name__ == '__main__':
#    main()                         #Hello world!

##ex:-program on function concept (function,loop and list) used in student result
##45 89 76 54 98 67
#def get_grade(avg_marks):                             #function creation
#   if avg_marks>=90:
#       return 'A'
#   elif avg_marks>=80 and avg_marks<90:
#       return 'B'                                  #grade  code
#   elif avg_marks>=70 and avg_marks<80:
#       return 'C'
#   elif avg_marks>=60 and avg_marks<70:
#       return 'D'
#   else:
#       return 'E'
#-------space
#def get_average(marks_list):                #function creation
#   sum = 0
#   n = len(marks_list)
#   for i in range(0,n):                              #avg marks code
#       sum = sum + marks_list[i]
#   return sum/n                              
#----space
#def main():                                                      #main function starting point.                   
#       no_student = int(input('Enter Number of students'))
#       name_list = []
#       avg_list = []
#       for i in range(0,no_student):
#           name = input('Enter student name:')                                             #def main
#           marks_list = list(map(int,input('Enter 6 subjects marks :').split(' ')))       #split method converts srt to list
#           name_list.append(name)
#           avg_list.append(get_average(marks_list))
#       #printing result
#       for i in range(0,no_student):
#           print('-------------------')
#           print('Name : ',name_list[i])                                                 #result printing
#           print('avg marks : ',avg_list[i])
#           print('grade : ',get_grade(avg_list[i]))
#--------space
#if __name__=='__main__':
#      main()                              #__name__ (module)   #main    protection when we import this file this makes wont run automatically #only calling or running the function.
#
#ans this we have to give input in terminal
#Enter number of students data:3
#enter student name:user1                                       user1 68.66666 D
#enter student 6 subject marks:45 76 98 76 48 69
#enter student name:user2                                       user2 81.333333 B
#enter student 6 subject marks:76 87 68 90 89 78
#enter student name:user3                                       user3 74.5 c
#enter student 6 subject marks:67 54 87 69 80 90
#result:-we get in terminal
#name : user1   user2   user3
#avg : 68.666  81.333  74.5
#grade: D         B     C


##ex:-program on Dictionary concept:this is voting polling of cricketer now who is the best cricketer we have to check by python
#data = ['kohli','kohli','smith','williamson','poting','kohli','de_villars','kohli','smith','smith','ponting','ponting','ponting','kohli',
#        'kohli','ponting','kohli','de_villiars','kohli','de_villiars','ponting','kohli','de_villiars','de_villiars','ponting',] 
#--------space                                                    
#my_dic = {}                                                  #kohli  :  9
#---------space                                               #smith  :  3
#for i in range(0,len(data)):                                 #williamson  :  1                              
#    temp = my_dic.get(data[i])                               #poting  :  1
#     if temp is None:                                        #de_villars  :  1
#          my_dic[data[i]] = 1                                #ponting  :  6
#     else:                                                   #de_villiars  :  4
#          my_dic[data[i]] = temp + 1
#---------space
#for player_name,votes in my_dic.items():
#    print(player_name,' : ',votes)                          #this will print in key value format. 



#strings intro in python:-''""  word or sentence.
#v1 = 'strings in python'
#print(type(v1))                                                      #<class'str'>
##for i in v1:                                                 #s
#       print(i)                                               #t            if we assign a element in values it cant be changed or replaced
###print(v1[0])          #s                                    #r            print the element by using indexing
#v1[0] = 'v'
#print(v1)                                                  #we cant modifiy the str character we can only access by indexing.
####for character in v1:                                    computer only supports for numerical language thats y every element has one numeric value to store in computer
#       print(ord(character))                               (str works on aschii values a-z ->numerical) 115 116 114 105 110 103 115 32 105 110 32 112 121 116 104 111 110 shows the nmbrs
#print(chr(97))                                             #a            (97=a)
##--------space
#H1 = 'Hello World!'                                                    
#print(H1.lower())                                                     #hello world!
#print(H1.upper())                                                     #HELLO WORLD!
#print(H1.title())                                                     #Hello World!
#H2 = 'Hi there'
#------space
#print(H1+H2)                                                         #Hello World!hi there (adding to strings)str cat or str concatntion
#H1 = 'Hello World!'
#H2 = 'Hi there'
#-------space
#if v1 == v2:
#    print('equal')
#else:                                                                #Not equal
#   print('Not equal')


#string applications and functions:-
#1)string slicing and join
#s = 'how are you?'
#print(s[0:3])                                             #how will printed in slicing this works on indexing          
#print(s[4:7])                                             #are
#l = [1,2,3,4,5]
#print(l)                                                 #[1,2,3,4,5]   we can do slicing in str & list.
#print(1[0:3])                                            #[1,2,3]
#l = ['how','are','you?']
#print(l)                                                 #['how','are','you?']

##string functionalities:-(split and join)                                             #split method is used for string converted list
#s = 'hello how is it going'                  #str           #join method is used for list converted string
#s1 = ['hello', 'how', 'is', 'it', 'going' ]  #list
#print(list(s.split(' ')))                           #sls     #['hello', 'how', 'is', 'it', 'going']  #str to list by using split.
#r = ' '.join(s1)                                    #lsj
#print(r)                                      #hello how is it going         #list to str by using join.s

#2)type conversions    if we want to convert list to str(.join) & str to list(.split)
#l = [1,2,3,4,5]
#print(type(1))                                           #<class 'list'>
#t = tuple(1)                                             #list to tuple
#print(type(t))                                           #<class 'tuple'>                                                        #list to tuple, tuple to list,set to list,list to set
#s =set(l)                                                #list so set
#print(type(s))                                           #<class 'set'> 
#list to tuple
#tuple to list
#set to list
#list to set

#3)fstring 
#a = 10
#b = 20                                             
#c = 30
#print(f'a : {a} , b : {b} , c : {c}')                    #a : 10 , b : 20 , c : 30
#s = f'{1+2} {3+4} {5+6}' 
#print(s)                                                 #3 7 11 converted in string format.


#oops concept intro in python:object orinted programming by using oops concept nmbr of values printed by one function name (by using this concept 1)security 2)duplicate remove 3)re usability of the existing code 4)gives good structure)we can hide our data by that only cls lo vunna vale access chestharu
#Inheritance:-allows us to define a cls that inherits all the methods & properties from another cls.
#Polymorphism:-(an object's ability to take on multiple forms)Having multiple forms. using the same function name, but with different signatures,for multiple types.
#Encapsulation:-A mechanism of wrapping the data(varibles) & code acting on the data (methods) together as a single unit. in encapsulation,the variables of a cls will be hidden from other classes, & can be accessed only through the methods of their current cls.
#Abstraction:-is a process of handling unnecssary information from the user.

#classes and object in python(cls is user defined data types)(object is physical existance)(object orinted programming)(C language doesnot support for oops concepts)
#creation of a cls(class is a blue print or plan (cls is a combination of variables and methods)(obj is physical existence)

#class student():
#    pass                 #if cls is empty we use pass statement.
#v1 = student()
#print(v1)                  #<__main__.student object at 0x0000021B77F1E750> #this is normal class this will show the momery address.

#cls and object creation and calling:-

#class student:                                 #class     __init__ is a constructor(constructor is starting point of class)
#   def __init__(self,id,name,age):             #this is contructor(self is cls function & id,name,age are parameters or arrgument)
#       self.id = id
#       self.name = name                       #class creation #variables or attributes
#       self.age = age
#------space
##   def print_id_name(self):                       #2nd fun print only id and name    #function for calling
##       print(self.id,self.name)                   #this is cls function
#-------space
#v1 = student(1,'student1',18)                     #object creation           
#v2 = student(2,'student2',18)                     #parameters 3 we have given according to constructor requirment.
#v3 = student(3,'student3',18)
#-------space
#print(v1.id,v1.name,v1.age)                          #1 student1 18
#print(v2.id,v2.name,v2.age)                          #2 student2 18         #object calling
#print(v3.id,v3.name,v3.age)                          #3 student3 18
#-----space   
##v1.print_id_name()                                  ##1 student1                                   
##v2.print_id_name()                                  ##2 student2            #object calling
##v3.print_id_name()                                  ##3 student3
#
#
#ex:-2 class student                         #class
#   def __init__(self,no,first,last,age):           #constructor(with parameters)& variables
#     self.id = no                                   #cls is defined as user defined datatype prepared for user requirement
#     self.f_name = first                            #first give cls name give constructor in that give parameters or variable
#     self.l_name = last                             #after give cls methods it works on variable
#     self.age = age                                 #after creation of object 
#-----space                                          #after that we can cl objects
#   def print_id_name(self):                        #functions in cls for printing id and name
#       print(self.id,self.name)
#------space
##   def full_name(self): 
##       print(self.f_name,self.l_name)                #function for printing full name
#------space 
#v1 = student(1,'student','s1',18)                      #object creation
#v2 = student(1,'student','s2',18) 
#v3 = student(1,'student','s3',18)
#-----space
##v1.full_name()                                               #student s1
##v2.full_name()                                               #student s2       #object calling  this shows full names
##v3.full_name()                                               #student s3
# 

#static and normal variables: 
#class
#variables / attribute. 2types of variable are available in a cls.
#methods / functions.  3types of methods are available in a cls.
#1)normal class variables(by using self key word and creating a cls is known as normal cls vaiable)(individual)
#2)static variables      (this data works on complete class)

#class student:                       #class     #by using static variable. 
#   school_name = 'xyz school'              #school name static variable. the name is common for all the objects. 
#--------space
#   def __init__(self,id,name):             #constructor normal variable
#       self.id = id
#       self.name = name
#------space
#   def show_data(self):                    #function object #by using self it used cls method. by that we can do work self variables in a cls.
#       print(self.id,self.name)
#------space
#student1 = student(1,'user1')
#student2 = student(2,'user2')
#print(student1.school_name)                                       #xyz school          stataic variable
#print(student2.school_name)                                       #xyz school
#student1.show_data()                                              #1 user1              object cl
#student2.show_data()                                              #2 user2
#     or
#student.show_data(student1)                                       #1 user1              cls name tho cl by passing obj inside().
#student.show_data(student2)                                       #2 user2

#ex:program
#class amazon:                                    #class
#    overall_discount = 5#(static variables)              #static variable
#------space
#   def __init__(self,p_id,p_name,p_price,p_discount):      #constructor         #cls variable
#       self.id = p_id                                              #by seeing that self we can conclude that we can cl by object
#       self.name = p_name                                          #parameters (or normal cls variables)
#       self.price = p_price
#       self.discount = p_discount
#----------space
#   def get_actual_price(self):             #100 - 10 - 5 = 85                 #creat a function
#       final_price = self.price - self.price*self.discount/100 - Amazon.overall_discount*self.price/100
#       return final_price
#------space
#p1 = amazon(1,'product',100,10)                       #object creating by using functions. data passing to constructure.                            
#p2 = amazon(1,'product',500,12)
#p3 = amazon(1,'product',1000,15)
#-----space
#print(p1.get_actual_price())                                          85.0
#print(p2.get_actual_price())                                          415.0            #calling a function with object.
#print(p3.get_actual_price())                                          800.0
#

#static methods and class methods:
#class:-3types
#1)variables
#2)normal variables    for accesing this we have to use normal bj use methods.
#3)static variables /class variables   for accessing cls variables we have to use static variables.(this are operated by cls methods).
##methods
#1)normal obj use methods
#2)static methods:-this will be in cls but it can perform another operations we can cl by using object name as well as cls name
#3)class methods:-is changing the discount by adding one more decarator(@) def to it. we can only cl by using cls method
#
#
#class Amazon:      #(static method)
       #class variables                              class method:-(is common for the data that working on functions)
#        overall_discount = 5
#-------space
#        def __init__(self,p_id,p_name,p_price,p_discount):         #constructor             #self will be call by using objecct name
#            self.id = p_id
#            self.name = p_name                                      #variables
#            self.price = p_price
#            self.discount = p_discount

#        def get_final_price(self):                       #function
#            return self.price - self.price*self.discount/100 - Amazon.overall_discount*self.price/100
#--------space
#        def print_data(self):                             #for printing the data we have to create a fun.
#            print('--------------')
#            print('id : ',self.id)
#            print('name : ',self.name)
#            print('final price : ',self.get_final_price())     #---------------------        calling
#-------------space                                            #id :   1
#p1 = Amazon(1,'product1',500,8)                                #name :  product           #passing the data to self.
#p2 = Amazon(2,'product2',800,11)                               #final price  : 436.0
#------space                                                   ----------------
#p1.print_data()                                                #id  : 2                          #calling the cls by object name.
#p2.print_data()                                                #name : product2
                                                                #final price  : 672.0
                                                        
###     @class method(common for whole cls)     #this is decarator @cls        #this works on the common data in the cls working on that function is known as cls method
#       def change_overall_discount(clc,discount):                    cls decoration def  (we can only cl by using cls method)
#           clc.overall_discount = discount
#
###Amazon.change_overall_discount(10)
###p1.print_data()
###p2.print_data()


#@staticmethod                     
#def print_something():                                      #static decoration def   (we can cl by using object name as well as cls name)
#    print('i am a static method')
#Amazon.print_something()                     #print function             #i am a static method                
#p1.print_something()                                                     #i am a static method              
#p2.print_something()                                                     #i am a static method


#inheritance concept:- this is one of the opps concept. objecct orriented (1)used for duplicate code remove 2)usage of existing code(we use existing code for developing our need)
#Grand father->single floor    (code re-using)
#Father-> Double floor
#you->Triple floor

#5 types in inheritnace:-
#1)single level inheritance - one parent and one child sub class
#2)multi level inheritance -A -> B -> C (this is in chain reaction)
#3)multiple inheritance - one sub class having multiple parent classes
#4)hierarchical inheritance - okate parent cls ki multiple child clses having. oka parent cls ki multiple sub clses vunte hierarchical inheritance
#A parent
#B(A)       ----u
#c(A)      z----v
#c(A)       ----x
#D(A)
#5)hybrid inheritance - combinaton of atleast two inheritance  types is called hybrid inheritance

#example:-
#class A:                                #cls
#   def __init__(self,a_value):            
#        self.a = a_value
# ---------space                                #Aclass is parent cls of B
#   def print_a(self):                           #(constructor)                           
#       print('A value : ',self.a)
#-.------space
#class B(A):        #single level                        #B is the sub cls of A. b is taking all the properities of A i.e., inheritance      
#   def __init__(self,a_value,b_value):                   #(constructor)
#       A.__init__(self,a_value)
#       self.b = b_value
#----------space
#   def print_b (self):
#    print('B value : ',self.b)
#-----------space
#obj1 = B(10,20)                          #here we are calling A class function with B class object.              
#obj1.print_a()                           #A value : 10
#obj1.print_b()                           #B value : 20

#
## ex:-1)single level inheritance:-occurs on one parent cls and one child cls. daily life ex:-
#class Driver:                      #cls                                              (driver class)
#   def __init__(self,f_name,age,mobile_no):              #constructor   (parameters passed to __init__ constructor)
#       self.f_name = f_name                              #variables    (assigning parameters to cls variables)
#       self.l_name = l_name
#       self.age = age
#       self.mobile_number = mobile_no
#
#   def full_name(self):                                                (created full name fun of driver cls){f_name}+{l_name}
#       return f'{self.f_name} {self.l_name}'
#
#class license(driver):                           (license class driver ni inheritance after we have to give parent cls at 1st). licence cls is derived by driver cls
#   def __init__(self,f_name,age,mobile_no,license_id,validity_year):                 #here we need to pass the sm parameters of driver cls. & sm parameter of license cls.
#       Driver._init__(self,f_name,l_name,age,mobile_no):                             #add driver cls paraameter in license cls.
#       self.license_id = license_id                                                  #(assigning parameters to license variables)                      
#       self.validity_year = validity_year
#
#   def is _valid_license(self):                           (functions)
#       if self.validity_year >= 2021:                     (conditional statement)
#           return True
#       else:    
#           return False
#
#user1_license = License('user','one',20,1234,101,2022)           #passing the object data,according to the parameter
#user2_license = License('user','two',22,2534,102,2021)
#                                                                                                                       
#print(user1_license.full_name())                                    #full_name function drivrer cls(parent cls).       #user one         
#print('Eligibility of licence : ',user1_license.is_valid_license()) #user_license is license cls(child cls).-          #Eligibility of license : True 

#
##2)Multi level inheritance:- if inheritance occurs between multilple clses then it says as multiple inheritance
#class Driver:                                                        #1) (driver class)
#   def __init__(self,f_name,age,mobile_no):
#       self.f_name = f_name
#       self.l_name = l_name
#       self.age = age
#       self.mobile_number = mobile_no
#--------space
#   def full_name(self):                                                   (to creat full name of driver function)
#       return f'{self.f_name} {self.l_name}'
#------space
#class license(driver):                                                  #2)   (license class driver ni inheritance after we have to give parent cls at 1st)
#   def __init__(self,f_name,age,mobile_no,license_id,validity_year):
#       Driver._init__(self,f_name,l_name,age,mobile_no):
#       self.license_id = license_id
#       self.validity_year = validity_year
#------space
#   def is_valid_license(self):                                                     (creating functions)
#       if self.validity_year >= 2021:
#           return True
#       else:    
#           return False
#--------space
#class vehical(License):                                            #3) adding all parameters of license & sm of vehical.
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):        
#       License._init_(self,f_name,l_name,age,mobile_no,license_id,validity_year)
#       self.vehical_no = vechical_no
#       self.vehical_age = vehical_age
# ----space
#   def is_valid_driver(self):                                  (function) #Vehical--->License--->Driver
#       if self.age>= 20:                                #by using dirver cls the work is reflected in vehical cls
#           return True
#       else:
#           return False
#------space
#vehical_one = vehical('user','one',21,2345,101,2022,202,2)                   #this is cls obj giving to every cls. #here we can call all clses with a single obj.
#--------space                                                                 if we given 2022                             if we given 2019
#print(Vehical_one.full_name())                                                #user one                                     #user one                                          
#print('License :',vehical_one.is_valid_license())                             #License : True                               #License : False
#print('Driver Eligible :',vehical_one.is_valid_driver())                      #Driver Eligible : True                       #Driver Eligible : True

#
##3)Multiple inheritance:-one cls ki multiple parent classes are present i.e, if we derive our cls from multiple classes is known as multiple inheritance (vehical and diesel we are used here)
##ex:-                                                                                          A -> B-> C  , MULTI LEVEL
#class A:                                                                                       A
#    def __init__(self):                                                                                     =>C    MULTIPLE INHERITANCE
#        self.a = 10                                                                            B
#-------space 
#class B:                                                                                         
#    def __init__(self):
#        self.a = 100                                                                                                   
#-------space
#class C(A,B):
#    def __init__(self):
#        A.__init__(self)                         #we need constructors  to take A B calsses (given priroity down to top)                                                                                           
#        B.__init__(self)
#        self.a = 1                
#-----space
#obj = C()
#print(obj.a)                   #1 wiii be printed if we remove that 100 will print if we remove that 10 will be printed

##class Driver:                                    #(driver class)
#   def __init__(self,f_name,age,mobile_no):
#       self.f_name = f_name
#       self.l_name = l_name
#       self.age = age
#       self.mobile_number = mobile_no
#--------space
#   def full_name(self):                                                   (to creat full name of driver function)
#       return f'{self.f_name} {self.l_name}'
#------space
#class license(driver):                             #(license class driver ni inheritance after we have to give parent cls at 1st)
#   def __init__(self,f_name,age,mobile_no,license_id,validity_year,vehical_no,vechial_age):
#       Driver._init__(self,f_name,l_name,age,mobile_no,license_id,validity_year):
#       self.license_id = license_id
#       self.validity_year = validity_year
#------space
#   def is _valid_license(self):                                                     (creating functions)
#       if self.validity_year >= 2021:
#           return True
#       else:    
#           return False
#--------space
#class vehical(License):                #vehical cls is derived from license cls
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):
#       License._init_(self,f_name,l_name,age,mobile_no,license_id,validity_year)
#       self.vehical_no = vechical_no
#       self.vehical_age = vehical_age
# ----space
#   def is_valid_driver(self):                                  (function)
#       if self.age>= 20:  
#           return True
#       else:
#           return False
#class Petrol:                       #cls only store  price
#   def_init__(self,price):
#       self.price = price
#--------space
#class Diesel:                      #cls only store  price
#   def __init__(self,price):
#       self.price = price
#------space
##multiple inheritance(vehicle and diesel)
#class Bus(Vehical Diesel):                 #cls this id derived from 2 classes(Vehical,Diesel).                  we can use multiple vehicals once we written he code while changing the vehical we can get
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age,price,wheels):   #Here we pass vehical cls parameters & this cls parameter.    
#       vehical.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age)         #vehical parameter
#       Diesel.__init__(self,price)                                                                                #Diesel parameter.
#       self.wheels = wheels                                                                                       #Vehical Diesel
#------space
#bus = Bus('user','one',21,2345,101,2022,201,2,100,6)                #object creation
#------space-          we can call every cls and we get data.
#print('driver name :',bus.full_name())                                              #driver name : user one
#print('license valid :',bus.is_valid_license())                                     #license valid : True
#print('driver eligible :',bus.is_valid_driver())                                    #driver eligible : True
#print('price of fuel per liter :',bus.price)                                        #price of fuel per liter :100

#
##4)Hirarchical and 5)Hybrid inheritance:-oka cls ni multiple class derive chesukodam 
#A parent
#B(A)                   oka parent cls ki multiple child having is called hierarchical inheritance
#C(A)
#D(A)
##class Driver:                                                         (driver class)
#   def __init__(self,f_name,age,mobile_no):
#       self.f_name = f_name
#       self.l_name = l_name
#       self.age = age
#       self.mobile_number = mobile_no
#--------space
#   def full_name(self):                                                   (to creat full name of driver function)
#       return f'{self.f_name} {self.l_name}'
#------space
#class license(driver):                                                     (license class driver ni inheritance after we have to give parent cls at 1st)
#   def __init__(self,f_name,age,mobile_no,license_id,validity_year):
#       Driver._init__(self,f_name,l_name,age,mobile_no,license_id,validity_year):
#       self.license_id = license_id
#       self.validity_year = validity_year
#------space
#   def is _valid_license(self):                                                     (creating functions)
#       if self.validity_year >= 2021:
#           return True
#       else:    
#           return False
#--------space
#class vehical(License):
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):
#       License._init_(self,f_name,l_name,age,mobile_no,license_id,validity_year)
#       self.vehical_no = vechical_no
#       self.vehical_age = vehical_age
# ----space
#   def is_valid_driver(self):                                  (function)
#       if self.age>= 20:  
#           return True
#       else:
#           return False
#class Petrol:
#   def_init__(self,price):
#       self.price = price
#--------space
#class Diesel:
#   def __init__(self,price):
#       self.price = price
#------space
##multiple inheritance  (here vehicle ki bus,lary,bike (one parent cls many child cls))          
#class Bus(Vehical,Diesel):                                                                                                we can use multiple vehicals once we written he code while changing the vehical we can get
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age,price,wheels):
#       vehical.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age)
#       Diesel.__init__(self,price)
#       self.wheels = wheels
#-------space
#class lary(Vehical,Diesel):
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age,price,wheels):
#       vehical.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age)
#       Diesel.__init__(self,price)
#       self.wheels = wheels
#---------space
#class bike(Vehical,petrol):
#-   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age,price,wheels):
#       vehical.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age)
#       Diesel.__init__(self,price)
#       self.wheels = wheels
#------space
#bus = Bus('user','one',21,2345,101,2022,201,2,100,6)
#------space
#print('driver name :',bus.full_name())                                              #driver name : user one
#print('license valid : ',bus.is_valid_license())                                    #license valid : True
#print('driver eligible :',bus.is_valid_driver())                                    #driver eligible : True
#print('price of fuel per liter :',bus.price)                                        #price of fuel per liter :100
#
#hierarchical inheritance:
#parent : vehical
#sub : bus , larry

##multiple:
#parent : vehical,diesel
#sub : bus
#
#hibrid inheritance:
#combination of atleast two inheritance type is called hybrid inherintance
#(we use code once agian existing code but we can't repeat code for this reason inheritance is very powerful



##polymorphism:-it refers to the use of a single type entity different ways.(is one of the oops concept):-different ways 1)method overloading(function name is same but handling different data by polymorphism.1)) 2)method overriding
#1)Method overloading:(this can handel different no.of parameters and different type of data)    single function usedd in different ways.
#def add(a,b,c=0,d=0,e=0):           #default values        (function)
#   ans = a+b+c+d+e
#   print('answer : ',ans)
#-----space
#add(2,3)                                #answer : 5
#add(2,3,4)                              #answer : 9  
#add(2,3,4,5)                            #answer : 14
#add(2,3,4,5,6)                          #answer : 20
#
#l = [1,2,3,4]                                                    
#s = "hello world!"
#print(len(l))                           #4 (calculating each character)    #sm function but different data handled by using polymorphism. 
#print(len(s))                           #12(calculating world into 1 character)
#
#Method overriding-polymorphism(used by inheritance concept):in sm cls this method will take from last rewritten code
#class father:
#   def __init__(self):
#       pass
#-------space
#   def __height(self):
#       print('Height : ',5.7)
#-------space
#   def Education(self):
#       print('Educatin : ', 'Degree')
#--------space
#   def last_name(self):
#       print('Last Name : xyz')
#class Son(Father):
#   def __init_(self):
#       father._init__(self):
#-----space
#   def __Height(self):
#       print(Height : ',5.11)
#-------space
#   def Education(self):
#       print('Education : ','Engineering')
#father = Father()
#son = Son()
#
#son.Height()                          #Height : 5.11                  this comes by overriiding method   
#son.Education()                       #Education : Engineering
#son.Last_name()                       #Last Name : xyz                taken from Fathercls
#---------
#father = Father()                      
#father.Height()                       #Height : 5.7
#father.Education()                    #Eduction : Degree
#father.last_name()                    #Last Name : xyz
#
#ex:-this method is used in        (over ride)
#class A:
#   def __init__(self,a,b):
#       self.a = a
#       self.b = b
#-------space
#   def __str__(self):                                   #(without this statement memory will be printed)
#       return f'{self.a} -- {self.b}'
#----------space
#obj = A(10,20)                                          #overriding concept  
#print(obj)                                              #10 -- 20

#
#operator overloading:- is a type of polymorphism
#+ => __add__
#- => __sub__
#* => __mul__                   #opertations
#> => __gt__
#< => __lt__
#class A:
#   def __init__(self,a):
#       self.a = a
#--------space
#   def __add__(self,other):
#       return A(self.a + other.a)
#-------space
#obj1 = A(10)
#obj2 = A(20)
#-----space
#print(obj1+obj2)                                   
#print(obj3)                               #This will show the memory location of the data
#print(obj3.a)                             #30
#
#class A:
#   def __init__(self,a):
#       self.a = a
#--------space
#   def __add__(self,other):
#       return A(self.a + other.a)
#-------space
#   def __lt__(self,other):
#       if self.a < other.a:
#           return True                                #True
#       else:
#           return False
#--------space
#   def__gt__(self,other):
#       if self.a > other.a:
#           return True
#       else:
#           return False                               #False
#
#obj1 = A(10)
#obj2 = A(20)
#-----space
#obj3 = obj1 + obj2
#print(obj3)                                    #30                                                                          
#print(obj3.a)                                  #here we get address of obj and new obj created and new obj printed 30 this is for addition operation
#print(obj1<obj2)                               #true
#print(obj1>obj2)                               #false

#
#Encapsulation:- (imp concept in oops in python) is the process of combining attributes and methods with in the class.is used for protection the data.
#Data protection 
#public
#private                   #__a means private
#       only class methods and inside the class
#protected                  #_protected   
#       inside class + its subclass

#class A:                     #private         #cls
#   def __init__(self,a,d):
#       self.__a = a #private
#       self.__b = b #private
#------------space
#   def show_data(self):
#       print('a : ',self.__a)
#       print('b : ',self.__b)
#---------space
#obj1 = A(10,20)                                              #a : 10      only we can access from cls
#obj1.show_data()                                             #b : 20         print(obj1.__a)we cant access from outside.
#

#class A:                      #protected
#   def __init__(self):
#       self._a = 10  #protected
#       self._b = 20  #protected
#-------space
#class B(A):
#   def __init__(self):
#       A.__init__(self)
#-------space
#   def show_data (self):
#       print('a : ',self._a)
#       print('b : ',self._b)
#obj = B()                                        #a : 10
#obj.show_data()                                  #b : 20

#
#Abstraction in python:-(is one of the oops retailed concept. at 1st we create one cls that gives us one structure (or) plan by using that  we creat multiple classes)(we cant create obj to abstruct cls)
#
#from abc #(module) import ABC #(cls),abstractmethod in this we have both abstract methodss and normal methods. in this we have structure and code but we cant creat object.
#------space
#class polygon(ABC):           #we create a cls that is derived from abstract method. in this we wont use init method. we use @abstract method.in abstract cls is empty cls.then after create a base cls or constructor. after create a sides init def

#from abc import ABC,abstractmethod                    #abc(abstract base class)     #abstractmethod(is a decorator)   abstraction gives structure by using that we can implement. 
#class polygon(ABC):
#--------space
#   @abstractmethod
#   def no_of_sides(self):
#       pass
#----------space
#class Triangle(polygon):
#   def __init__(self):
#       pass
#---------space
#   def no_of_sides(self):
#       print('I have 3 sides')
#=-------space
#class Rectangle(polygon):
#   def __init__(self):
#       pass
#---------space
#   def no_of_sides(self):
#       print('I have 4 sides')
#--------space
#obj1 = Triangle()
#obj2 = Rectangle()
#obj1.no_of_sides()                                   #I have 3 sides
#obj2.no_of_sides()                                   #I have 4 sides         #abstruction it givws structure by using that we create sub classes and we impliment our code

#
#List comprehension:-it is a type of method of creation of list (shortly)
#before this list comperhension we done by like this:
#l = [1,2,3,4,5,6]
#new = []
#for i in range(0,len(l)):
#   new.append(l[i]*5)
#print(new)         
#                                    #[5, 10, 15, 20, 25, 30]
#        #with comprehenstion
#after coming list comperhension we done by like this: this method using with for loop
#l = [1,2,3,4,5,6]
#new_list = [x*5 for x in l]
#print(new_list)                     #[5,10,15,20,25,30] came sm output but the list of code is less compared to previous method


#list comprehenstion and for loop and if condition:
#even_list = [x for x in range(20) if x%2 == 0]
#odd_list = [x for x in range(20) if x%2 == 1]
#print(even_list)                                          #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18] this code will print 1 to 20 even nmbrs by using if condition
#print(odd_list)                                           #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] this code will print 1 to 20 odd nmbrs by using if condition

#x =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#y = [] 
#z = []
#for i in  x:
#    if i %2 == 0:
#        y.append(i)
#    else:
#        z.append(i)
#print(y)              #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18] this code will print 1 to 20 odd nmbrs by using if condition
#print(z)              #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] this code will print 1 to 20 odd nmbrs by using if condition

#
#Lambda functions in python:- this is single line function. only present in python. we cant add no of codes in it. we can only return one operation (a+b) (a*b) (a-b). simple way to writting the functions
#normal function:we can add n lines of codes in one function.  (a+b),(a*b),(a-b)
#
#def function1(a,b):
#   return a+b                                    #5
#   sub = a-b                                     #-1
#print(hello)                                     #hello
#print(function1(2,3))                            #5 #(normal function(in this function we can write multiple operations))
#
#lambda function:                           #(in this we can only do one operation)(this mostly used in (map function or iteratable ))
#x = lambda a,b : a+b
#print(x(1,2))                                      #3 here we can parameters then sm value  returned

#l = [1,2,3,4,5,6] 
#multiple_ten = lambda a : a*10
#print(list(map(multiple_ten,1)))                    #[10,20,30,40,50,60] lambda function this returns with map object. 

#l = [1,2,3,4,5,6]
#m = []
#for i in range(0,len(l)):
#    m.append(l[i]*10)
#print(m)                      #[10, 20, 30, 40, 50, 60]by using for loop


#Threadingin python:-to decrease the tym to run the multiple codes. we have to use threadings 
#import time                                   #this time module
#print(time.time())                            #1668579707.751314 #this shows the time in secs

##without using threading concept:
#import time
#
#def calc_square(numbers):                                                #square number :
#    print('square number :')                                             #square : 1
#    for number in numbers:                                               #square : 4
#        time.sleep(0.2)                                                  #square : 9 
#        print('square : ',number*number)                                 #square : 16
#                                                                         #square : 25
#def calc_cube(numbers):                                                  #cube number :z
#    print('cube number :')                                               #cube : 1
#     for number in numbers:                                              #cube : 8
#        time.sleep(0.2)                                                  #cube : 27
#        print('cube : ',number*number*number)                            #cube : 64
#initial_time = time.time()                                               #cube : 125 
#l = [1,2,3,4,5]                                                          #timetaken : 2.058202028274536 #this program running ki 2min thisukundhi without using threading
#calc_square(l)
#calc_cube(l)
#print('time taken : ',time.time()-initial_time)


##with using threading concept:-
#import threading                                       #(this is inbuilt module in python)                                    
#import time                                            #(time module)

#def calc_square(numbers):                                                #square number :
#    print('square number :')                                             #cube number :
#    for number in numbers:                                               #cube :1
#        time.sleep(0.2)                                                  #square : 1 
#        print('square : ',number*number)                                 #square : 4
#                                                                         #cube : 8
#def calc_cube(numbers):                                                  #square : 9
#    print('cube number :')                                               #cube : 27
#    for number in numbers:                                               #square : 16
#        time.sleep(0.2)                                                  #cube : 64
#        print('cube : ',number*number*number)                            #cube : 125
#initial_time = time.time()                                               #cube : 15 
#l = [1,2,3,4,5]                                                          #Time taken : 1.0433464050292968          ##this program running ki 1min thisukundhi with using threading the codes are running parallel.
#                                                                         
#t1 = threading.Thread(target =calc_square,args =(l,))                    
#t2 = threading.Thread(target =calc_cube,args=(l,))                      
#                                                                         
#t1.start()                                                               
#t2.start()
#
#t1.join()
#t2.join()
#                                                     
#print('Time taken : ',time.time()-initial_time)              #threaders are printed simultaneously by using threading module 

#
#Decorators in python:-
#def login_required(f1):                                      #Decorators 
#    def inner(name,is_login):                                #function inside one more funnction creating with same parameters
#        if is_login ==False:
#            print('Kindly Login!')
#            return
#        return f1(name,is_login)
#    return inner         
#
#@login_required 
#def home(name,is_login):
#    print('welcome to home page of our website!') 
#
#@login_required 
#def orders(name,is_login):
#    print('welcome to orders page of our website')
#
#def about():
#    print('welcome to about section of our website')
#
#home('user',False)                                     #Kindly Login!                 #calling
#orders('user',True)                                    #welcome to orders page of our website
#about() 
#                                               #welcome to about section of our website
#
#Generators in python: sm like functions which contain yield keyword. in this we dont use return statements.(multiple values) retuned here we use yield statement instead of return statement avthye
#def f2():                                                          #1 #0
#   for i in range(10):                                             #2
#       yield i                                                     #3
#                                                                   #4
#result = f2()                                                      #5
#                                                                   #6 
#for value in result:                                               #7
#   print(value)                                                    #8
#        (or) we can access in both forms                           #9
#
#print(result.__next__())                                           #0       
#print(result.__next__())                                           #1    #in this only 4 nmbrs are printed
#print(result.__next__())                                           #2 
#print(result.__next__())                                           #3

# 
#Exception Handling in python:-errors 1)compile time error,(this shows indentation errors) 2)run time error(exception handling)this we have to do code lo thapu vunte chupisthadhi
#1)compiler error            (code time error)   #run time error  (logic error)
#if True:          by using compiler                                    #if True
#print('hello')     we can get indentation errors                       #print('hello')

#2)run time  error (or) exception handling
#a = int(input('Enter a value:'))                          #4             #2
#b =  int(input('Enter b value:'))                         #5             #0
#d = a/b                                                   #0.8           #zeroDivisionError  (shows run time error)
#print('Answer : ',d)                                                     #here the program will be stopped the Hello world code will not be printed
#try:                                                         #by using thi try and except the remaining code will be runned        
#   d = a/b                                                   #2
#except:                                                      #0       
#   print('May be Invalid input')                             #May be Invalid input   
#print('Hello world!')                                        #Hello world!
#
##try:#the code which might throw error     (this is error handling )
##except:#handling the error                (by using this the code will be continued wether the erroe occur or not occur )
##finally:#no matter what this block will excute   

#try:                                                                 #Enter a value :4
#   a = int(input('Enter a value:'))                                  #Enter a value :2
#   b = int(input('Enter b value:'))                                  #division : 2.0
#   c = a/b                                                           #I am finally block, i donot care any one
#   print('division : ',c)
#except:                                                              #Enter a value :4    
#   print('Denominator cannot be Zero')                               #Enter a value :0
#finally:                                                             #denominator cannot be zero 
#print('I am finally block, i donot care any one')                    #I am finally block, i donnot care any one

#
#file handling in python:-1)writting data to the file 2)reading data from the file 3)appending data to the file
#reading - r                        #key
#write - w                          #key
#append -a                          #key 
#reading and writing - r+           #key
##creating a file and writing something init
#f = open('my_file.txt','w')       #(this creates file and write)
#-----space
#f.write('This is my first file\nThis is my file\n')                        #\n=creates new line
#f.write('I am the subscriber of peoples vybe')                             #(in file)This is my first file
#                                                                           #This is my file
#                                                                           #I am the subscriber of peoples vybe
#f.close()
#print ('Data is saved to file SuccessFully!')                            #Data is saved to file successfully!   (the file will be created and data will be saved)     
#
#writing and appending                                                     #(in file)This is my first file
#f = open('my_file.txt','a')                                               #This is my file                               
#f.write('\nHello world!')                                                 #I am the subscriber of peoples vybe
#f.close()                                                                 #Hello world!
#print('Data is saved to file SuccessFully!')                              ##Data is saved to file successfully! 
#reading the data in the file:
#try:
#   f = open('my_file.txt','n')
#   print(f.read())
#except:
#   print("file name does not exist")                                     #file name does not exist  
#
#
#
#
#st = "sagar"
#print(st)                      #sagar     
#print(st[0])                  #s
#print(st.replace("s", "H"))
#print(st)                    #Hagar
#name = "youtube"
#print('my ' + name[3:7])    #my tube                    
#
#name = 'youtube'
#print(name , ' rocks')       #youtube  rocks
#print(name + ' rocks')       #youtube  rocks
#




#python:-Guido van russov:-  bought this to build python.
#Functional programming from c
#OOPs from c++
#Scripting langagues Features from perl and shell script
#Modular Programming features from Module-3

numeric=int,float,complex,bool       sequence=list,tuple,set,string,Range
#telusuko(python) python Interpreter. IDE-Integrated Development Environment(easy to debug).  High level programming. easy to learn. 
#Arithmetic operators(+ - * % / // )
#Assignment operators:-(=)
#Relational operators:-(== , =<, =, !=, )
#Logical operators:-(and or not)
#unary operators:-(1-1)
#bitwise operator:-compliment(~) & | ^ << >>

#Arthmatic Operator:-(+ - * % / // )
       
#a =10           
#b=20                                #30
#print(a+b)
#print(2 + 3)                         #5
#print(9 - 8)                          #1
#print(4 * 6)                         #24
#print(8 / 4)                         #2.0#float
#print(5 / 2)                         #2.5
#print(5 // 2)                        #2#intger_division.
#print(8 + 2 * 3)                     #14  #This uses Bodmas(brackers,Orders,Divide,Multiple,Add,Subtract)
#print(8 + 2)*3                      #30
#print(2 * 2* 2)                     #8
#print(2 ** 3)                        #8
#print(10 * 'sagar')                  #will print 10 times sagar
#print(10 / 3)                        #3.3333333333333335
#print(10 // 3)                       #3   (quataiont)
#print(10 % 3)                        #1    (remainder)

#print('sagar')                       #sagar
#print("sagar's laptop")              #sagar's laptop
#print('sagar "laptop"')              #sagar "laptop"
#print('sagar\'s "laptop"')           #sagar's "laptop"
#print('sagar' + 'sagar')             #sagarsagar
#print(10 * 'sagar')                  #sagarsagarsagarsagarsagarsagarsagarsagarsagarsagar
#print('c:\docs\sagar')               #c:\docs\sagar
#print(r'c:\docs\sagar')              #c:\docs\sagar

"""
"""
#variables
a = 10
b = 20 
print(a+b)                           #30
print(10 + 20)                       #30
x = 20
print(x + 30)                        #50
y = 30
print(y + 20)                        #50
x = 9
print(x + y)                         #39
y = 1
print(x + y)                         #10
print(x + 10)                        #19
name = ('sagar')
print(name)                          #sagar
name = ('sagar+ragas')
print(name)                          #sagar+ragas
name = ('sagar')
print(name[0])                       #s
name = ('sagar')
print(name[4])                       #r
name = ('sagar')
print(name[-1])                      #r
name = ('sagar')
print(name[-5])                      #s
name = ('sagar')
print(name[0:4])                      #saga
name = ('sagar')
print(name[0:])                      #sagar
name = ('sagar')
print(name[:4])                      #saga
name = ('sagar')
print(name[0:9])                      #sagar
name = ('sagar')
print(len(name))                      #5

none,numeric(int,float,complex),list[],tuple(),set{},string"",range(2,10,2),dictionary{'key':'value'}


#list[] adding different values ex:strings+numbers group. them together we can add,remove,update values. we can change values 
nums = [1,2,4,6,77,88]
print(nums)                      #(1, 2, 4, 6, 77, 88)
print(nums[2])                   #4
print(nums[1:])                  #(2, 4, 6, 77, 88)
print(nums[-2])                  #77

names = ['sagar', 'ram', 'raj']
print(names)                       #['sagar', 'ram', 'raj']

mil = [names, nums]                       
print(mil)                         #[['sagar', 'ram', 'raj'], [1, 2, 4, 6, 77, 88]]

nums = [1,2,3,4,5,66,77,88]
nums.append(99)                   #print at last
print(nums)                       #[1, 2, 3, 4, 5, 66, 77, 88, 99]
nums.insert(2,99)                 #print at indexed point
print(nums)                       #[1, 2, 99, 3, 4, 5, 66, 77, 88, 99]
nums.remove(4)                    #removed by number
print(nums)                       #[1, 2, 99, 3, 5, 66, 77, 88, 99]
nums.pop(2)                        #deleting the index number by using pop function
print(nums)                       #[1, 2, 3, 5, 66, 77, 88, 99]
nums.pop()                        #the last number dlted
print(nums)                       #[1, 2, 3, 5, 66, 77, 88]
del nums[2:]                      #all dlted expect 2 numbers
print(nums)                       #[1, 2]
nums.extend([12,34,56,78,90])     #add multiple values   
print(nums)                       #[1, 2, 12, 34, 56, 78, 90]
print (min (nums))                #1
print (max(nums))                 #90
print (sum(nums))                #273
print(sorted(nums))              #[1, 2, 12, 34, 56, 78, 90]   


#tuple() & sets 
tup = (1,2,3,4,5,6,7)                 #sm like list but tupple we cant change the values
print (tup)                           #(1, 2, 3, 4, 5, 6, 7)
print (tup[1])                        #2
print (tup[5])                        #6
s = {22,25,14,21,5}                   #sm like list sets cant printed by sequence and not duplicate {} collection of unique nmbrs. indexing not supported we cant add by using index in sets.
print (s)                             #{5, 21, 22, 25, 14}
r = {22,88,99,77,66,77,66}
print (r)                             #{66, 99, 22, 88, 77}


#dictionary     it consists key and values {}
data = {1: 'sagar', 2: 'ravi', 3: 'ragas'}
print (data[2])                       #ravi
print (data[3])                       #ragas
print (data.get(1))                   #sagar
print (data.get(4))                   #None
print (data.get(3,'not found'))       #ragas
print (data.get(4,'not found'))       #not found
keys = ['sagar','ragas','ram']
values =['python','java','js']
data = dict(zip(keys,values))         #{'sagar': 'python', 'ragas': 'java', 'ram': 'js'}
print (data) 
print (data['sagar'])                 #python  
data ['monu']  ='cs'
print (data)                          #{'sagar': 'python', 'ragas': 'java', 'ram': 'js', 'monu': 'cs'}
del data ['ram'] 
print (data)                          #{'sagar': 'python', 'ragas': 'java', 'monu': 'cs'}
prog = {'js':'atom', 'cs':'vs','python':['pycharm','sublime',],'java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print (prog)                #{'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'sublime'], 'java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
print (prog['js'])          #atom
print (prog['python'])      #['pycharm', 'sublime']
print (prog['python'][1])      #sublime
print (prog['java']['JEE'])    #Eclipse

#more on variables in python:
nmbr = 5
print (id(nmbr))              #2664230093168
name = 'sagar'
print (id(name))              #2375962948656
a = 10
b = a
print (a)                     #10
print (b)                     #10
print (id(a))                 #1565290136080   if same date present in multiple variables that point to only one box here a and b
print (id(b))                 #1565290136080
print(id(10))                 #1565290136080            
k = 10
print (id(k))                 #1565290136080 
a = 9
print (id(a))                 #1936330195440
"""
#when we have data in your memory which will not be used or taged by any variable collected by garbage collector

#numeric=int,float,complex,bool       sequence=list,tuple,set,string,Range

"""
print(range(1,11))                      this will print 1 to 10 numbers
print(list(range(11)))                  #this will print [0 to 10] numbers in list order.
print(list(range(2,12,2)))              #this will print [2,4,6,8,10]. even numbers.
print(list(range(1,12,1)))              #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


for i in range (1,101):                 #1 to 100 will be printed
    print(i)
for i in range (1,101):                 #even nmbrs 1 to 100 printed
    if i%2 == 0:  
        print (i) 
for i in range (1,101):                 #odd nmbrs 1 to 100 printed
    if i%2 != 0:
        print (i)        

even = []
odd = []
for i in range (1,100):
    if i%2 != 0:
        odd.append(i)
    else:
        even.append(i)

print("Even numbers are: ",even)
print()                                                 #odd nmbrs printed 1 to 100
print("Odd numbers are :",odd)

even = []
odd = []
for i in range (1,100):
    if i%2 == 0:
        odd.append(i)
    else:
        even.append(i)

print("Even numbers are: ",even)
print()                                                #even nmbrs printed 1 to 100
print("Odd numbers are :",odd)


#print (0.1 + 0.2 == 0.30000000000000004)          #True
#print (0.1 + 0.2 == 0.3)                          #false

#Binary:-(base2)0 - 1   bin(25) we get binary value '0b11001'
#Decimal:-(base10)0 - 9  0b0101 we get decimal value '5'
#Octal:-(base8)0 - 7  0ct(25)  this will give octal of number '0o31'
#Hexa Decimal:-(base16)0 -9 a -f   hex(25)  '0x19'

import math              print(math.floor(2.9))#2   print(math.floor(2.2))#3  print(math.pi) print(math.e)  import math as m m.sqrt(25)#5.0
import random
from random import* 

#many use of using IDE(Integreated Development Environment) is Debugging purpose.

x = int(input("enter a value: "))
y = int(input("enter a value: "))
z =(x+y)    
print(x+y) #20
print(z)     #20

#if,elif,else,nested if (this are blocks)
x=8
if x%2==0:
    print("even")
else:
    print("odd")

n = 2
if (n==1):
    print("one")
elif (n==2):
    print("Two")
elif (n==3):
    print("Three")
else:
    print("wrong input")

k = 8
if k % 2 ==0:
    print("Even")
    if k > 5:
        print("Great")
    else:
        print("Not so grt")
else:
    print("odd")


#while loop is used for itteration & condition.
i = 1                #initialization
while i<=5:          #condition
    print("python")
    i=i+1                #increment/decrement. #python printed 5times

ran = "python"
for i in ran:            #python
    print(i,end="")

ran ="python"
d = ran 
for i in range(5):              #python will be printed 5times
    print(d)   

rac ="python"
j = 1
for i in rac:
    while j <= 5:
        print(rac)
        j= j+1                  #python will be printed 5times

   
i = 1                        
while i<=5:
    print("sagar",end=" ")
    j = 1
    while j<=4:
        print("python",end=" ")
        j=j+1
    i = i+1 
    print()                #sagar python python python python 5times printed.
 
#for loop works on range & sequence:
k = [1,2,'sagar','python']      #1
for i in k:                     #2
    print(i)                    #sagar

x ='python'               #p
for i in x:               #y
    print(i)              #t

for i in range(10):      #0,9 printed
    print(i)

#break,contiue,pass:-
av = 5                                               
x=int(input("How many candies you want? "))             #4                 #10
i = 1                                                   #canndy 4 times    #canndy 5times
while i <= x:                                           #bye               #out of stock
    if i>av:                                                               #bye
        print("out of stock")
        break
    print("canndy")
    i=i+1

print("bye")

for i in range(1,10):
    if i % 3 == 0:
        continue
    print(i)        #1 2 4 5 7 8


#printing pattern:-
for i in range(4):             ## # # #        #           # # # #
    for j in range(4):         ## # # #   #4+1 # #   #4-1  # # # 
        print('#',end=' ')     ## # # #        # # #       # #
    print()                    ## # # #        # # # #     #


#for else:
nums = [1,5,10,26,27,28]
for num in nums:
    if num % 5 == 0:
        print(num)              #5 10
        break                   #5 only one iteration done 5 printed
else:
    print("number not found")           #else used for for loop. 


#prime numbers:-
n = int(input("enter a value: "))
for i in range(2,n):
    if n % i == 0: 
        print("not prime")          #22 not prime
        break
else:
    print("prime")                             #7 primme

#Array in python:-
from array import*         #this shows the address and list size of the given variable.  
val = array('i',[5,9,-8,4])
print(val.buffer_info())     #(2014286463424, 4)    address and list size


#Array values from user in python:-In this we need to have all the values in same data type.(int)(float). we can shirnk easily.
from array import*
vals = array('i',[5,9,8,-4,2])     #for int            ('u'['a','e','i'])  #for unicode
print(vals)                  #array('i', [5, 9, 8, 4, 2])   i allows +int and -int.  I only allows +int 
print(vals.buffer_info())    #(1977577159792, 5) address and size
print(vals.typecode)         #i
vals.reverse()
print(vals)                   #array('i', [2, -4, 8, 9, 5])
print(vals[0])                #2
for i in range(5):                 #or (len(vals))  (vals)
    print(vals[i])             #this will print step by step of data.

#Array values from user:-
from array import*
arr = array('i',[])         
n= int(input("enter the len of array: "))        #4
for i in range(n):
    x = int(input("Enter the next value"))       #11 2 3 34
    arr.append(x)
print(arr)                                   #array('i', [11, 2, 3, 34])
 
from numpy import*           #if we want to perform certain multi dimensional or sentific calculation we have to install numpy package.    #python -m pip install numpy
arr = array([1,2,3,4,5])
print(arr)                     #[1 2 3 4 5]  


from numpy import*
arr = array([1,2,3,4,5])
arr = arr+5
print(arr)        #[ 6  7  8  9 10]

#Function creation and calling functin:-each task is defined as function because of reuseability.
def python():            #fun python name, without parameter values without return value.
    print("Hello")       #Hello
    print("world")       #world
python()                 #fun call

def add(x,y):
    c = x+y
    print(c)
add(6,8)             #14

def addi(u,v):
    c = u+v
    return c
result = add(5,9)
print(result)          #14  fun with  para and return value.

#function Arguments:-Types of arguments
def person(name,age):
    print(name)
    print(age)
person('sagar',24)        #sagar 24

def sum(a,*b):
    c = a
    for i in b:
        c = c + i
    print(c)
sum(5,6,7,89,78)       #185

def person(name, **data):
    print(name)
    print(data)
person('sagar', age=24, city='hyd', mob=89774758)                #{'age': 24, 'city': 'hyd', 'mob': 89774758}
"""

#corey schafer pyton:- 
#python --version (for checkin py version)
#s = 'bobby\'s world'        or   "bobby's world"
#print(s)              #bobby's world
#s = 'hello world'
#print(s[0:5])       #hello   
#print(s.lower())
#print(s.upper())
#print(s.('l'))   #3
#print(s.find('world))   #6
#new_s = s.replace('world','universe')
#print(new_s)            world replaced by universe
#greeting = 'hello'
#name = 'ragas'
#message = greting + ',' + name + '.welcom!'    or    message = f'{greeting}, {name}. welcome!'
#print(massage)    #hello, ragas. welcome!
#num = 1
#num = num + 1 #2     (or)  num += 1 #2      num *= 10  #10
#print(num)    #2
#print(round(3.75))     #4      print(round(3.75,1)    #3.8
#1)arithmetic operators 2)comparsions operatores 
#num_1 = '100'
#num_2 = '200'
#num_1 = int(num_1)
#num_2 = int(num_2)
#print(num_1 + num_2)               #300
#list a = ['history',1,2,4,'maths']
#print(a)         -#['history',1,2,4,'maths']
#print(a[1])       #1
#print(a[-1])      #maths
#print(a[0:2])     #['history',1]  or print(a[:2])     #['history',1]
#print(a[:3])      #[4,'maths']      #this slicing
#a.append('art')                                            #adding the normal elements
#print(a)         #['history',1,2,4,'maths','art']
#a.insert(0,'art')
#print(a)         #['art','history',1,2,4,'maths','art']
#a1 =['student','teacher']
#a.extend(a1)                                               #adding multiple values
#print(a)            #['history',1,2,4,'maths','student','teacher']       
#a.remove('maths)     #maths removed from list
#popped = a.pop()              #this remove last value
#print(popped)          #this will shhows the popped value
#a.reverse()         #show in revers
#a.sort()            #show by ascending order
#a.sort(reverse=True) #show the descending order
#print(max(a))
#print(min(a))
#print(sum(a))
#print(a.index('art'))       #0
#print('maths' in a)         #True
#for a in (courses)
#  print(course)       #history
#                      #maths
#for index, a in enumerate(courses):
#   print(index,course,start):     #1  history
#                                  #4  maths
#a_str =' - '.join(a)
#   print(a_str)                #history - 1 - 2 - 4 - maths 
#new_list =a_str.split(' _ ')
#   print(new_list)              #['history',1,2,4,'maths']
#mutable:-
#list1 = ['history',1,2,4,'maths']
#list2 = list1
#print(list1)    #['history',1,2,4,'maths']
#print(list2)    #['history',1,2,4,'maths']
#list1[0] = 'art'
#print(list1)     #['art','history',1,2,4,'maths']
#print(list2)     #['art','history',1,2,4,'maths']
#tuple:()
#immutable
#sets:{} un oreder,sortedd by itself
#a = {'art','history',1,2,4,'maths'}
#a1 = {'art','history','maths'}
#print(a.intersection(a1))              #{'art','history','maths'}
#print(a.differences(a1))               #{1,2,4}
#print(a.union(a1))                     #this shows everything
#empty a = []    #list
#empty a = ()    #tuple
#empty a = {}    #sets
#Dictioneries:key value pairs {} we can add we can update
#student = {'name':'John','age':25,'courses':['maths',compsci']}
#print(student['name'])               #john
#print(student.get('name'))           #john
#student['phone'] = '555-555'
#print(student)                   #student = {'name':'John','age':25,'courses':['maths',compsci'],'phone: '555-555'}
#student.update({'name':'Jane','age':26,'phone: '555-555'}
#print(student)                   #student = {'name':'Jane','age':26,'courses':['maths',compsci'],'phone: '555-555'}
#del student['age']            #this will delete age from list
#age = student.pop('age)                #this will pop the age in list
#print(len(student))              #4
#print(student.keys())            #this will print 4 keys
#print(student.values())          #this will print 4 values
#print(student.items())           #this will print the all dictionry
#for key, value in student.items():
#   print(key, value)                      #this will print the key values
#
#conditionals and booleans:
#lang = 'py'
#if lang == 'py':
#   print('True') 
#elif lang == 'Java':
#   print('Java') 
#elif lang == 'Javascript':
#   print('Javascript')         
#else:
#   print('false')             #True 
#
#user = 'Admin'              #and
#logged_in = True
#if user == 'Admin' and logged_in:
#   print('Admin page')
#else:
#   print('Bad creds')                        #Admin page
#user = 'Admin'
#logged_in = false
#if user == 'Admin' and logged_in:
#   print('Admin page')
#else:
#   print('Bad creds')                        #bad creds
#
#user = 'Admin'                 #or
#logged_in = False
#if user == 'Admin' or logged_in:
#   print('Admin page')
#else:
#   print('Bad creds')                        #Admin page
#
#user = 'Admin'
#logged_in = False
#if not logged_in:
#   print('please log In')
#else:
#   print('Welcome')                   #Please log In
#
#a = [1,2,3]
#b = [1,2,3]
#print(a == b)            #True
#print(a is b)      #False
#print(id(a))             #this show the storage no
#print(id(b))             #this stow the storage no
#
#condition = 0
#if condition:
#   print('Evaluated to True')
#else:
#   print('Evaluated to False')        #False
##condition = 10
#if condition:
#   print('Evaluated to True')
#else:
#   print('Evaluated to False')        #True
#
#loops and iterations:-
#nums = [1,2,3,4,5]
#for num in nums
#   if num == 3:
#       print('Found!')             #1
#       break                       #2
#print(num)                         #Found!
#nums = [1,2,3,4,5]
#for num in nums                    #1
#   if num == 3:                    #2
#       print('Found!')             #Found!
#       continue                    #4
#print(num)                         #5
#for i in ramnge(10):
#   print(i)               #this will print 1 to 9                         
#x = 0
#while x < 10:
#   print(x)
#   x += 1            #this will print 1 to 9
#while x < 10:        #or      while True:
#   if x == 5:
#       break
#   print(x)
#   x +=1            #this will break automatically on 5 print 1 to 4
#
#functions:-  def:-define a function
#def hello_func():               #creation of function
#   print('Hello Function!')           only updating this the no.of times cl or print prined
#hello_func()          #this will cl the function and print
#hello_func()          #this is printed by updated 
#hello_func()          #this is printed by updated 
#def hello_func():
#   return 'hello Function.'
#print(hello_func().upper())            #HELLO FUNCTION.
#def hello_func(greeting,name='you):
#   return '{}, {}'.format(greeting,name)
#print(]hello_func('Hi', name = 'sagar'))         #Hi sagar
#def student_info(*args, **kwargs):
#    print(args)                                         #('maths', 'art')
#    print(kwargs)                                       #{'name': 'Jhon', 'age':24}
#student_info('maths', 'art', name='Jhon', age=24)
"""
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType
#
#suresh tech (python):-youtube          IDLE:-integrated development & leraning environment(py interpreter)         IDE:-integrated development environment(Notepad++,pycharm,vs ect)   give file with extention .py 
#one member need to talk with m/c we have to use programming(c,c++,java,c#,etc) lang. 1991(introduced by (Gudio Van Rossum))
#progrmming is a way to instruct commputer to perform various task. 1st programming lang:Formula Translation(Fortran)(introduced by John Backs)
#python download(installing). program life cycle ((high lvl lang)input print("hello world")-(low lvl)m/c code(0,1)-(cpu)output(hello world). High lvl to low lvl m/c code:-Compiler(converts high lvl lang to m/c code in one session c,c++,java,etc.performance is fast.),Interpreter(converts to m/c line by line py,perl,matlab etc.performance is lower.),Assembler(converts assembly lang into m/c),Translator(Generic term that cloud refer to a compiler,assembler or interpreter. converts high lvl to low lvl.)
#py is a scripting,general-purpose,high-lvl, & interpreted programming lang. (s lang: is a programming lang that is interpreted)                key words are known as reservered words by py.(total 35 words is reserved)        Identifiers:-Identifier is the name given to identify a variable,cls,fun etc.    
#statement:-Any excutable instruction that tells computer to perform a specific action is called a statement. group of statements is called a block. Indentation all statement with the sm distance to the right will make block of code. comments:information that the davelopers provide to understand the sourcce code(improves readability of the program)#single line comment,""""""''''''Multi line comments. 
#1st program
#a = 200 b =100 c = 600 d = 40     
#oneguidecost = 110
#total = a + b + c + d                       varibles are used to store data(values,elements) when you declare a varible,it occupies some space in the memory.      
#print(total)
#print(total/oneguidecost)           8.5444

#Name space(unique name for each & every obj) & scope(global space,local space).   input(input()fun) output(print()fun)
#output:-   print(value(s),sep=",end='\n', file=file,flush=flush)
#input:-we have to give while running the code input(),input('Enter your name'),list-will be discussed later.   by default entered input will be converted into string.  

#ATM Program:-
#pin, cash = input('Enter your pin and cash').split('@')
#print('pin and cash are',pin,cash)
#cashvalue = int(cash)
#atmAmount = 50000
#remainingAmount = atmAmount-cashvalue
#print('Take your cash',cash,remainingAmount,sep="@@",
#end="===")                                                     #Enter your pin and cash1234@5000
#print('Thank you for using ATM',end="\t")                      #pin and cash are 1234 5000
#print('Thank you sagar ragas for great teaching')              #Take your cash@@5000@@45000===Thank you for using ATM   Thank you sagar ragas for great teaching
#operators:-Are used to perform various operations on values & variables.
#Arithmetic:-add(+),sub(-),mul(*),divides(/)divides the 1st operand by sec(float),(//)divides the first operand by sec(floor),(%)returns the reminder when 1st operand is divided by sec,**Returns 1st to the power of sec.
#Relational:-(Returns either True or False b/t 2 variables)==,>,<,>=,<=,!=
#Assignment:-=(a=b+c),+=(a+=b,a=a+b),-=(a-=b,a=a-b),*=(a*=b,a=a*b)
#Logical:-and(both true),or(one true),not(false,vice versa)
#Bitwise:-&AND,|OR,~NOT,^XOR,>>RIGHT SHIFT,<<LEFT SHIFT

#Age program:-
#yearofbirth = int(input('please tell your date of year'))
#currentyear = 2023
#age = currentyear - yearofbirth
#print('your age is:',age)                   #24      2023-1999
#
#Data types:- are classes in py
#Numeric(int12,34,-56,float12.3,3.4,complex10+3j,12+6i)
#sequence types(strings(sequence of characters''""''''''(string is immutable or hashable(elements cannot be changed once assigned))(len,indexing0-all,slicinglstart:end:stop,concatenation is joining of 2 or more strings+*repeat)),list[]ordered collection of items,.append,.extend,insert,del,remove,pop(this is mutable),tuple():ordered collection of items(immutable)we cannot change elements once it is assigned)
#Boolean(True,False):assign or compare the elements
#Set{}unordered collection of iteams.can have any no.of items & they may be of diff types(int,float,tuple,string)but cannot have mutable elements(lists,sets,dic)set operations(union,intersection,difference,symmetric difference)
#Dictionary{}unordered collection of items(mutable)(no duplicates)dic holds key:value pair,
#
#indexing(0,1,2) & slicing(start:end:step):-
#channelname = "sagar ragas"  print(len(channel name)) print(channel name[1])    a
#print(channelname[1:4])     aga   print (channelname[3:10:2]   arg       print(channelname[::-1])    sagar ragas(printed reversly)
#concatenation:joining two or more strings into single string (+operator)
#repeating:-by using *2 or more we get no.of repeated elements in variable(*operator)

#control flow program:- if else statements
#lastball = 6       #4
#if lastball==6:
#   print('won the match')
#else:                                     #won the match
#   print('loss the match')                #loss the match

#number = int(input('enter a number'))
#if(number%2==0):                           #2
#   print('it is even number')             #it is even number
#else:                                      #5
#   print('it is odd number')              #it is odd number

#Nested if:-
#number = int(input('enter a number'))
#if(number%2==0):
#    if(number%4==0):
#       print('Congrates,divided by both 2 & 4')          #if given no. divides with 3 & 4 then congrates visabled
#    else:
#       print('sorry')
#else:
#   print('sorry')

#if-elif ladder:-
#rank = int(input('enter your rank'))
#if rank<=1000:
#   print('you got college1')                    #1  you got college1
#elif rank>1000 and rank<=10000:
#   print('you got college2')
#elif rank>10000 and rank<=40000:
#   print('you got college3')
#else:
#   print('sorry no colleges available of your rank')

#for loop:-used for sequential traversing & usd for printing iterable elements.(if we know fixed no.of iterations(definite)(we you for loop))  (break,continue,pass)
#numberlist = [1,2,3,10,19,30]           #1     #5
#for number in numberlist:               #2     #10
#   print(number)       #print(number*5)#30     #150
#
#for i in range(11):               #1
#   print(i)                       #10
#
#name = input('enter your name')
#lasttwocharacters = name[-2:]
#for numbers in range(1,11):                          #ararararar
#   print(lasttwocharacters*numbers)
#
#name = input('enter your name')                           #s -it is consonant
#vowelslist = ['a','e','i','o','u']                        #a -it is vowel 
#for character in name:                                    #g -it is consonant
#   if character in vowelslist:                            #a -it is vowel
#       print(character,'-it is vowel')                    #r -it is consonant
#   else: 
#       print(character,'-it is consonant')
#
#control statements:break,continue,pass
#marks = [50,67,40,90,30,98]
#sum=0
#for mark in marks:
#    sum = sum+mark
#print('Total sum',sum)           #Total sum 375
#
#While loop:-you never know how many number of times loops executes(indefinite iteration)      (break,continue,pass)
#i = 1                     #1
#while i<10:     #i<=10   #2
#    print(i)              #3
#    i=i+1                 #9   10           
#
#import random
#score = 0
#scoreinfo = []
#while score<500:
#    scorevalue =  random.randint(1,30)
#    score = score + scorevalue
#    scoreinfo.append(scorevalue)                                        #Total flips 30 [20, 12, 27, 2, 13, 24, 1, 18, 21, 24, 13, 25, 21, 22, 22, 5, 7, 3, 26, 21, 3, 3, 17, 26, 27, 16, 29, 9, 2
#print('Total flips',len(scoreinfo),scoreinfo,score)                     #3, 27] 507
#
#pass statement:-used in case if we are not sure what to code
#slicing:-is used to get subset of the sequence of items[start:end:step]
#break:returns control out of the loop directly
#continue:return control to the begining of the loop

#functions:-is put commonly used statement s together instead of writing same code again again
#def evenorodd(number):
#    if(number%2==0):
#            print('{}is even'.format(number))
#    else:        
#            print('{is odd.format(number)}') 
#
#evenorodd(19)
#evenorodd(18)
#evenorodd(22)

#oops(object oriented programming system):-   obj=anything that has state & behaviour is called an obj.   cls:-is a blueprint to create a obj. 
#
#
#
#
#
#
#
#
#
#
#programming knowledge:-               print=is a in-built function         hello world=is a argument
#python:-multi-paradigm programming language,interpreted language,object oriented programming language,supports dynamic data type,independent from platforms,it is free & open source. 
#born dec-1989. by Guido van Rossum. public release feb-1991. python.org webite -1996 0r 1997. it is a scripting language. 
#order of operationsin py(in PEMDAS):-(),**,* / // %,+ -. (parentheses,exponents,Multiplication & division,addition & subtraction)(please,excuse,my dear,aunt sally)
#Variable is a storage location paired with an symbolic name, which contains some known or unknown quantity of information referred to as a value. 
#
#dir (__builtins__)      #to see all functions list (float,pow,len,max,min,range,print,type,)    help (max)
#In many languages require you to complie your program into a form that the m/c understands.    (complie-->execte-->output) 
#python is instead directly interpreted into m/c instructions        (source code-->output)
#
#if elif else conditions:-
#name = input("enter a name: ") 
#if name == "sagar":
#    print("name entered is : ", name)
#elif name == "leo":
#    print("name entered is : ", name)
#elif name == "roy":
#    print("name entered is : ", name)
#elif name == "evu":       
#    print("name entered is : ", name)
#else:    
#    print("name is invalid")

#nested if conditions:-
#x = 10
#if x >= 0:
#    print("x is positive")
#    if (x%2) == 0:
#        print("x is even")
#    else:
#        print("x is odd")
#else:                                   #x is positive
#    print("x is negative")              #x is even

#
#0bject:-instance of cls,implimention of cls         (BMW)
#class:-blueprint of object,     (car)
#Encapsulation:-protecting our data (school bag)
#polymorphism:-different behaviors in different instances
#Abstraction:-hiding our irrelevant data
#inheritance:-one property of the obj is acquiring another property of an obj    (father son)
#
##List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#
#for adding items in list:- .append,.insert,.extend         Remove item:- .remove,.pop,del thislist[0],.clear()
#for adding items in set:- .add,.update,here we can add list to set by .update.        remove item:- .remove, .discard, .pop, .clear, del 
#for adding items in Dictionary:- thisdict["color"] = "red"   ,.update({"color": "red"})    remove item:- .popitem(),del thisdict["model"],.clear()
#
#import random
#print(random.randrange(1, 10))                #print different 1 to 10. 
# 
#a = "Hello, World!"
#print(a[1])                       #e
#x = int(2.8)            2
#print(type(x))          #int
#y = float(1)            #1.0
#print(type(y))          #float
#
#name = (3+4j)
#print(name)          #(3+4j)
#print(type(name))    #complex
#s = {'sagar':'ragas'}     
#print(s)              #{'sagar': 'ragas'}
#print(type(s))        #dict

#for i in range(1,10):                #hello
#    print('hello')                   #hello   9times printed

#
#salary = [1,2,3,4,5,6]               
#sum=0
#for values in salary:      
# sum = sum + values              

#print(sum)            #21 sum of the all elements
#
#str = "sagarram"
#print(str[::-1])      printing reverse order. 
#
#
#name = input("Enter a Name: ")

#vinay question
#v1 = 'strings in python'
#print(type(v1))                                               #<class'str'>
#for i in v1:                                                 #s
#       print(i)                                              #t


#name = input("enter a value:")
#if  name == "yash":
#    print("He is from kphb")
#elif name == "vinay":
#   print("He is from sangareddy")
#elif name == "dillip":
#    print("He ias from ameerpet")
#elif name == "sagar":
#    print("He is from madhapur")
#elif name == "tharun":
#    print("He is from gachibowli")
#elif name == "vamsi":
#    print("he is from lb nagar")
#else:
#    print("The entered name is invalid")
#compiler:-this convert the human lang to machine lang and give the output.  Drawback this will show the error after compile & excuting the full code. this consumes lot of memory. ()
#interpreter:-this will convert the sm human lang to m/c lang. but it is easy to debug errors. & this compile & excutes by line by line. that code can be executed as soon as it is written. This means that prototyping can be very quick. Python can be treated in a procedural way, an object-oriented way or a functional way.
#w3schools:-
#python is programming language. python can be used on a server to create web apps. 
#Python File Handling:-In our File Handling section we will learn how to open, read, write, and delete files.Python File Handling
#It was created by Guido van Rossum, and released in 1991. This used to web development,software development,mathematics,system scripting.
#Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick. Python can be treated in a procedural way, an object-oriented way or a functional way.
#Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.
#in cmd we go inside python & write our code print("Hello, world!") :-Hello, world!  if you want to exit then use:- exit().
#Indentation is refers to the spaces in python.& this is most imp in python. The number of spaces is the most common use is four, but it has to be at least one.
#if 5 > 2:
#  print("Five is greater than two!")   #Five is greater than two!
#
#Variables:variables are created when you assign a value (or) element to it:
#X = 5    y = ("sagar")       print(x) 5  print(y) sagar
#Commenting single line use#     & multiple lines """        """     
#Variable are containers for storing data values or elements. x = 5 print(x) 5       y = "sagar" print(y) sagar
#Variables do not need to be declared with any particular type, and can even change type after they have been set. x = 5  x = "sagar"  print(x) sagar
#Casting:If you want to specify the data type of a variable, this can be done with casting.  x = str(3) print(x)'3'   y = int(3) print(y)3   z = float(3)  print(z)3.0 . 
#Get the type:we can get the type of a variable with type() function.  x = 5 print(type(x) <class 'int'>      y = "sagar" print(type(y))  <class 'str'>.     
#Variable names:-should start with letter or underscore.should contain alpha numeric character & under scores. are case-sensitive. varible name dont start with numbers, dont use python key words. 
#Multi words variable names:-Camel Case,Pascal Case,Snake Case.
#Python allows you to assign values to multiple variables in one line:
#x, y, z = "orange", "apple", "mango"      print(x)  print(y)  print(z)   orange apple mango
#And you can assign the same value to multiple variables in one line
#x = y = z = "apple"  print(x) print(y) print(z)  apple apple apple
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#fruits = ["apple", "mango", "grapes"]
#x, y, z = fruits   print(x) print(y) print(z)  apple mango grapes
#Output variables:- print() function   x = "python is awesome"  print(x)   python is awesome 
#Output multiple variables, separated by comma: x = "python" y = "is"  z = "awesome"  print(x, y, z)  Python is awesome       & this is the best way to combine in python.
#Output multiple variables you can also use + operater variables: x = "python"  y = "is"  z = "awesome"  print(x + y + z)  Python is awesome
#Global variables:-Variables that are created outside of a function are known as global variables.
#x = "awesome"
#def myfunc():
#  print("python is" + x)
#myfunc()               #Python is awesome
#
#Python Data Types (or) Built in type:- text:str(''""),    numeric:int(20), float(2.0), complex(1j)   sequence:-list[], tuple(), range(range(6))     mapping:dict {"sagar" : "ragas"}  set:set{"apple", "mango"},  x = forzenset({"apple", "mango"})) print(x) frozenset({'apple', "mango"})    boolean:bool true   binary:bytes(b"Hello"),bytearray(bytearray(5)),memoryview(memoryview(bytes(5)))   none:none none. 
#
#Python numbers:-integer(1,-1),float(1.0,-1.0),complex(1+5j,-5j)   by using print(type(x)) we can find the type of object. 
#Type conversion:-convert from one type to another with the int(), float(), and complex() methods:  #note:- we cannot convert complex numbers into another number type.
#x = 1  y = 2.8  z = 1j   a = float(x)  b = int(y)  c = complex(z)   print(a)1.0  print(b)2  print(c)1+0j  print(type(a))float  print(type(b))int  print(type(c))complex. 
#Random numbers:-Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:  import random   print(random.randrange(1, 10))  #this will create random numbers when we run this code. 

#Python strings:-Strings in python are surrounded by either single quotation marks, or double quotation marks.'hello' is the same as "hello". we can assign a string to a variable a = "Hello" print(a). we can assign a multiline string to a variable by using three quotes""""""(or)'''''':
#String are Arrays:-Get the character at position 1  a = "Hello, World" print(a[1]) e  by using indexing the character will be shown. 
#Looping through a string:-Loop through the letters in the word "saagarragas" for x in "sagarragas"  print(x)    this will the element & produce in sequence manner(vinay question).
#String Length:-The len() function returns the length of a string:  a = "Hello, World"  print(len(a))13  #this will show the length of the variable. 
#Check string:-To check if a certain phrase or character is present in a string, we can use the keyword in. txt = "The best things in life are free!"   print("free" in txt)  #this will check the variable & give Boolen.  if statement:   txt = "The best things in life are free!"  if "free" in txt:  print("Yes, 'free' is present.")    #gives output:Yes, 'free' is present.
#Check if Not:-To check if a certain phrase or character is NOT present in a string, we can use the keyword not in. txt = "The best things in life are free!"  print("expensive" not in txt) #give boolen. if statement:  txt = "The best things in life are free!"  if "expensive" not in txt:  print("No, 'expensive' is NOT present.")     #gives output:No, 'expensive' is NOT present.
#String Slicing:You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.  b = "Hello, World!" print(b[2:5])llo  #from position 2 to position 5.  from start print(b[:5])Hello  from end print(b[2:])oll world  for negative indexing print(b[-5:-2])orl.
#Python-modify Strings:-a = "hello world!"  print(a.upper())HELLO WORLD!  a = "Hello, World!"  print(a.lower())hello world!   a = " Hello, World! "  print(a.strip()) Hello, World(this remove the extra space)  a = "Hello, World!"  print(a.replace("H", "J"))Jello, World!  a = "Hello, World!"  print(a.split(","))  ['Hello', ' World!']     
#Concatenate String:- To concatenate, or combine, 2strings we can use + operator  a = "Hello" b = "World!"  c = a + b print(c)HelloWorld   #To add a space b/w them c = a + " " + b print(c)Hello World  
#Format Strings:-we can not combine strings and numbers.But we can combine strings and numbers by using the format() method! age = 24  txt = "my name is sagar, & I am {}"  print(txt.format(age))My name is sagar, and I am 36.  #we can add unlimited numbers of arguments quantity = 3 item = 567 price = 49.95  myorder = "I want {} pieces of item {} for {} dollars."  print(myorder.format(quantity, item, price))I want to pay 49.95 dollars for 3 pieces of item 567.    #by using index numbers we add arguments in a correct place.    
#Escapr Characters:\"  txt = "We are the so-called \"Vikings\" from the north."  print(txt)We are the so-called "Vikings" from the north.

#Python Boolean Values:-In programming you often need to know if an expression is True or False. print(10 > 9)True  #When you run a condition in an if statement, 
#a = 200 
#b = 90 
#if b > a: 
#   print("b is greater than a")
#else: 
#   print("b is not greater than a")       #b is not greater than a
#check the object is an integer or not:  x = 200 print(isinstance(x, int))True
# 
#Python Operators:-Operators are used to perform operations on variables & values.  Python Operators:-Arithmetic operators(+ - * / % ** //),Assignment operators(= += -= *= /= %= //= **= &= |= ^=  >>= <<=),Comparsion operators(== != > < >= <=),Logical operators(and or not),Identity operators(is  is not),Membership operators(in  not in),Bitwise operators(& | ^ ~ << >> )  Precedence(first to last) order in python(() ** +x -x ~x * / // % + - << >> & ^ | == != > >= < <= is  is not in  in not  not and or) 
# 
#Python list[]:-Lists are used to store multiple items in a single variable.Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.List items are ordered, changeable, and allow duplicate values.List items follow the index(0 to end)   #To find length of list List = ["sagar", "ragas"] print(len(List))2 #list item contain different data types.  #to find type of list List = ["Sagar", "Ragas"] print(type(list))<class 'list'>
#Python Collection (Arrays):- 
#List:-is a collection which is ordered and changeable. Allows duplicate members.
#Tuple:-is a collection which is ordered and unchangeable. Allows duplicate members.
#Set:-is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. #*Set items are unchangeable, but you can remove and/or add items whenever you like.
#Dictionary:-is a collection which is ordered** and changeable. No duplicate members. #As of Python version 3.7, dictionaries are ordered
#Access List item:-are indexed and you can access them by referring to the index number. #list =["sagar", "ragas"] print(list[1])ragas  #negative indexing means start from the end list = ["sagar", "ragas"] print(list[-1])ragas  #Range of indexes list = ["apple", "banana", "cherry", "orange", "kiwi", "melon",] print(list[2:4])['cherry', 'orange']  #start to end but not including 4 list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] print(list[:4])['apple', 'banana', 'cherry', 'orange']   #this will print 2 to end print(list[2:])  #check if item exists list = ["apple", "mango", cherry]  if "apple" in list  print("yes")yes. 
#Change list items:-To change the value of a specific item, refer to the index number. list =["sagar", "ragas"] list[1] = "ram" print(list) ['sagar', 'ram']  #change a range of items lidt[1:3] =["blackberry", "watermelon"] print(list)  #insert a iteam to variable:- list = ["apple", "banana", "cherry"]  list.insert(2, "watermelon") print(list)['apple', 'banana', 'watermelon', 'cherry']
#Add list items:-To add an item to the end of the list, 1)apppend items() method is used. list = ["apple", "banana", "cherry"]  list.append("orange") print(list)['apple', 'banana', 'cherry', 'orange'].  2)insert items() list.insert(1, "orange") print(list)['apple', 'orange', 'banana', 'cherry'] 3)extend list list tropic = ["mango", "pineapple", "papaya"] list.extend(tropical)  print(list)['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'].
#Remove list items:-remove() method removes the specified item. #list = ["apple", "banana", "cherry"]  list.remove("banana") print(list)['apple', 'cherry']  #by index pop() list.pop(1)print(list) this remove the 2nd value.  list.pop() remove the last value. del list[0]remove the index. del list this will delte the list. list.clear() this will clear the list[].
#Loop Lists:-loop through the list items by using a for loop: items by one by one  
#list = ["apple", "banana", "cherry"]
#for x in list:                     #apple
#print(x)                           #banana
#While loop:-
#list = ["apple", "mango", "orange"]
#i = 0
#while i < len(list):        #apple
#   print(list[i])           #mango
#   i = i + 1                #orange
#list comprehension:-List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list 
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []
#for x in fruits:
#  if "a" in x:
#    newlist.append(x)
#print(newlist)                     #['apple', 'banana', 'mango']
#
#Sort Lists:-List objects have a sort() method that will sort the list alphanumerically, ascending, by default: 
#thislist = [100, 50, 65, 82, 23]                  #thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
#thislist.sort()                                   #thislist.sort()
#print(thislist)      #[23, 50, 65, 82, 100]       #print(thislist)     #['banana', 'kiwi', 'mango', 'orange', 'pineapple']'''



#sundeep saradhi:-youtube      py is simple syntax,length of code is small,complex problems sloved. features of py:-simple to learn,open source,portability,high level interpreter,object oriented,standard libraries. 
#pthyon is a procedural & object oriented language.
#building block:-function,object & class driven. Extension(.py). Translation type(interpreted). Database connectivity(supported in py).IDE(Vs code,pyCharm,pyDev,Jupyter,Notebook,Spyder,etc.,)
#py key words:False,return,lambda,from,And,as Yield,pass,raise,class,None,tryglobal,del,elif,assert,break,finally,continue,True,nonlocal,not,if,else,except,is,for,def,while,with,or,import,in. dont use this as varible naming purpose. varible is name given to a memory location.
#Numeric:-integer 3,4,5,complex number a+bj,float 3.14,4.19
#Dictionary:key:value pairs key1:value1,key2:value2 
#Boolean:True or False
#Set:unorderd collection of unique object. {10.20}
#Sequence Type:-strings"sagar","python",List[10,"sagar"],tuple(10,20,30).Dic (multiple values can assinged)
#
#variables assignment:-
#basic assignment:- ls = "sagar"  print(ls)   sagar
#Tuple assignment:- x,y =(20,49)  print(x)20 print(y)49   
#List assignment:- x,y =[20,46] print(x)20  print(y)46
#sequence assignment:- a,b,c=10,20,30 print(a)10 print(b)20 print(c)30  (or) print(a,b,c)
#Extended sequence unpacking:-p*q = 'hello'  print(p)h  print(*q)['e','l','l','o']
#multiple target assignment:-a=b=c=0  print(a)0 print(b)0 print(c)0
#augmented assignment:-a=5  a=a+5 print(a)10  a+=5 print(a)15.
#
#we cant convert str to int but it automatically takes input int to string format. the input function read the data into string format.  
#
#
#a = input("enter a value: ").split()   #10, 20, 30, 40
#print(a)                    #['10', '20', '30', '40']
#print("hello", end=" ")                             #hello world (this print in sm line)
#print("world")
#print ("hello","welcome","to","python", sep="\n")      #this print in different lines. hello welcome to python.
#a = 10
#b = 4.5
#print(a, "this is grade",b, "this is points")       #10 this is grade 4.5 this is points
#
#operators:-
#Arithmetic ope(+,-,*,/(quation),//,%(remainder).**(power))
#Relational Ope(<,>,<=,>=,==,!=)    #boolen result
#Assignment Ope(==,+=,-=,*=,/=,%=,//=,etc.,)
#Bitwise Ope(&,|,^,~,<<,>>) (decimal-->binary-->operation-->decimal)
#Logical Ope(and,or,not)        #boolen results
#membership Ope(or) search ope (in, not in)
#Identity Ope(is,is not) by using id(a)  id(b)

#control structures:-flow of control:-1)sequential-line by line 2)conditional-based on condition(if,if else,if elif else,nested if) 3)iterative/loops-group of start executly repeated(for,loop)(while loop) 4)jumping statements(break,continue,pass)
#
#
#a = int(input("enter a value: "))
#b = int(input("enter a value: "))
#c = int(input("enter a value: "))
#if a>b:
#    if a>c:
#        print("a is big")             #30 20 10 a is big
#    else:
#        print("c is big")
#else:
#    if b>c:
#        print("b is big")
#    else:
#        print("c is big")

#n = int(input("enter a value: "))
#i = 1
#while i <= n:
#    print(i)
#    i = i+1                   #this is increment or decrement statement  #100    #this print 1 to 100 values.

#for i in range(1,101):
#    print(i)                 #this will print 1 to 100 values by using for loop.

#n = int(input("enter a value: "))
#i = 1
#while i<=n:
#    print(i,end=",")       #this will print 1 to 100 side by side. 
#    i = i+1

#we can access with:-1)range  2)sequence(takes multiple values)
#1)for i in range(1,101):         #start,stop,gap
#    print(i)                  #1,101        #this print 1 to 100 values.  #print(i,end=" ") #this print side by side1 100.

#2)st ="python"      #p              #li=[10,20,30,40]    #10
#for ka in st:       #y              #for i in li:        #20
#    print(ka)       #t              #  print(i)          #30


#s = "p"
#s1 = "y"
#s2 = "t"
#s3 = "h"
#s4 = "o"
#s5 = "n"
#print(s+s1+s2+s3+s4+s5)  #python
#print(s,s1,s2,s3,s4,s5)  #p y t h o n

#for i in range(5):                   #*  this will print * in separate lines. 
#    print("*")                       #*       by combining this 2 codes we get L shape is ready.
                                      #*
#for j in range(5):
#    print("*",end=" ")               #* * * * *   by using end function this printed in same row

#for i in range(5):                      # * * * * *
#    for j in range(5):                  # * * * * *
#        print("*",end=" ")              # * * * * *
#    print(" ")                          # * * * * *
                                         # * * * * *

#for i in range(5):                       #*          (outer loop =rows inner loop =columns). 
#   for j in range(i+1):                  #* *          #this is increasing triangle pattern.
#        print('*',end=" ")               #* * *
#    print(" ")                           #* * * *
                                          #* * * * *
#for i in range(5):                       #* * * * *               #this is decreasing triangle pattern.
#    for j in range(i,5):                 #* * * *
#        print("*",end=" ")               #* * *
#    print()                              #* *
                                          #*           

#for i in range(5):
#   for j in range(i,5):            #* * * * *            #        *      #this total code will be printed as box shape.
#        print("*",end=" ")         #* * * *              #      * * 
#    for j in range(i+1):           #* * *                #    * * *
#        print("*",end=" ")         #* *                  #  * * * *
#    print()                        #*                    #* * * * *  

#for i in range(5):                  #*                   # * * * * *
#    for j in range(i+1):            #* *                 #   * * * *      #this total code will be printed as box shape.
#        print("#",end=" ")          #* * *               #     * * * 
#    for j in range(i,5):            #* * * *             #       * *
#        print("*",end=" ")          #* * * * *           #         *
#    print()     

#for i in range(5):                         #        *                            
#    for j in range(i,5):                   #      * * *
#        print(" ",end=" ")                 #    * * * * *     #this is hill triangle
#    for j in range(i):                     #  * * * * * * *
#        print("*",end=" ")                 #* * * * * * * * *
#    for j in range(i+1):
#        print("*",end=" ")
#    print()    

#for i in range(5):
#    for j in range(i+1):                #this revrse hill triangle   #by adding this both we can get Diamond shape 
#        print("",end=" ")
#    for j in range(i,-1):
#        print("*",end=" ")
#    for i in range(i,5):
#        print("*",end=" ")

#name = 'python'                          #p
#for i in range(len(name)):               #p y
#    for j in range(1+i):                 #p y t
#        print(name[j],end=" ")           #p y t h
#    print()                              #p y t h o 
                                          #p y t h o n


#jumping statements:-
#for i in range(10):
#    if i == 7:
#        break       
#    else:
#        print(i)                   #0 1 2 3 4 5 6 

#for i in range(10):
#    if i == 4:
#        continue
#    else:
#        print(i)                    #0 1 2 3 5 6 7 8 9 #this will skip the 4 from the given values.

#for i in range(10):
#    if i == 5:
#        pass
#    else:
#        print(i)                    #0 1 2 3 4 5 6 7 8 9 

#i = 1
#while i<=10:
#    if i==5:
#        pass        #1 2 3 4 5 6 7 8 9 10 are printed
#    print(i)
#    i = i+1        #increment or decrement

#i = 1
#while i<=10:
#    if i == 5:
#        continue            #1 2 3 4
#    print(i)
#    i = i+1

#i = 1
#while i<=10:
#    if i == 5:
#        break      #1 2 3 4
#    print(i)
#    i = i+1


#Mathamatical functions & randam functions:-
#import math
#print(math.ceil(20.1)) #21  #shows top value
#print(math.floor(20.9)) #20 #shows less value
#a= 10
#b = 20
#print(math.copysign(a,b))  #a=10 b=20  #-10.0    
#print(math.fabs(b))   #20.0.
#print(math.factorial(5)) #120
#l =10,20,30
#print(math.fsum(l))  #l=10,20,30  #60.0
#print(math.gcd(3,10)) #1
#print(math.pow(2,3)) #8.0
#print(math.sqrt(16)) #4.0
#print(math.sin(60))  #-0.30428106    print(math.cos(30)) 0.1541592635897
#print(math.pi)       #3.141592635
#print(math.tau)     #6.283153071
#print(math.e)       #2.7182818284
#import random
#l=[10,20,30,40,50]
#print(random.choice(l))      #this print random numbers
#print(random.choices(l,k=3))  #this display 3values randomly [30, 50, 30]
#print(random.randrange(10,15,1)) #this print random numbr in range
#print(random.shuffle(l))  #this shuffles the list values
#print(random.uniform(10,15))        #this will show the random value in given,

#list[]:-multiple data types values assigned to one variable. [cama sperated values]. list is mutable we can add remove & modify easily. 
#   0 1 2 3 4 5     6
#a=[1,2,3,7,8,20.4,"hello"]
# -7 -6 -5 -4 -3 -2  -1
#print(a[0])             #assessing throgh index values    1
#print(a[-1])            #hello
#print(a[::-1])          #this will print list in reverse order ['hello', 20.4, 8, 7, 3, 2, 1]       
#slicing:-extracting some of multiple values from give values:-
#print(a[:])                #[1, 2, 3, 7, 8, 20.4, 'hello']    
#print(a[0:3])              #0start,:slicing,3stop.      [1, 2, 3]                
#print(a[:4])               #[1, 2, 3, 7]
#print(a[4:])               #[8, 20.4, 'hello']
#Reassignmeng list elements:-
#a[3] =30
#print(a)                  #element was replaced 7 to 30 [1, 2, 3, 30, 8, 20.4, 'hello']
#Basic Operations:-+,*,len,min,max,sum,membershio,iterations.
#a =[10,20,30,40]
#b =[50,60,70,80]
#print(a+b)                 #this will add the 2 list(concatenation)[10, 20, 30, 40, 50, 60, 70, 80]
#print(a*b)                #this wont workout becz only we have to give the int for multiplication with list. not a list to list.
#print(len(a))              #4
#print(max(a))              #40
#print(min(a))              #10
#print(sum(a))              #100
#print(10 in a)             #True
#print(50 in a)             #False
#print(10 not in a)         #False
#for i in a:
#    print(i)               #10 20 30 40
#for i in range(len(a)):
#    print(a[i])           #10 20 30 40

#bulit in functions:-  (append,extend,insert)used for adding elements to variable.  (remove,pop,del)used for deleting the values. (sort)used for assending & decending order.
#k = [30,60]
#print(type(k))         #list
#k.append(90)
#print(k)                #[30,60,90]
#k.extend([120,150,160])
#print(k)                 #[30, 60, 90, 120, 150, 160]adding multiple values
#k.insert(2,40)
#print(k)                 #[30, 60, 40, 90, 120, 150, 160]#this insert 40 in 2 place of the list
#k.remove(90)
#print(k)                #[30, 60, 40, 120, 150, 160] #this will remove the 90 element from list 
#k.pop()
#print(k)                #[30, 60, 40, 120, 150] #this will dlt the last amount from the list.
#del k[0]
#print(k)                #[60, 40, 120, 150] this will be remov the 30 by accessing index
#import random
#random.shuffle(k)
#print(k)                #[60, 40, 120, 150]
#print(sorted(k))        #[40, 60, 120, 150] asending order
#(k.sort(reverse=True))
#print(k)                #[150, 120, 60, 40] desending order
#s = [10,20,30,40,10,20,30,40,30,40,20,10]
#print(s.count(30))         #3  how many times it is repeating the value in list.
#(s.reverse())
#print(s)                #[10, 20, 40, 30, 40, 30, 20, 10, 40, 30, 20, 10] this will show the revers order of s

#list comprehension:-
#y =[ele*ele for ele in range(10)]  #0,1,2,3,4,5,6,7,8,9  
#print(y)                         #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] this give all squares 
#y = [ele for ele in range(10) if ele%2==0]
#print(y)                         #[0, 2, 4, 6, 8]  this will show the even numbers

#tuple():is a immutable (we cant change the values(add,del,reassign))(coma separated values multiple data types used) we can access by index.
#tu=(10,20,30,40,50)
#print(type(tu))               #<class 'tuple'>
#print(tu)                     #(10, 20, 30, 40, 50
#print(tu[0])                  #10
#print(tu[-1])                 #50
#print(tu[1:4])                #(20, 30, 40)        #if we want to change the values in tuples we have to convert tuple to list then we can change tuple to list.
#print(len(tu))                #5
#print(min(tu))                #10
#print(max(tu))                #50
#print(sum(tu))                #150 
#print(10 in tu)               #True
#print(100 in tu)              #False
#for ele in tu:
#    print(ele)                #10 20 30 40 50
#for i in range(len(tu)):
#    print(tu[i])              #10 20 30 40 50
#print(tu.count(10))           #1 gives index values
#print(tu.index(40))           #3 this will give the index number.
#tk = (10)
#print(type(tk))               #int
#ty =(10,)
#print(type(ty))               #tuple comma should be added.

#strings:-""''
#st = "python"
#print(type(st))           #str
#print(st)                 #python
#print(st[0])              #p
#print(st[-1])             #n
#print(st[:3])             #pyt
#str = "Hello"
#welcome to python"""
#print(str)                #welcome to python
#s1 = "python"
#s2 = "programming"
#print(s1 + s2)            #pythonprogramming
#print(s1*2)               #pythonpython
#print(len(s1))            #6
#print(min(s1))            #h   by following the hashkey 
#print(max(s1))            #y
#print('p' in s1)          #True
#for i in st:              #p
#    print(i)              #y
#for i in range(len(st)):  #p
#    print(st[i])          #y
#s1[2]= 'z'                #strings also wont support for item assignment.this is also immutable.
#built in methods:- 
#s = "Welcome To Python Programming"   
#print(s.capitalize())              #Welcome to python programming
#s1 = "python"
#print(s1.center(10,"*"))           #**python**   * using as fill character.
#print(s.count('o'))                #4 times o is there in this variable. 
#print(s.endswith("ing"))           #True
#print(s.startswith("wel"))         #True
#print(s.find('o'))                 #4 index
#print(s.rfind('o'))                #20 reverse index
#print(s.index('o'))                #4 index
#s2 = "abc123"
#print(s2.isalnum())                #True  #this will say alpha or numeric elements present in variable or not (True or False)
#s3 = "Welcom to python programming"
#print(s3.title())                  #Welcom To Python Programming (1st letter capital)
#print(s2.ljust(10,'*'))            #abc123****
#print(s2.rjust(10,'*'))            #****abc123
#print(s1.upper())                  #PYTHON
#print(s1.lower())                  #python
#s4 = '  Python   '
#print(s4)                          #   python
#print(s4.lstrip())                 #python      removes the left free spaces
#print(s4.rstrip())                 #   python
#print(s.replace("o","y"))          #welcyme ty pythyn prygramming
#rint(s.split())                   #['welcome', 'to', 'python', 'programming']
#print(s.swapcase())                #wELCOME tO pYTHON pROGRAMMING (convert small to big & big to small)
#print(s1.zfill(10))                #0000python

#Sets:-{}, comma separated values. multiple data types. Duplicate will be removed only unique. un ordered. mutable(we can add data & remove data). no-indexing & no-slicing. if we need to assign set give as set() other wise it taken as k dict.
#se = set()
#print(type(se))           #set
#se = {10,90,40,70,90}
#print(se)                   #{40, 10, 90, 70} un-ordered & duplicates are removed & printed.
#print(len(se))              #4
#se.add(80)
#print(se)                  #{70, 40, 10, 80, 90}  #this add 10
#se.remove(10)
#print(se)                  #{70, 40, 80, 90}      #this remove 10
#se.discard(90)
#print(se)                  #{70, 40, 80}
#print(se.pop())            #40 this del the last element and display that.
#for ele in se:             #70
#    print(ele)             #40
#print(se.__len__())        #2
#s = {10,20,30}
#t = {10,20,40,50,60}        #s.issubset(t),t.issubset(s),t.issuperset(s),s.issuperset(t),s.union(t),s.intersection(t),s.difference(t),
#s.add(100)
#print(s)                   #{100, 10, 20, 30}
#print(s.symmetric_difference(t))    #{50, 100, 40, 60, 30}
#s.update(t)
#print(s)                   #{100, 40, 10, 50, 20, 60, 30}

#Dictionaries:-{}. items. key-value based. keys-no duplicates,values-can duplicates. by using keys we can access.
#di = {"name" : "sagar", "per" : "88"}
#print(type(di))                   #dict
#print(di)                         #{'name': 'sagar', 'per': '88'}
#print(di["name"])                 #sagar
#di["per"]=90
#print(di)                         #{'name': 'sagar', 'per': 90} #value updated
#di['collage']='abcd'
#print(di)                         #{'name': 'sagar', 'per': 90, 'collage': 'abcd'}   #one key : value added
#print(len(di))                    #3
#del di['collage']
#print(di)                         #{'name': 'sagar', 'per': 90}
#d = {i:1**2 for i in range(10)}
#print(d)                          #{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

#Functions:-for a complex program to be reduced by step by step is knowns functions. 
#types of functions:1)Built in functions(factorial,pow,sqrt,sin,cos),  2)user defined functions(we have to create this),  3)Lambda(this is Anonymus function),  4)recursion
#2)user defined function:-we have to write (user defined function- top (def))-->function call
#def welcome():                       #function creation(or)defination with name  (without parameter,without return value).
#    print("welcome to the python world")
#welcome()                    #welcome to the python world  #functionn calling

#def display(str):               #fun calling or defination with name #we can pass function call to fun defination.
#    print("hello", str , "welcome to functions" )
#display("python")             #hello python welcome to functions. #inthis python & str is arguments (or)parameters.

#def add(a,b):
#    c=a+b
#    print(c)
#add(10,20)               #30

#def add(a,b):
#    c=a+b
#    return (c)
#res =add(10,20)
#print(res)              #30

#types of Arugments:1)Required Arguments(parameters should match in both fun calling & defination,positional arguments),2)Default Arguments(no.of parameteres may not be equal in both call & def,Defult arguments should listed at end of the parameter),3)Keyword Arguments(we hve to use variable names are known as key words,no need to follow the positions),4)Arbitary Arguments(we can pass any no.of arguments in fun call,but only one argument in fun def).
#def display(a,b):
#    print(a,b)
#display(10,20)          #10 20

#def display(a,b=100):
#    print(a,b)
#display(10)              #10 100

#def display(a,b,c):
#    print(a,b,c)
#display(c=100,b=50,a=10)      #10 50 100

#def display(*marks):
#    print(marks)          #marks[2]       #69
#display(90,80,69,89,90)       #(90, 80, 69, 89, 90) #it gose into tuple format,we can access by index. here we can assign multiple values to single variable.  

#multiple values returns:-
#def display(a,b):
#    return a,b
#res=display(10,20)
#print(res)            #(10, 20)  print(res[0])  10 by using index value we can access.

#local variables & global variables:-
#a = 100                #global Variable.we can use outside the function.
#def display():
#    a=500              #local variable. 1st prefrence.we can only use with in the function.
#    print(a)
#display()      #500
#print(a)       #100

#lambda Function:- this is annymous function.
#add = lambda a,b : a+b        #a,b arguments.   a+b expressions.
#print(add(3,4))          #7

#Recursion:-just like iteration. calling the same fun itself. for stoping recursion we use Base condition. we use recursive call.
#def fact(n):
#    if  n==1:        #base condition
#        return 1
#    else:
#        return n*fact(n-1)
#print(fact(10))                  #24

#files:-we can store outputs then we can read anytime.    open,read/write,close.   read(existing file we can read),write(it remove existing file & add new from first line),append(it creates if it has then append at end starts).
#file is data saving purpose used. write data into file(write,writelines),Reading Data from file(read,readline,readlines),file handling funs(tell,seek)

#Libraries in Python:-has lot of functions.
#data scinece:-Pandas,Numpy,SciPY,Scrapy,Matplotib,Seaborn,Scikit-learn,Tensorflow,Scikit-image,Librpsa.
#Data Visualization:-Matplotlib,ggplot,Ploty,Altair,Seaborn,Boken<Pygal
#Data Manipulation:-Pandas,Numpy
#Database Access:-SQLAlchermy,Quandl
#Data Modeling:-Tensorflow,PYtroch,Scikit-learn,Keras. 
#Deep learning:-TensorFlow,Troch,Caffe,Theano,Deepmat,ML.NET,Neon,Microsoft CNTK,Deeplearning 4j.
#Image Processing:-OpenCV,Scikit-image,Scikit-learn,Scipy,Numpy.
#AI & Machine learning:-Scikit-learn,Theano,TensorFlow,Keras.

#OOPs concepts:-object oriented programming concepts. 
#by using object running interpreter. 
#Encpslation:-Data & Methods is rapping & placing in a single unit.
#Abstraction:-Hiding implementation. only essential functionality is visible. here we method overriding.
#Data Hiding:-is protecting from unauthorized access specifiers.
#Inheritence:-(is a parent->child relationship). Here we need 2 classes. 1)Base class(parent),(by using child object we can access both parent & child) 2)derived class(child)(need object to access)
#1)single inheritance:-1 base(parent) class & 1 derived(child) class
#2)multilevel inheritance:-bass class--> derived class bass class(access base class)--> derived class(access base class & derived class).
#3)hierarchical inheritance:-1 base class & 2 derived classes
#4)multiple inheritance:-2 base classes & we get only one derived class.
#Polmorphism:-excuting in different ways is known as polmorphism.
#1)Compile Time Polymorphism:-operator overloading.(+)we can represent it as unary plus,addition,concatenation.  Method overloading(name will be same but parameter will be changed).
#2)Run Time Polymorphism:-method over riding concept is complsary here(name will be same & parameter also same). 1 in base class & 1 in derived class.

#Python supports for:-procedure orinted(written in functions & implemented) &(OOPs) object orinted(real world entity matching & we implement(objects,clases))   
#classes:-Logical entity. & this is a blue print. Object will follow the blue print.Object is a instance of a class.   Name(car)-->attributtes(brand,color,wheels)-->Functions/mathods(moving/idle/reverse). this all said to be generlized definition of a class. 
#object:-is a physical entity.follows the cls. instance of a class.real world entity(paper,car,pen).class:-human-->name,weight,height,color(logical entity class)-->walk,run sit. object:-sagar-->70kgs,5.11,white,-->walk,run sit. class is blue print and object is physical entity that follows the class.
#class if want to access(attributes,methods)by creating objects we can access this both.    without creating object we cant access attributes & methods.
#class is a keyword.
"""
class Human:                
    def __init__(self,c,h):         #__inti__ = intilazation constructor.
        self.color=c
        self.height=h 
    def run(self,n):
        print(n+" "+"Running...")
    def walk(self):
        print("Walking....")             #Class
sagar=Human("Whitw",5.11)              #obj name=class name()     
print(sagar.color,sagar.height)        #Whitw 5.11
ragas=Human("fair",5.7)
print(ragas.color,ragas.height)        #fair 5.7

sagar.run("sagar")                     #sagar Running...
ragas.run("ragaga")                    #ragas Running...
"""

#Inheritance:- Parent(base)-child(Derived class). 




"""
#for i in range(10):
#    print(i)

#x = 100
#def f1():
#    print("dont distrub me. because i am on fire:",x)
#f1()                                      #dont distrub me. because i am on fire: 100

card = (input("enter a value: "))
if len(card) == 16:
    #print(12*'#'+card[-1:-5:-1],end=" ")      #1method      ############4444
    #print(12*'#',end="")    
    #print(card[12:])                          #2nd method   ############4444
    #print(12*'#'+card[12:])                   #3rd method   ############4444
else:
    print("Invalid")


import math
print(math.sqrt(4))     #2.0

from random import*
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")
"""

#Keywords:-True,False,None,and,as assert,break,class,continue,def,del,elif,else,except,finally,for,from,from,global,if,import,in,is,lambda,nonlocal,not,or,pass,raise,return,try,while,with,yield. 
#In built DT:-int,float,complex,bool,str,bytes,bytearray,range,list,tuple,set,forzenset,dict,None.


sa = "sagar"            #str to list
ka = sa[::-1]
ma = []
print(ka)         #ragas
for i in ka:
    print(i, end="")    #ragas
    if i not in ma:
        ma.append(i) 
    else:
        pass
print(ma)       #['r', 'a', 'g', 's']

#

a="sagar"              #str to str 
dummy=""
for j in a[::-1]:
    if j not in dummy:
        dummy = dummy+str(j)
    else:
        pass
print(dummy)                   #rags
       
