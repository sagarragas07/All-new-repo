#python:- is a programming language. is a set of extensions that given to computer to complete the task.
#in python indentation is very imp
#python used:-web development,game development,m/c learning and Ai,data science & data visualization,business app,audio & video app
#variables:- a variable name can be started with: lower case,upper case,_,one2,One3,_one, variable will store the elements in variable age=18
#print and input in python:-input taking data for users(scan off), output is displaying data to user(print off) 
#data types:-1)nmbrs-int(1,2,4,5),2)words-string'sagar'"",3)bool(true or false) this is basic Dt or primitive Dt
#array type Dt- or secquencial Dt:4)set{} 5)tuple() 6)list[group of data] this store group of values
#7)dictionary: this store pair of key values {}                   float1.2,3.4. complex3+2j,1+4j.
#8)user defined Dt is also knows as classes by this python got the name as object oriented programming language
#in list functions:-[]in(certain element),index(element index),len(),append(element added last),max(),min(),sort(assending order),remove()
#in tuple:-() is sm like list but cannot be changed once it assigned(immutable nature) print(type(t)). this will run fastly compared to list functions:-len(),max(),min(),index() 
#in sets:-{}this is decleared by variables s r a. this wont create or remove duplicate values or repeated values. in sets there will not be indexes like list&tuple by this we cant update elements sm like tuple.in set they wont print in given order this will store by sort by itself to become faster.function:-max(),min(),len(),remove(),add()
#dictionaries:-{}stores pair of values key:value d = {'name':'sagar80','nationality':'india'} print(d['name']) in this we use key as a index to run adding2types,printer access2types function:-   max(),min(),len()    
#indentation:-maintaining space. in if or else we have give a tab or 4spaces to go inside statement.
#operators in python:-arithmetic operators(+add)(-sub)(*mul)(/divied)(%reminder(modules))(2**3=8 2power3 power calculation)(5/2=2.5float)(5//2=2int)
#                     conditional operators (==equal)(<lessthan)(>grt)(<=lessequal)(>=grtequal)(!=not equal)
#                     logical operators(this are used in between conditional operators) (and , or , not) (in , not in checking a element in or not in list) 
#                     Bitwise operators(is used in compler to run) (& and, | or, ^ xor)

#name = 'sagar'
#print(name)                      #sagar
#name = input('enter your name')                #we have to give our name
#print(name,'welcome to our channel')        #sagar welcome to our channel 
#
#print('hello world',end=' ')
#print('hello world')                         #hello world hello world  #this will give but print in same line some gap in same line
#
#v1 = 10 
#v2 ='sagar'
#v3 = 4.8
#v4 = true
#print(type(v1))                         #int
#print(type(v2))                         #str
#print(type(v3))                         #float
#print(type(v4))                         #bool
                #changeable bcz it has index values
#list:-[]
#     0,1,2,3,   4 ,    5
#arr=[1,2,3,4,'sagar','mine'] 
#print(type(arr))                          #list   #and it prints sm like we given
#print(len(arr))                          #this will print length
#print(4 in arr)                          #checking the value in list or not      #true
#req_index = arr.index(4)
#print(req_index)                         #this will show the 4 values index #sagar
#arr.append(15)
#arr.append(12)                  
#print(arr)                              #this will add 15,12 in last of the list values
#print(max(arr))                       #this will print max value in list
#print(min(arr))                       #this will print min value in list
#
#print('before sorting : ',end="")
#print(arr)                                 #this will show normal list
#arr.sort()
#print('after sorting : ',end="")
#print(arr)                                #this will show ascending order in list
#arr. remove(4)
#print(arr)                                #this will remove 4 from thie list
#arr[0]= 10                              #now the 1 is replaced by 10 (updated by index)
#
#tuple;-()     immutable it doesn't change the values
#t=(1,2,3,4)                      #used to work fast no need to update again
#print(type(t))                    #'tuple' we cant update the values 
#print(len(t))                     #this will show length
#print(min(t))                     #this will show min value
#print(max(t))                     #this will show max value
#print(t.index(4))                 #this will show index value of 4
#  
#sets:-{}               #remove duplicate values in set #this will save by sorting automaticaly
#s = {3,3,3,2,2,1,1}    
#print(s)                        #{1,2,3}
#s.add(8)                #adding new value in set.
#print(s)                #{1,2,3,8}   (no order,no duplicate values,no updates)
#print(len(s))           #this will show length
#print(max(s))           #this will show max value
#print(min(s))           #this will show min value
#
#dictionaries:-{}
#d ={'name':'sagar','nationality':'india'}
#print(d['name'])         #sagar       key is given by us
#d['name']='sagar'
#d.__setitem__('nationality','india')         #2 types of methods this will be added to sets
#print(d)
#print(d['name])

#print(d.get('name'))                #this will access the dic

#dic = {1:10,2:20,3:30,4:40}
#print(len(dic))                    #lenth  4
#print(max(dic))                    #max   4
#print(min(dic))                    #min   1
#
#arthematic operators:-
#a = 4
#b = 3
#add = a+b
#sub = a-b
#mul = a*b
#div = a/b
#power = a**b
#integer_div = a//b
#print(add)             #7
#print(sub)             #1
#print(mul)             #12
#print(div)             #1.3333
#print(power)           #64
#print(integer_div)     #1
#
#conditional operators:-
#a = 10
#b = 11
#print(a == b)          #false
#print(a<b)             #true
#print(a>b)             #false
#print(a!=b)            #true
#print(a<=b)            #true  
#print(a>=b)            #false
#
#logical operators: used between condition operators (and,or,not)
#true and true =true              true or true =true
#false and true =false            false or true =true                  c = true
#true and false =false            true or false =true                  print(not c)         #false    will be printed
#false and false = false          false or false =false
#
#in,not in
#l=[1,2,3,4,,5]
#print(4 in l)       #this will print True
#print(4 not in l)   #this will print False bcz 4 is inside the list
#
#if else statements (conditional statements) 
#name = input('enter your name:')                           #sagar
#age = int(input('enter your age:'))                        #17, 21
#if age<18:                                                 #name,'sorry you are not eligible!           (lessthen<)
#      print(name,'sorry you are not eligible!')            #hello',sagar,',you are welcome!
#else:  
#     print('hello',name,',you are welcome!')
#    #after run we have to give name and age then the output will be printed 17,21
#
#if elif else (if multiple conditions are there we use elif statement)
#marks = float(input('Enter your marks:'))
#if marks >= 90:
#   print('your grade is : A')                           #98    #'your grade is : 'A'
#elif marks >=80 and marks <90:                         
#   print('your grade is : B')                           #82    #'your grade is : 'B'
#elif marks >=70 and marks <80:                         
#   print('your grade is : c')                           #75    #'your grade is : 'c'                
#else: 
#   print('sorry, you are failed!')                            #'sorry, you are failed!'
#we have to give marks by printing that we can grade
#
#nested if statement using of if conditions inside multiple if conditions 
#name = input('enter your name:')              #sagar
#age = int(input('enter your age:'))           #23
#gender = input('enter your gender(M/F):')     #M
# -------space
#if age >=18:
#    if gender == 'M':
#        print('hello Mr.',name,',welcome!')
#     else:
#         print('hello Mrs.',name,',welcome!')
#else:
#   print('you are not Eligible!')                            #virat 25 M  anushka 24 F   user 15 M
#
#If main in python:-python will work on modules. each python file is called module.
##first.py file                        #second.py file
#import second                         #a=10
##modules                              -------space
#print(second.a)                        
#------space                           #if __name__ == '__main__':
# if __name__ == '__main__':                print('secondfile')
#       print('first file')  4y5

#loops introduction (if any work we have to do n number of times then we use loops) :1)for loop(is used mostly)(run for range) 2)while loop(it is continues for true or false)
#range function:  print(list(range(1,10)))    #(0,1,2,3,4,5,6,7,8,9)    #range(start,end,gap):   print(list(range(1,16,2)))   #(1,3,5,7,9,11,13,15)
#
#for i in range(1,10):                                                                     #1st type for i in range(1,21):
#       print(i,"sagar01")  sagar01 sagar02 sagar03 sagar04 sagar05 sagar9 .....                   //some code
#
#la = [1,2,3,4,5]                                                                         #2nd type la = [4,5,5]
#for value in la:                                                                          for value in la:
#       print(value)                      #1 2 3 4 5                                                          //some code
#
#la = [10,20,30,40,50]
#s = 0
#for value in la:                        print
#       s = s + value
#print('answer : ',s)                           #150
#
#to create a 5table by forloop
#t = int(input('Enter table number : '))
#for i in range(1,21):
#       print(t,'x',i,'=',t*i)  select no what table u want to print     #5 x 1=5....5 x 20=100 
#
#while loop (sm as for loop)
#i=0                                                       #whilecondition:
#while i<10:                                                               #//some code
#     print(i,'Hello')                                                    #//increment statement or decrement statement   (this line is imp whileloop)
#     i = i+1                   #(Hello............10tyms printed)
#
#Break and continue and pass  (if we want to stop suddenly our loop we use) this must be used inside if
#lan = ['user1','user2','user3','user4','user5']
#is_persent = False
#for name in lan:
#       if name == 'user3':                       #checking weather 3 present or not
#           is_present = True
#           break                                   #breaking the loop when we found our needy(time will be safed)
#if is_present == True:
#     print('user3 is present in the list!')
#else:           
#     print('user3 is not present in the list!')                     #user3 is present in the list!
#
#continue statement: this must used inside if (this is used to skip one nmbr and print another nmbr)
#for i in range (1,11):
#      print(i)               #this print all 1 to 10 nmbrs 
#      if i == 5:
#           continue
#       print(i)              #this print 1 to 10 but removes 5 (1,2,3,4,6,7,8,9,10)
#            break
#       print(i)               #1 2 3 4
#
#pass statement: this says there is no code but stay empty
#if condition:
#       pass             #(creating a empty statement)
# 
#functions in python:1)funtions is used to prevent the duplicate  code,well structured or (orgenaized way)  
#functions syntax:- 1)function creation  2)function calling (print(hello)) 
#1)def function_name(parameters):                    #def:-(short form for define)is keyword used to define a function
#       //code
#       return some_result
##ex:- a company 3 cate-
#manager = [34,56,78,98,]   `
#developer = [32,45,34,67,98]
#support_staff = [12,54,67,89.90,45,32]
#-----space 
#def get avg(arr):                               #function creation
#       n = len(arr)
#       sum = 0
#       for i in range(0,n):
#               sum = sum + arr[i]
#        return sum/n                             #(by using this we get avgs of 3 categires)
#---space                                                     
#print('Manger Avg : ',get_avg(manager))                      #55.0    #calling the function
#print('Developer Avg : ',get_avg(developer))                 #67.90
#print('support support Avg : ',get_avg(support_staff)        #65.00
# 
#type of functions:
#1) without parameters, without return value
#def welcome_msg():
#       print('hello, Nice to see your!')                 #(function creation)
#       print('welcome to our application!')
# ----space
#welcome_msg() 
#welcome_msg()           #(function calling)
#welcome_msg()           #the msgs will be printed for 4times
#welcome_msg() 
#
#2)without parameters, with return value
#def some_of_first_10_number()
#       sum = 0
#       for i in range(1,11)
#               sum = sum + i
#       return sum                    #(function creation)         
#----space
#answer = some_of_first_10_numberp()
#print(answer)                          #(function calling) #55
#
#3)with parameter, without return value
#def welcome_user(name,gender):                          #name and gender i are parameters
#       if gender == 'M':
#           print('welcome Mr.',name,', Have a nice day!')
#       else:
#           print('welcome Mrs.',name,',Have a nice day!')         #(function creation)
#------space
#name = input('Enter your name:')
#gender = inpu('Enter your gender(M/F)')                 #run the code by giving the name and gender one M and one F
#welcome_user(name,gender)                     #(function calling)                    #welcome mr. virat , have a nice day
#
#4)with parameter, with return value 
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
#recursion in python: is calling a function with in the sm function this is powerful (recursion works same as loops) is a stack this works backward calculation after base condition. loops works in forward and recursive is backward 
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
##ex:program in loops    ##finding the max value in the given list
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
##ex:-program on function concept (function,loop and list) used in student result
##45 89 76 54 98 67
#def get_grade(avg_marks):                             #function creation
#   if avg_marks>=90:
#       return 'A'
#   elif avg_marks>=80 and avg_marks<90:
#       return 'B'                                                      #grade marks code
#   elif avg_marks>=70 and avg_marks<80:
#       return 'C'
#   elif avg_marks>=60 and avg_marks<70:
#       return 'D'
#   else:
#       return 'E'
#-------space
#def get_average(marks_list):                            #function creation
#   sum = 0
#   n = len(marks_list)
#   for i in range(0,n):                                                #avg marks code
#       sum = sum + marks_list[i]
#   return sum/n                              
#----space
#def main():                                    
#       no_student = int(input('Enter Number of student's))
#       name_list = []
#       avg_list = []
#       for i in range(0,no_student):
#           name =input('Enter student name:')                                             #def main
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
#      main()                                                                              #main
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
#name :
#avg :
#grade:
#
##ex:-program on Dictionary concept:this is voting polling of cricketer now who is the best cricketer we have to check by python
#data = ['kohli','kohli','smith','williamson','poting','kohli','de_villars','kohli','smith','smith','ponting','ponting','ponting','kohli',
#        'kohli','ponting','kohli','de_villiars','kohli','de_villiars','poning','kohli','de_villiars','de_villiars','ponting',] 
#--------space                                                    
#my_dic = {}                                                  #kohli  :  8
#---------space                                               #smith  :  3
#for i in range(0,len(data)):                                 #williamson  :  1                              
#     temp = my_dic.get(data[i])                              #poting  :  1
#     if temp is None:                                        #de_villars  :  1
#          my_dic[data[i]] = 1                                #ponting  :  5
#     else:                                                   #de_villiars  :  4
#          my_dic[data[i]] = temp + 1
#---------space
#for player_name,votes in my_dic.items():
#    print(player_name,' : ',votes)
#
#strings intro in python:-''""
#v1 = 'strings in python'
#print(type(v1))                                                      #<class'str'>
##for character in v1:                                                 #s
#       print(character)                                               #t            if we assign a element in values it cant be changed or replaced
###print(v1[0])                                                        #s            print the element by using indexing
####for character in v1:                                                             computer only supports for numerical language thats y every element has one numeric value to store in computer
#       print(ord(character))                                                       (str works on aschii values a-z ->numerical) 115 116 114 105 110 103 115 32 105 110 32 112 121 116 104 111 110 shows the nmbrs
#print(chr(97))                                                        #a            (97=a)
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
#
#string applications and functions:-
#1)string slicing and join
#s = 'how are you?'
#print(s[0:3])                                             #how will printed in slicing this works on indexing          
#print(s[4:7])                                             #are
#l = [1,2,3,4,5]
#print(l)                                                 #[1,2,3,4,5]   slicing is also done in list
#print(1[0:3])                                            #[1,2,3]
#l = ['how','are','you?']
#print(l)                                                 #['how','are','you?']
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
#print(type(t))                                           #<class 'tuple'>                                                        #list to tuple, tuple to list,set to list,list to set
#
#3)fstring 
#a = 10
#b = 20                                             
#c = 30
#print(f'a : {a} , b : {b} , c : {c}')                    #a : 10 , b : 20 , c : 30
#s = f'{1+2} {3+4} {5+6}' 
#print(f'a : {a} , b : {b}, c : {c}')                     #3 7 11
#
#oops concept intro in python:object orinted programming by using oops concept nmbr of values printed by one function name (by using this concept 1)security 2)duplicate remove 3)re usability of the existing code 4)gives good structure)we can hide our data by that only cls lo vunna vale access chestharu
#Inheritance
#Polymorphism
#Encapsulation
#Abstraction
#
#classes in object in python(cls is user defined data types)(object is physical existance)(object orinted progremming)
#creation of a cls(class is a blue print or plan (cls is a combination of variables and methods)
#class student:                                 #class
#   def __init__(self,id,name,age):                 #contructor(self is arrgument)
#       self.id = id
#       self.name = name                         #variables
#       self.age = age
#------space
#   def print_id_name(self):                       #2nd one print only id and name    #function for calling
#       print(self.id,self.name)                   #this is function
#-------space
#v1 = student(1,'student1',18)                     #object creation           
#v2 = student(2,'student2',18)                    #parameters 3 we have given
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
#ex:-2 class student                         #class
#   def __init__(self,no,first,last,age):           #constructor
#     self.id = no                                   #cls is defined as user defined datatype prepared for user requirement
#     self.f_name = first                            #first give cls name give constructor in that give parameters or variable
#     self.l_name = last                             #after give cls methods it works on variable
#     self.age = age                                 #after creation of object 
#-----space                                          #after that we can cl objects
#   def print_id_name(self):                        #function for printing id and name
#       print(self.id,self.name)
#------space
#   def full_name(self): 
#       print(self.f_name,self.l_name)                #function for printing full name
#------space 
#v1 = student(1,'student','s1',18)                    #object creation
#v2 = student(1,'student','s2',18) 
#v3 = student(1,'student','s3',18)
#-----space
#v1.full_name()                                               #student s1
#v2.full_name()                                               #student s2       #object calling
#v3.full_name()                                               #student s3
# 
#static and normal variables: 
#class
#variables / attribute 
#1)normal class variables          (this has self key word)
#2)static variables                (this data works on complete class)
#class student:                     #class
#   school_name = 'xyz school' 
#--------space
#   def __init__(self,id,name):                #constructor
#       self.id = id
#       self.name = name
#------space
#   def show_data(self):                    #function
#       print(self.id,self.name)
#------space
#student1 = student(1,'user1')
#student2 = student(2,'user2')
#print(student1.school_name)                                       #xyz school          stataic variable
#print(student2.school_name)                                       #xyz school
#student1.show_data()                                              #1 user1              object cl
#student2.show_data()                                              #2 user2
#student.show_data(student1)                                       #1 user1              cls name tho cl
#student.show_data(student2)                                       #2 user2

#ex:program
#class amazon:                                    #class
#    overall_discount = 5                                         #static variable
#------space
#   def __init__(self,p_id,p_name,p_price,p_discount):      #constructor         #cls variable
#       self.id = p_id                                              #by seeing that self we can conclude that we can cl by object
#       self.name = p_name                                          #parameters
#       self.price = p_price
#       self.discount = p_discount
#----------space
#   def get_actual_price(self):             #100 - 10 - 5 =85                 #creat a function
#       final_price = self.price - self.price*self.discount/100 - Amazon.overall_discount*self.price/100
#       return final_price
#------space
#p1 = amazon(1,'product',100,10)                       #object creating by using functions                            
#p2 = amazon(1,'product',500,12)
#p3 = amazon(1,'product',1000,15)
#-----space
#print(p1.get_actual_price())                                          85.0
#print(p2.get_actual_price())                                          415.0            #calling a function
#print(p3.get_actual_price())                                          800.0
#
#static and class methods:
#class:-
#3variables
#normal variables
#static variables / class variables
##methods
#static methods:-this will be in cls but it can perform another operations we can cl by using object name as well as cls name
#class methods:- is changing the discount by adding one more decarator(@) def to it. we can only cl by using cls method
#class amazon:      #(not printed code)(static method)
#       #class variables                              class method:-(is common for the data that working on functions)
#       overall_discount = 5
#-------space
#   def __init__(self,p_id,p_name,p_price,p_discount):         #constructor             #self will be call by using objecct name
#       self.id = p_id
#       self.name = p_name                                      #variables
#       self.price = p_price
#       self.discount = p_discount
#   def get_final_price(self):                     #function
#       return self.price - self.price*self.discount/100 - amazon.overall_discount*self.price/100
#--------space
#   def print_data(self):
#     print('--------------')
#     print('id : ',self.id)
#     print('name : ',self.name)
#     print('final price : ',self.get_finnal_price())           #---------------------
#-------------space                                              #id :   1
#p1 = Amazon(1,'product1',500,8)                                 #name :  product
#p2 = Amazon(2,'product2',800,11)                                #final price  : 436.0
#------space                                                      ----------------
#p1.print_data()                                                #id  : 2
#p2.print_data()                                                #name : product2
#(not printed amazon code)                                      #final price  : 672.0
#                                                        
###@class method     #this is decarator @cls        #this works on the common data in the cls working on that function is known as cls method
#def change_overall_discount(clc,discount):                    cls decoration def  (we can only cl by using cls method)
#   clc.overall_discount = discount
#
#@staticmethod                     
#def print_something():                                      #static decoration def   (we can cl by using object name as well as cls name)
#    print('i am a static method')
#Amozon.print_something()                     #print function             #i am a static method                
#p1.print_something()                                                     #i am a static method              
#p2.print_something()                                                     #i am a static method
#(upto here not printed code)
#
#inheritance concept:- this is one of the opps concept. objecct orriented (1)used for code duplicate code remove 2)usage of existing code)(we use existing code for developing our need)
#example:-
#class A:                                #cls
#   def __init__(self,a_value):            
#        self.a = a_value
# ---------space                                #Aclass is parent cls of B
#   def print_a(self):                           #(constructor)
#    def print_a(self):                           
#       print('A value : ',self.a)
#-.------space
#class B(A):        #single level                        #B is the sub cls of A. b is taking all the properities of A i.e., inheritance      
#   def __init__(self,a_value,b_value):                   #(constructor)
#       A.__init__(self,a_value)
#       self.b = b_value
#----------space
#   def print_b (self):
#   print('B value : ',self.b)
#-----------space
#obj1 = b(10,20)                                     #A value : 10
#obj1.print_a()                                      #B value : 20
#obj1.print_b()  
#(not printed)
#
## ex:-1)single level inheritance:-occurs on one parent cls and one child cls. daily life ex:-
#class Driver:                      #cls                                              (driver class)
#   def __init__(self,f_name,age,mobile_no):             #constructor
#       self.f_name = f_name                              #variables
#       self.l_name = l_name
#       self.age = age
#       self.mobile_number = mobile_no
#--------space
#   def full_name(self):                                                   (to creat full name of driver function)
#       return f'{self.f_name} {self.l_name}'
#------space
#class license(driver):                                                     (license class driver ni inheritance after we have to give parent cls at 1st)
#   def __init__(self,f_name,age,mobile_no,license_id,validity_year):
#       Driver._init__(self,f_name,l_name,age,mobile_no):
#       self.license_id = license_id
#       self.validity_year = validity_year
#------space
#   def is _valid_license(self):                                                     (creating functions)
#       if self.validity_year >= 2021:
#           return True
#       else:    
#           return False
#-----------space
#user1_license = License('user','one',20,1234,101,2022)
#user2_license = License('user','two',22,2534,102,2021)
#------------space                                                                  user one
#print(user1_license.full_name())                                                   Eligibility of license : True         
#print('Eligibility of licence : ',user1_license.is_valid_license())
#
##2)Multi level inheritance:- if inheritance occurs between multilple clses then it says multiple inheritance
#class Driver:                                                         (driver class)
#   def __init__(self,f_name,age,nobile_no):
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
#class vehical(License):
#   def __init__(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):
#       License._init_(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year)
#       self.vehical_no = vechical_no
#       self.vehical_age = vehical_age
# ----space
#   def is_valid_driver(self):                                  (function)
#       if self.age>= 20:                                #by using dirver cls the work is reflected in vecical cls
#           return True
#       else:
#           return False
#------space
#vehical_one = vehical('user','one',21,2345,101,2022,202,2)
#--------space                                                                 if we given 2022                             if we given 2019
#print(Vehical_one.full_name())                                                #user one                                     #user one                                          
#print('License :',vehical_one.is_valid_license())                             #License : True                               #License : False
#print('Driver Eligible :',vehical_one.is_valid_driver())                      #Driver Eligible : True                       #Driver Eligible : True
#
##3)Multiple inheritance:-one cls ki multiple parent classes are present i.e, if we derive our cls from multiple classes is known as multiple inheritance
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
#        A.__init__(self)                                                                                              
#        B.__init__(self)
#        self.a = 1                
#-----space
#obj = C()
#print(obj.a)                   #1 wiii be printed if we remove that 100 will print if we remove that 10 will be printed
##class Driver:                                    #(driver class)
#   def __init__(self,f_name,age,nobile_no):
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
#   def __init__(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):
#       License._init_(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year)
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
#multiple inheritance
#class Bus(Vehical Diesel):                 #cls                                                                                        we can use multiple vehicals once we written he code while changing the vehical we can get
#   def __init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age,price,wheels):
#       vehical.__init__(self,f_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age)
#       Diesel.__init__(self,price)
#       self.wheels = wheels
#------space
#bus = Bus('user','one',21,2345,101,2022,201,2,100,6)                #object creation
#------space
#print('driver name :',bus.full_name())                                              #driver name : user one
#print('license valid : ',bus.is_valid_license())                                    #license valid : True
#print('driver eligible :',bus.is_valid_driver())                                    #driver eligible : True
#print('price of fuel per liter :',bus.price)                                        #price of fuel per liter :100
#
##4)Hirarchical and Hybrid inheritance:-oka cls ni multiple class derive chesukodam 
#A parent
#B(A)                   oka cls ki multiple child having is called hierarchical inheritance
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
#   def __init__(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year,vehical_no,vehical_age):
#       License._init_(self,f_name,l_name,l_name,age,mobile_no,license_id,validity_year)
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
#multiple inheritance
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
#multiple:
#parent : vehical,diesel
#sub : bus
#hibrid inheritance:
#combination of atleast two inheeritance type is called hybrid inherintance
#(we use code once agian existing code but we can't repeat code for this reason inheritance is very powerful
#
#5 types in inheritnace:-
#1)single level inheritance - one parent and one sub class
#2)multi level inheritance -A -> B -> C (this is in chain reaction)
#3)multiple inheritance - one sub class having multiple parents
#4)heirarchical inheritance - okate parent cls ki multiple child clses having. oka parent cls ki multiple sub clses vunte hierarchical inheritance
#A parent
#B(A)
#c(A)
#c(A)
#D(A)
#5)hybrid inheritance - combinaton of atleast two inheritance  types is called hybrid inheritance
#
##polymorphism:-it refers to the use of a single type entity.(is one of the oops concept):-different ways 1)method overloading(function name is same but handling different data by polymorphism.1)) 2)method overriding
#1)Method overloading:(this can handel different no.of parameters and different type of data )
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
#print(len(l))                           #4
#print(len(s))                           #12
#
#Method overriding-polymorphism:in sm cls this method will take from last rewritten code
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
#ex:-
#class A:
#   def __init__(self,a,b):
#       self.a = a
#       self.b = b
#-------space
#   def __str__(self):
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
#       return self.a + other.a
#-------space
#obj1 = A(10)
#obj2 = A(20)
#-----space
#print(obj1+obj2)                                   #30
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
#           return False                             #False
#
#obj1 = A(10)
#obj2 = A(20)
#-----space
#obj3 = obj1 + obj2
#print(obj3)                                    #30                                                                          
#print(obj3.a)                                  #here we get address of obj and new obj created and new obj printed 30 this is for addition operation
#print(obj1>obj2)                               #true
#print(obj1>obj2)                               #false
#
#Encapsulation:- (imp concept in oops in python) is the process of combining attributes and methods with in the class.is used for protection the data.
#Data protection 
#public
#private                   #__a means private
#       only class methods and inside the class
#protected                  #_protected   
#       inside class + its subclass
#class A:                      #cls
#   def __init__(self,a,d):
#       self.__a = a #private
#       self.__b = b #private
#------------space
#   def show_data(self):
#       print('a : ',self.__a)
#       print('b : ',self.__b)
#---------space
#obj1 = A(10,20)                                              #a : 10
#obj1.show_data()                                             #b : 20
#class A:
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
#from abc import ABC,abstractmethod
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
#
#Lambda functionsm in python:- this is single line function. only present in python. we cant add no of codes in it. we can only return one operation (a+b) (a*b) (a-b). simple way to writting the functions
#normal function:we can add n lines of codes in one function.  (a+b),(a*b),(a-b)
#def function1(a,b):
#   return a+b            
#   sub = a-b                                     #-1
#print(hello)                                     #hello
#print(function1(2,3))                            #5 #(normal function(in this function we can write multiple operations))
#
#lambda function:                           #(in this we can only do one operation)(this mostly used in (map function or iteratable ))
#x = lambda a,b : a+b
#print(x(1,2))                                      #3 here we can parameters thrn sm value  returned
#l = [1,2,3,4,5,6] 
#multiple_ten = lambda a : a*10
#print(list(map(multiple_ten,1)))                    #[10,20,30,40,50,60] lambda function with amp function 
#
#Threadingin python:-to decrease the tym to run the multiple codes. we use threading 
#import time                                   #this time module
#print(time.time())                             #1668579707.751314 #this shows the time in secs
##without using threading concept:
#import time

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
#print('timetaken : ',time.time()-initial_time)
#
##with using threading concept:-
#import threading                                       #(this is inbuilt module in python)                                    
#import time

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
#l = [1,2,3,4,5]                                                          #Time taken : 1.0433464050292968          ##this program running ki 1min thisukundhi with using threading
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
#about()                                                #welcome to about section of our website
#
#Generators in python: sm like functions which contain yield keyword. in this we dont use return statements.multiple values retuned here we use yield statement instead of return statement avthye
#def f2():                                                          #1
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
#1)compiler error
#if True:          by using compiler                                    #if True
#print('hello')     we can get indentation errors                       #print('hello')
#2)run time  error (or) exception handling
#a = int(input('Enter a value:'))                          #4             #2
#b =  int(input('Enter b value:'))                         #5             #0
#d = a/b                                                   #0.8           #zeroDivisionError
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
#print('I am finally block, i donnot care any one')                   #I am finally block, i donnot care any one
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
#
#
#
#
#
#
#telusuko(python)
a=10
b=20                                #30
print(a+b)
print(2 + 3)                         #5
print(9 - 8)                          #1
print(4 * 6)                         #24
print(8 / 4)                         #2.0
print(5 / 2)                         #2.5
print(5 // 2)                        #2
print(8 + 2 * 3)                     #14
#print(8 + 2)*3                      #30
print(10 / 3)                        #3.3333333333333335
print(10 // 3)                       #3   (quataiont)
print(10 % 3)                        #1    (remainder)

print('sagar')                       #sagar
print("sagar's laptop")              #sagar's laptop
print('sagar "laptop"')              #sagar "laptop"
print('sagar\'s "laptop"')           #sagar's "laptop"
print('sagar + sagar')               #sagar + sagar
print(10 * 'sagar')                  #sagarsagarsagarsagarsagarsagarsagarsagarsagarsagar
print('c:\docs\sagar')               #c:\docs\sagar
print(r'c:\docs\sagar')              #c:\docs\sagar

#variables
a=10
b=20 
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

#list[] adding different values ex:strings+numbers group. them together we can add,remove,update values. we can change values 
nums = (1,2,4,6,77,88)
print(nums)                      #(1, 2, 4, 6, 77, 88)
print(nums[2])                   #4
print(nums[1:])                  #(2, 4, 6, 77, 88)
print(nums[-2])                  #77

names = ['sagar', 'ram', 'raj']
print(names)                       #['sagar', 'ram', 'raj']

mil = [names,nums]                       
print(mil)                         #[['sagar', 'ram', 'raj'], (1, 2, 4, 6, 77, 88)]

nums = [1,2,3,4,5,66,77,88]
nums.append(99)
print(nums)                       #[1, 2, 3, 4, 5, 66, 77, 88, 99]
nums.insert(2,99)
print(nums)                       #[1, 2, 99, 3, 4, 5, 66, 77, 88, 99]
nums.remove(4)
print(nums)                       #[1, 2, 99, 3, 5, 66, 77, 88, 99]
nums.pop(2)
print(nums)                       #[1, 2, 3, 5, 66, 77, 88, 99]
nums.pop()
print(nums)                       #[1, 2, 3, 5, 66, 77, 88]
del nums[2:]
print(nums)                       #[1, 2]
nums.extend([12,34,56,78,90])
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
s = {22,25,14,21,5}                   #sm like list sets cant printed by sequence and not duplicate {} collection of unique nmbrs. indexing notsupported
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
#when we have data in your memory which will not be used or taged by any variable collected by garbage collector
'''
for i in range (1,101):                 #1 to 100 will be printed
    print(i)
for i in range (1,100):                 #even nmbrs 1 to 100 printed
    if i%2 == 0:  
        print (i) 
for i in range (1,100):                 #odd nmbr 1 to 100 printed
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
'''

print (0.1 + 0.2 == 0.30000000000000004)          #True
print (0.1 + 0.2 == 0.3)                          #false


#corey schafer pyton:-
#python --version (for checkin py version)
#s = 'bobby\'s world'        or   "bobby's world"
#print(s)              #bobby's world
#s = 'hello world'
#print(s[0:5])       #hello   
#print(s.lower())
#print(s.upper())
#print(s.count('l'))   #3
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
#
#
#
#
#