
for i in 'sagar':                       #s
    print(i)                            #a
                                        #g
                                        #a
                                        #r

sagar=[1,2,3,4,5]                       #1
for ragas in sagar:                     #2
    print(ragas)                        #3      
                                        #4 
                                        #5
'''
sa=[1,2,3,4,5]                           #1
sum=0                                   #2
                                        #3
                                        #4           
for i in sa:                             #5
    sum=sum+i
    print(sum)
    
 
sa=[1,2,3,4,5]                               #1
sum=0                                       #3
                                            #6
                                            #10
for i in sa:                                 #15
    sum=sum+i
    print(sum)
 '''   
#range function                             #1
for i in range(1,10,2):                     #3
    print(i)                                #5
                                            #7
                                            #9
for i in range(0,20,5):                     #0
    print(i)                                #5
                                            #10
                                            #15
#forloop
mobiles=['iphone','oneplus','mi','realme','samsung',]     #this is iphone
for i in mobiles:                                          #this is not iphone
    if i =='iphone':                                       #this is not iphone
        print('this is iphone')                            #this is not iphone
    else:                                                  #this is not iphone    
        print("this is not iphone")                                

#whileloop
c=0                                                        #c is 1
while c<3:                                                 #c is 2
    c+=1                                                   #c is 3
    print("c is",c)                                        #completed
else:
    print("completed")    


#tuple handson
sagar=(1,2,3.3,'sagar')
print(type(sagar))                                      #tuple

sagar=(1,2,3.3,'sagar')                                 #sagar
print(sagar[3])


sagar=(1,2,3.3,'sagar')                                 #(1, 2, 3.3, 'sagar', 1, 2, 3.3, 'sagar') repeating
print(sagar*2)


sagar=(1,2,3.3,4)
a=(1,2,3,4,5)                                           #(1, 2, 3.3, 4, 1, 2, 3, 4, 5) concatration
print(sagar+a)


sagar=(1,2,3.3,4)
a=(1,2,3,4,5)                                           #True membership
print(2 in a)

sagar=(1,2,3.3,4)
a=(1,2,3,4,5)                                           #false membership
print(8 in a)

sagar=(1,2,3.3,4)                                      #1
a=(1,2,3,4,5)                                          #2
for i in a:                                            #3interation
    print(i)                                           #4
                                                       #5
#functions
sagar=(1,2,3.3,4) 
print(min(sagar))                                      #1(min)

sagar=(1,2,3.3,4) 
print(max(sagar))                                      #4(max)

sagar=(1,2,3.3,4) 
print(sum(sagar))                                      #10.3(sum)


sagar=(1,2,3.3,4) 
print(sorted(sagar))                                      #[1, 2, 3.3, 4]


#continue and break statement
for val in 'sagar':
    if val=='i':
        break                                          #the end
    print(val)
print("the end")        

for val in 'sagar':                                    #s
    if val=='a':                                       #g
        continue                                       #r                                         
    print(val)                                         #the end
print("the end")                                       


