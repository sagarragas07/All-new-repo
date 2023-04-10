#import pandas as pd                 #in cmd pip install pandas            py --version                                         python3.10 -m venv studysession
#import numpy as nm                  #in cmd pip install numpy             py -m pip --version  (pip installed)                 pip3 install --upgrade pip
#1)it is a high performance data analsis tool                              py -m pip install numpy  (numpy installed)           pip3 install pandas      
#2)it is used for working with large data sets                             py -m pip install --upgrade pip
#3)supports or load files with different formats(excel,csv)                py -m pip --version
#4)it is more flexiable to use                                             py -m pip install pandas
#5)the data represents in a tabular way(rows & columns)                    py -m pip install matplotlib
#6)pandas are sutiable for working on missing data 
#7)pandas used for indexing-slicing-subsetting the large data
#8)we can merge & join two different data sets easily 
#9)we can also reshape datasets.

#data structures:-
#1)series:-data represents one dimensional :-(list as a argument we can pass to series)  pd.Series(data,index)
#2)data frames:-data represents two demensional :-(list/dictionary/series/another dataframe we can pass to DF)  pd.DataFrame(data)  this is most efficient data structure to do analysis data sets.
#3)panel:-data represents multi deminsional :-pass the data   col             Rows                       (syntax of panel )
#                                        pd.panel(data,      major axis,     minor axis  ,dtype)                                                                   
"""
#1)Series data structure:-
import pandas as pd
ls=[1,2,3,4,]                                #0 1        9
a = pd.Series(ls)                            #1 2        8
print(a)                                     #3 4        6
print(type(a))                               #padas.core.series.series
pd.Series(ls,index=['9','8','7','6'])
print(a)

#2)DataFrame structure:-                                  #no  name   percentage  loc   study
dic = {'name':['sagar','raju','venu'],                    #0  sagar    90        rdm    btech
'percentage':[90,89,88],                                  #1  raju     89        kphb   degre
'loc':['rdm','kphb','hyd'],                               #2  venu     88        hyd    inter
'study':['btech','degre','inter']}

df = pd.DataFrame(dic)                                         
print(df)
print(type(df))                                             #<class 'pandas.core.frame.DataFrame'>
pd.DataFrame(dic,index=[7,8,9])
df.to_csv('sagar.csv')                                      #this will create sagar.csv file                         
#3)panel structure:-
"""
"""
#different ways to create Series in pandas
#1)empty Series:-
import pandas as pd                                             #empty series is created
sd = pd.Series()                                                #Series([], dtype: float64)
print(sd)

#2)to create series using a list:-                           #0 10     a
ls = [10,20,30,40]                                           #1 20     b    #here the index value is changed
sd = pd.Series(ls)                                           #2 30     c    #series using list created
print(sd)                                                    #3 40     d    #list is kama seperated values unclosed square brackets
sd = pd.Series(ls,index=['a','b','c','d'])  
print(sd)

#3)to create series using array
import numpy as np                                 #[ 60  70  80  90 100]
a = np.array([60,70,80,90,100])
print(a)                                            #0         60
sa = pd.Series(a)                                   #1         70        #arrays are space encloded with square brackets              
print(sa)                                           #2         80                  by using array series is created
                                                    #4         100

#4)to create series using dictionary:-              #a         10
dic = {'a':10,'b':20,'c':30,'d':40}                 #b         20                 in this type the index we give bcz 
sk = pd.Series(dic)                                 #c         30                  dic is key:value type
print(sk)                                           #d         40

#to create series using dictionary with list of tuples:-
dt = [('a',10),('b',20),('c',30),('d',40)]                # the complete tuple will be considered as single element
sm = pd.Series(dt)                                        #0  (a, 10)                             
print(sm)                                                 #1  (b, 20)                             
                                                          #3  (d, 40)
#different ways to create dataframes in pandas
#1)load the DF excel file:- df=pd.read_excel("path")   print(df) the data will represented by rows & columns including with indexes.
import pandas as pd                           #(before running this code install in terminal (python -m pip install openpyxl))
d = pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\new.xlsx")        
print(d)                              #the data will be read in xlsx by using the path
df=pd.DataFrame(d)
print(df)                             #now creating a DataFrame by passing argument with complete details we get data  
#
#2)load the DF csv file:- df=pd.read.csv("path")      print(df) the data will represented by rows & columns including with indexes.
data = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\nextcsv.csv")
print(data)                            #the data will be read in xlsx by using the path 
df1=pd.DataFrame(data)
print(df1)                             #now creating a DataFrame by passing argument with complete details we get data  
#
#3)create DF using dictionary:- df=pd.dataFrame(df) frame=pd.DataFrame(dic) the dic is converted to DF
data1 ={'name of student':['sagar','ragas','ram'],
'roll no':[101,102,103],
'Telugu':[98,96,90],
'English':[95,87,95,]}
print(data1)                            #the dictionary was created
df2=pd.DataFrame(data1)
print(df2)                              #now creating a DataFrame by passing argument with complete details we get data
#
#4)create DF using list of tuples:- df=pd.dataframe(data) frame=pd.DataFrame(data) the data will be given in (data=excel,csv,dic)
ls=[("abc",10,89,2),("def",11,79,3),("klm",12,65,4)]
print(ls)                            #[('abc',10,89,2),('def',11,79,3),('klm',12,65,4)]
df = pd.DataFrame(ls)                #    0   1   2  3 
print(df)                            #0  abc  10  89  2 
                                     #1  def  11  79  3
                                     #2  klm  12  65  4
"""
"""
#Attributes of series in pandas:
#index - series.index - return all index values
import pandas as pd
s = pd.Series([10,20,30,40,50],name="Numbers") 
print(s)                                             #series is created with default indexing (it will return the given values for the given values)
print(s.index)                                        #RangeIndex(start=0, stop=5, step=1) this will show the index range

#array - series.array - return an array of values
print(s.array)                                       #<PandasArray>
                                                     #[10, 20, 30, 40, 50]
                                                     #Length: 5, dtype: int64

#values - series.values - return values of series
print(s.values)                                      #[10 20 30 40 50]

#name - series.name - return name of series
print(s.name)                                        #Numbers

#shape - series.shape - return the shape
print(s.shape)                                       #(5,)

#ndim - series.ndim - returns the dimension of series
print(s.ndim)                                        #1

#size - series.size - return the size of series
print(s.size)                                        #5

#nbytes - series.nbytes -returns the memory occupiesd by values
print(s.nbytes)                                      #40

#memory-usage() - series.memory-usage() - return memory occupied by both index & values
print(s.memory_usage())                              #168

#empty - series.empty - returns true - if series is empty
#                       returns false - if series is not empty          
print(s.memory_usage(index=False))                  #40
print(s.memory_usage(index=True))                   #168
s1 = pd.Series()
print(s1)                                           #Series([], dtype: float64)
print(s1.size)                                      #0
print(s1.empty)                                     #True
"""
"""
#Mathematical operations Functions on Series in pandas (for this we have to create 2 different series)
import pandas as pd
a=pd.Series([10,20,30,40,50])
b=pd.Series([5,4,3,2,1])
print(a)
print(b)
print(a+b)#operator this will add a and b          #(or)   (a).add(b)function
print(a-b)#operator this will sub a and b          #(or)   (a).subtract(b)function
print(a*b)#operator this will  multiply a and b    #(or)   (a).multiply(b)function
print(a/b)#operator this will  module a and b      #(or)   (a).%(b)function
print(a<b)#operator this will  lessthan a and       #(or)  (a).le(b)function
print(a>b)#operator this will  greaterthan a and b  #(or)  (a).gt(b)function
print(a==b)#operator this will  == a and b          #(or)  (a).equal(b)function
print(a**b)#operator this will  power a and b          #(or)  (a).pow(b)function
"""
"""
#indexing and slicing:-
#uploading a record of DataFrame of excel file
import pandas as pd
d = pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")        
print(d)                              #the data will be read in xlsx by using the path
df=pd.DataFrame(d)
print(df)                             #now creating a DataFrame by passing argument with complete details we get data  

#data_frame.head(number_of_rows)
print(df.head())                          #first five rows(or)records will be dispalyed
print(df.head(2))                          #only top 2 rows(or)records displayed

#data_frame.tail(number_of_rows)
print(df.tail())                          #last five rows(or)records will be dispalyed
print(df.tail(2))                         #only last 10 rows(or)records displayed

#data_farme.describe()
print(df.describe())                     #shows detailed calculation of our df

#data_frame.shape
print(df.shape)                          #this shows the rows and columns in df(20,7)
print(df.columns)
print(df,['Roll_No'])                    #this will print rollno column
print(df,[['Roll_No','Telugu']])         #this will print rollno column and telugu column

#data_frame[satrt:stop:step]              #indexing
print(df[0:10:1])                         #1 to 10 rows will be displayed in df
#
#data_frame['column_name']
print(df["Name_of _Student"])             #we have to give particular name of the column then we get only particular data of a column in df
#
#data_frame[[column_1,column_2]]
print(df[["Name_of _Student","Telugu"]])        #now we get 2 columns detailes from df
#
#data_frame[[column_1,column_2]][start;stop:step]
print(df[["Name_of _Student","Maths"]][0:10:2])       #only 0,2,4,6,8 data displayed 2columns mixed rows displayed
#
#data_frame.iterrows()
for rec in df.iterrows():
    print(rec)                              #it shows induvudal values from df tuple format lo print ithadhi
for index,rows in df.iterrows():
    print(index,rows['Name_of _Student'])     #this will print the index and name column

#loc(stop index included)we use with column name:-
#data_frame.loc[row_number]
print(df.loc[5])                                  #the total 5th row is printed
#
#data_frame.loc[row_number,[column_name,...]]
print(df.loc[18,["Name_of _Student"]])             #the 19th row & name details printed
#
#data_frame.loc[start:stop]
print(df.loc[0:5])                                #0 to 5 rows&columns printed
#
#data_frame.loc[start:stop,"column_name"]
print(df.loc[0:5,"Name_of _Student"])               #0 and 5th columns printed
#
#data_frame.loc[start:stop,["column_1,column_2,...."]
print(df.loc[0:4,"Name_of _Student":"Science"])              #by giving the range the data will be printed
# 
##iloc(stop index excluded)column number:- #columns ni index tho axises chestham
#data_frame.iloc[rows_number,column_number]
print(df.iloc[0:4])                                        #0 to 3 rows&columns printed  
print(df.iloc[2,4])                                    #68 2column 4row printed
#data_frameiloc[row_start:row_stop,col_start:col_stop]        
#print(df.iloc[0:5,0:3])                                #this will print 4rows & 3 columns

#data_frameiloc[start:stop,"column_number"]
#print(df.iloc[0:4,2])                                  #this will print 4 rows and 2columns

#data_frameiloc[[row_1,row_2,....]]
#print(df.iloc[[1,2,3]])                                  #this will print 3 rows

#data_frameiloc[[col_1,col_2,....]]
#print(df.iloc[:,[1,2,3]])                                  #this will print 3 columns

#data_frameiloc[:,[col_1,col_2,....]]
#data_frameiloc[[start:stop,[col_1,col_2....]]

# 
#Sorting DataFrame(by column)in Pandas :-
#import pandas as pd
#d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")
#df=pd.DataFrame(d)
#print(df)
#Data_Frame.sort_values("column_name")
#print(df.sort_values("Name_of _Student"))                       #sorted by alpha order name column
#print(df.sort_values("Maths"))                                   #sorted by maths marks column ascending order
#data_frame.sort_values("column_name',ascending=false)
#print(df.sort_values("Maths",ascending=False))                   #sorted by maths marks column decending order
#print(df.sort_values("Name_of _Student",ascending=False))        #sorted by decending order with alpha
#data_frame.sort_values(["column_1","column_2"])
#print(df.sort_values(["Name_of _Student","Maths"])                #sorted by Name of student & Maths marks column decending order with alpha
#print(df.sort_values(["Name_of _Student","Maths"],ascending=[1,0])  #sorted by Name of student (ascending)& Maths marks(decending)column decending order with alpha 

#Manipulating dataframes in pandas:- 
import pandas as pd 
d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")                                      
df=pd.DataFrame(d)                                                    #DataFrame is created
print(df)
Data_Frame['new_col_name']=default_Value
df['Total_Marks']=0
print(df)                                                             #new column is added
df['Total_Marks']=df['Telugu']+df['English']+df['Maths']+df['Science']+df['Social']
print(df)                                                             #now the total marks column added we get total marks
df.drop(columns="Total_Marks")                                        #orginal Total_marks not droped
print(df)
df=df.drop(columns="Total_Marks")                                     #now the df=df orginal Total_marks not droped
print(df)
df['Total_Marks']=df['Telugu']+df['English']+df['Maths']+df['Science']+df['Social']
print(df[['Roll_No','Total_Marks']])                                 #this will only print 'Roll_No','Total_Marks'

#Removing Duplicates
#Data_Frame.duplicated() -boolean result
import pandas as pd
d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")                                      
df=pd.DataFrame(d)                                                    #DataFrame is created
print(df)
print(df.duplicated())                                #this will show all false becz no duplicated values are present in df
d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")            #now we add sm duplicated values for checking df in excel sheet                                   
df=pd.DataFrame(d)                                                    #DataFrame is created
print(df)
print(df.duplicated())                                #this will show some true&false becz sm duplicated values are present in df
df.drop_duplicates()  
print(df)                                            #this will drop the duplicated values #this is temp removed
df.drop_duplicates(inplace=True)
print(df)                                             #this will drop the duplicated values  #in orginal df

#Handling Missing Data:-
import pandas as pd
d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")                                      
df=pd.DataFrame(d)                                                    #DataFrame is created
print(df)
print(df.fillna(77))                                                      #this will fill the nan values in df by fillna
print(df["Science"].fillna(77))                                           #this will fill in science column in df
print(df.dropna())                                                        #this will drop the nan  
print(df.dropna(inplace=True))                                            #this will drop the nan in df orangilly
"""                       
#Data Filtering & Conditional changes:-
import pandas as pd
d=pd.read_excel("C:\\Users\\SMUTHYALA\\Desktop\\mar.xlsx")                                      
df=pd.DataFrame(d)                                                    #DataFrame is created
print(df)
print(df.loc[df["Maths"]<85])                                          #this will print Maths less than 85 in df(simple condition)
print(df.loc[(df["Maths"]>60) & (df["Maths"]<80)])                     #this will print maths less than 60&80in df(compund condition)
print(df.loc[df["Name_of _Student"].str.contains("hari")])             #this will print the hari name in df (simple condition.str.contsins)
print(df.loc[df["Name_of _Student"].str.startswith("h")])              #this will print the hari name in df (simple condition.str.startswith)
print(df.loc[df["Name_of _Student"].str.endswith("h")])                #this will print the hari name in df (simple condition.str.endswith)
df['Total_Marks']=df['Telugu']+df['English']+df['Maths']+df['Science']+df['Social']     #this will print a new column Total_Marks   
print(df)
df["percentage"]=(df["Total_Marks"]/500)*100                             #this will print the peercentage column
print(df)
df["Grade"]="pass/Fail"                                                  #new column created
print(df)
df.loc[df["percentage"]<40,["Grade"]]="Fail"                             #grade pass is filluped
print(df)
df.loc[((df["percentage"]>=40) & df["percentage"]<60),["Grade"]]="PASS"      #this will print pass
print(df)
df.loc[((df["percentage"]>=60) & df["percentage"]<70),["Grade"]]="FIRST CLASS"   #this will print FIRST CLASS
print(df)
df.to_excel("C:\\Users\\SMUTHYALA\\Desktop\\Marks_with_Grade.xlsx")    #this will the data to excel and create a new excel sheet from df

"""
dic = {'names':['sagar','tharun','yash'],
'location':['rdm','ntpc','hyd'],
'age' :[22,23,24],
'edu' : ['btech','dip','bba']
}

df = pd.DataFrame(dic)
print(df)
print(type(df))

#df.to_csv('friends.csv')

"""
"""
df = pd.read_csv('friends.csv')
print(df)

print(df.loc[0,:])
print(df.loc[df['age']<23])

"""

import pandas as pd
dict = {'Movie_data':['The Godfather','Bird Box','fight Club'],
'Year':[1992,2018,1999],
'Rating':[9.2,6.8,8.8]}
df = pd.DataFrame(dict)                                         
print(df)
print(type(df))
pd.DataFrame(dict,index=[1,2,3])