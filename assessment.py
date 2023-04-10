#python Assessment
#1.Find the Second maximum score from the Given List
list = [28, 29, 40, 45, 99,100,101,120]
list.sort()
print("Second largest element is:", list[-2])                           #output:-101

#2.Output Reverse Pyramid of Numbers from given number 
#Sample n = 5              

n=5
                                                                          #5 4 3 2 1
for i in range(n, 0,-1):                                                  #4 3 2 1
    for j in range(i, 0,-1):                                              #3 2 1
        print(j, end=" ")                                                 #2 1
                                                                          #1
    print()

#3.Check If String is Palindrome or not
string=input("Enter string:")
if(string==string[::-1]):                                         #if string is palindrome the string is a palindrome will be printed
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")                          #if string is not palindrome the string isn't a palindrome  will be printed     

#4.Read a CSV file using pandas. Get & print the following respective o/p’s in the console(Attached in email)
#a.Find the most expensive car company name.
import pandas as pd 
data = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\Automobile_data csv.csv")
print(data)
df1=pd.DataFrame(data)
print(df1)
df1 = df1 [['company','price']][df1.price==df1['price'].max()]
print(df1)                                                                 #5  mercedes-benz  45400.0 printed

#b.Print All Toyota Cars details
import pandas as pd 
df = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\Automobile_data csv.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)                                                          #All Toyota Cars details printed

#c.Count total cars per company
import pandas as pd
df = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\Automobile_data csv.csv")
print(df['company'].value_counts())                                       #Count total cars per company printed

#d.Find each company’s highest price car
import pandas as pd
df = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\Automobile_data csv.csv")
car_Manufacturers = df.groupby('company')
pricedf = car_Manufacturers['company','price'].max()
print(pricedf)                                                             #each company’s highest price car printed

#5.Define a class which has the following string transformation methods.
#a.Convert to lower case
list=("i love my india")
print(str.lower(list))                                  #i love my india

#b.Convert to upper case
list=("i love my india")
print(str.upper(list))                                 #I LOVE MY INDIA

#c.Capitalize only first word
s = "aws data engineer associate"
star = s.title()
print(star)                                            #Aws Data Engineer Associate

#d.Split the given input using delimiter
input = 'sagar ragas ram rahman'
print(input)
print(input.split())
print(type(input.split()))                              #['sagar', 'ragas', 'ram', 'rahman']
                                                        #list





#index.html to host a static website   
#<html> 
#     <head>
#        <title>My First Webpage</title>
#     <head>
#     <body>
#        <h1>I love coffee</h1>
#        <p>Hello world</p>
#     </body>
# 
#     <img src="coffee.jpg" width=500/>
#</html>
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
# 
# 
# 
# 
# 
# 
# 
#                                                      