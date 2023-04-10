#typefunction
a=10
b=2.3
c='sagar'
d=3+2j
f=True

print(type(a))                      #<class 'int'>
print(type(b))                      #<class 'float'>
print(type(c))                      #<class 'str'>
print(type(d))                      #<class 'complex'>
print(type(f))                      #<class 'bool'>


#typeconversion

num=20
d=str(num)                          #inttostrconverted
print(d)                            #inttostr
print(type(d))
'''
num='sagar'
d=int(num)                          #strtoint not converted
print(d)                            #invaild strtoint
print(type(d))

num='20'
d=int(num)                          #strtoint not converted                 
print(d)                            #it wont convert from strtoint
print(type(d))
'''
num = 1.2
print(type(num))                #<class 'float'>
d=int(num)                      #1
print(d)                        #<class 'int'>       
print(type(d))

#comments 1single#  2multiple"""  """ or '''  '''

a=10                           #a is int var
b=20
c=a+b                          #add       
print(c)                       #30

#control statements 1)conditional statements:

1 # a==b
2 # a!=b
3 # a<=b
4 # a.=b

a=1
b=3
if a>b:
    print("a is smaller than b")           #a<b a is smaller than b
elif a>b:
    print("a is smaller than b")           #a<b a is smaller than b
else:
    print("b is smaller than a")           #b is smaller than a


a=1
b=22
if a<b: print('this is short hand if')          #this is shor hand if
  
a=1
b=22
print ('this is short hand if') if a<b else print('this is short hand if else')         #this is short hand


if True:
    print('this is if')           #this is if    
if False:
    print('this is if')
else:
    print('this is else')         #this is else
  
#logical ops

a=200
b=33
c=500
if a>b and  c>b:
    print('and')                #and

else:
    print('else')    

a=200
b=33
c=500
if a>b and  c<b:
    print('and')                    #else

else:
    print('else') 
 

a=200
b=33
c=500
if a>b or  c<b:
    print('or')                    #or

else:
    print('else') 

a=200
b=33
c=500                       #ntng
if b<a:
    pass


