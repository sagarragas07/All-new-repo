#strings '""'''
s='sagar'
s1="python life"
s2='''
this 
is 
string
'''
print(type(s))                         #<class 'str'>
print(type(s1))                        #<class 'str'>
print(type(s2))                        #<class 'str'>

h=s2.replace("is",'are')             #replaceing there
print(h)                             #there
                                     #are 

h=s2.upper()                         #THIS
print(h)                             #IS        
                                     #STRING      


h=s2.lower()                         #this
print(h)                             #is          
                                     #string

h=s2.strip()                         #this
print(h)                             #is          
                                     #string 


h=s2.split()                         #this converts strg to list
print(h)                             #['this', 'is', 'string']      
                                     
print(s1.startswith('p'))             #true
print(s1.startswith('k'))             #False 

print(s1.endswith('e'))               #true
print(s1.endswith('i'))               #false

print('my name is {}'.format('sagar'))       #my name is sagar

print(s2.count('is'))                        #2
print(len(s2))                               #18

#sets in python
s={}
print(type(s))                               #<class 'dict'>

s={1,2,3,4,43}
print(type(s))                               #<class 'set'>

s={1,2.2,'sagar'}
s.add('python')                              #{'python', 1, 2.2, 'sagar'}
print(s)

s={1,2.2,'sagar'}
s.update(['python'])                          #{1, 2.2, 'python', 'sagar'}
print(s)

s={1,2.2,'sagar'}
print(len(s))                                #3

s={1,2.2,'sagar',1}
print(s)                                     #{1, 2.2, 'sagar'} it wont take repeated values

s={1,2.2,'sagar'}
s.remove('sagar')                          #{1, 2.2,}
print(s)

a1={1,2,3,4,5,6}
a2={5,6,7,8,9,100}                          #{1, 2, 3, 4, 5, 6, 100, 7, 8, 9} or a1|a2
print(a1.union(a2))

a1={1,2,3,4,5,6}
a2={5,6,7,8,9,100}                          #{5, 6}
print(a1.intersection(a2))

a1={1,2,3,4,5,6}
a2={5,6,7,8,9,100}                          #{1, 2, 3, 4} only a1 will be shown
print(a1.difference(a2))

a1={1,2,3,4,5,6}
a2={7,8,9,100}                              #True
print(a1.isdisjoint(a2))

a1={1,2,3,4,5,6}
a2={5,6,7,8,9,100}                           #False
print(a1.isdisjoint(a2))

a1={1,2,3,4,5,6}
a2={1,2,3,4,5,6}                             #True opp to disjoint
print(a1.issubset(a2))


a1={1,2,3,4,5,6}
a2={7,8,9,100}                           #False
print(a1.issubset(a2))


#dictionery in python:
dic={}
print(type(dic))                             #<class 'dict'>

dic={'name':'sagar','age':23}
print(dic)                                   #{'name': 'sagar', 'age': 23}

dic={'name':'sagar','age':23}
print(dic['name'])                           #sagar   keys will be always uniqe

dic={'name':'sagar','age':23}
print(dic['name'])                           #sagar   keys will be always uniqe

dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
print(dic['phno'])                           #[957337, 834688947893, 873834, 3986893]

#functions
dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
dic.pop('name')
print(dic)                                  #{'age': 23, 'phno': [957337, 834688947893, 873834, 3986893]}pop will remove

dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
dic.update({'address':'hyd'})
print(dic)                                  #{'name': 'sagar', 'age': 23, 'phno': [957337, 834688947893, 873834, 3986893], 'address': 'hyd'}

dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
dic.clear()
print(dic)                                  #{} clears all

dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
print(dic.keys())                           #dict_keys(['name', 'age', 'phno']) shows key values

dic={'name':'sagar','age':23,'phno':[957337,834688947893,873834,3986893,]}
print(dic.values())                           #dict_values(['sagar', 23, [957337, 834688947893, 873834, 3986893]]) shows values 


#functions                                            arguments and parameters are same
def functionname():
    print("this is function")                        #this is function
functionname()    

def functionname(name):
    print("this is function",name)                 #this is function sagar single argument 
functionname('sagar')  

def functionname(name,age):
    print("this is function",name,age)                #this is function sagar 23 multiple argument
functionname('sagar',23)

def functionname(a,b):
    return a+b                                      #4 this is build by return functions ki we have to use returns as a good programmer
w=functionname(1,3)                                       
print(w)

def functionname(a):
    return a*3                                     #9
print(functionname(3))       

def functionname(a):
    pass                                           #ntng will be displayed


def functionname(a):                                #1       as we can send str,tupple,list
    for i in a:                                     #2     in this sending list to function
        print(i)                                    #3     function lopala forloop ela rasthamu
functionname([1,2,3,4,5])                           #4


def functionname(*a):                           #(1, 2, 3, 4, 5, 6, 7)
    print(a)                                    #this is orbitery argument by  using this * all converated as tupple and saved
functionname(1,2,3,4,5,6,7)    

def functionname(**a):                          #{'name': 'sagar', 'age': 23}
    print(a)                                    #this is keywords argument by  using this ** saved as dic formate
functionname(name='sagar',age=23) 


#file handling in python
#read,write,append
f = open('sagar.txt','r')                           #first we have to creat a file.txt write something init
content = f.read()                                  #name that file with variable f and push it to content give fun  
print(content)                                      #print the content and close it #this is file
f.close()

f = open('sagar.txt','w')                            #13 
content = f.write('this is write') 
print(content)                     
f.close()

f = open('sagar.txt','r')                          
content = f.read()                                  #this is write
print(content)                                      #this write mode is replaced this is file to this is write
f.close()

f = open('sagar.txt','a')                            #by using this a we can store our files without replaceing
content = f.write('this is sagar') 
print(content)                     
f.close()

f = open('sagar.txt','r')                          
content = f.read()                                  #this is writethis is sagar
print(content)                                      #this append mode store everying
f.close()

#error handling in pythone
try:
    print(x)                                     #except (try is through into except)
except:
    print('except')

try:
    print(x)                                     #name 'x' is not defined (we can text our execption)
except Exception as e:
    print(e)

try:
    print(x)                                     #this is finally
except Exception as e:
    print(e)   
finally:
    print("this is finally")

x=0
try:
    print(1/x)                                     #division by zero
except Exception as e:                             #this is finally
    print(e)   
finally:
    print("this is finally")

x=-1
if x<0:                                               #Exception: the is raise
    raise Exception("the is raise")   

    
    
     