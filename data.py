#data types in python:-
#none : variable not assigned
#numeric: int(1,2,5,8) float(1.2,1.4,1.6) complex(2+5j,3+6J) bool(True,false)
#list
#tuple
#set                     :this all are sequence
#string
#range

#dictionary

a = 5.6                   #5.6
print (a)
b = int(a)                
print(b)                 #5    
k = float(b)
print (k)                #5.0
s = 6
c = complex(b,k)   
print (c)               #(5+5j)
b = 3
k = 4
print (b>k)             #False
print (b<k)             #True
print (bool (b<k))      #True

lst = [1,2,3,4,5,]
print (type(lst))       #<class 'list'>    list []

s = {25,34,56,78,56,34}
print (s)                   #{56,25,34,78}  sets{}
print (type(s))             #<class 'set'>

tup = (1,2,33,44,55)           
print (tup)                #(1, 2, 33, 44, 55)    tuple()
print (type(tup))          #<class 'tuple'>

st = 'sagar'
print (st)                  #sagar             string(""'')
print (type(st))            #<class 'str'>

range(10)
print (range(0,10))          #range(0, 10)
print (list(range(10)))      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (list(range(2,10,2)))  #[2, 4, 6, 8]
print(type(range(10)))       #<class 'range'>
  

d = {'sagar':'mi','rahul':'iphone','ragas':'sam'}  
print(d)                       #{'sagar': 'mi', 'rahul': 'iphone', 'ragas': 'sam'}
print (d.keys())               #dict_keys(['sagar', 'rahul', 'ragas'])
print (d.values())             #dict_values(['mi', 'iphone', 'sam'])


