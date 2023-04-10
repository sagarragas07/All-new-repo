sagar=[1,2.2,'sagar',True]                    #[1, 2.2, 'sagar', True]
print(sagar)

sagar=[1,2.2,'sagar',True]                     #[1, 2.2, 'sagar', True,1]
sagar.append(1)
print(sagar)

sagar=[1,2.2,'sagar',True]                     #list
sagar.append(1)
print(type(sagar))

sagar=[1,2.2,'sagar',True]                     #[1, 2.2, 'sagar', True, 1, 2, 4, 6, 8]
sagar.extend([1,2,4,6,8])
print(sagar)

sagar=[1,1,2.2,'sagar',True]                     #[1, 'python', 2.2, 'sagar', True]
sagar.insert(1,'python')
print(sagar)

sagar=[1,1,2.2,'sagar',True]                     #3
print(sagar.count(1))

sagar=[1,1,2.2,'sagar',False]                     #2
print(sagar.count(1))

sagar=[1,1,2.2,'sagar',True]                     #5
print(len(sagar))

sagar=[1,1,2.2,'sagar',True]                     #pop means 1 deleted [1, 2.2, 'sagar', True]
sagar.pop(1)
print(sagar)

sagar=[1,1,2.2,'sagar',True]                     #[True, 'sagar', 2.2, 1, 1] print in reverse
sagar.reverse()
print(sagar)

sagar=[1,2,3,55,4,8,5,66,77,888]                 #[1, 2, 3, 4, 5, 8, 55, 66, 77, 888] assending order
sagar.sort()
print(sagar)

sagar=[1,2,3,55,4,8,5,66,77,888]                  #for loop 1
for i in sagar:                                   #2
    print(i)                                      #3

sagar=[1,2,3,[55,4,8,5],66,77,888]                 #55 nextlist
print(sagar[3][0])










