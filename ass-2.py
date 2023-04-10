#1.Split the below data into 3 differnt columns into a dataframe
import pandas as pd
def split_dict_columns(dict_):
    df = pd.DataFrame.from_dict(dict_, orient='columns')
    return df

# this is form normal tabular formate
d = {'movie_data':['The Godfather 1972 9.2',
                    'Bird Box 2018 6.8',
                    'Fight Club 1999 8.8']}

# this is for tabular formate this (name,year,rating)
d = {'Name': ['The Godfather','Bird Box','Fight Club'],
     'Year'  : [1972,2018,1999],
     'Rating' : [9.2,6.8,8.8]}
                    
df = split_dict_columns(d)
print(df)
           
                     #(or)

#1.Split the below data into 3 differnt columns into a dataframe
import pandas as pd
dict = {'Movie_data':['The Godfather','Bird Box','fight Club'],
'Year':[1992,2018,1999],                                                
'Rating':[9.2,6.8,8.8]}                                                 
df = pd.DataFrame(dict)                                                 
print(df)                                                                
print(type(df))                                                         

#output:- #       Movie_data  Year  Rating
          #0    The Godfather  1992    9.2
          #1       Bird Box   2018     6.8
          #2     fight Club   1999     8.8 
          #class 'pandas.core.frame.DataFrame'>
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

#2.Create a new discount(5 percent of original cost column value) column in Pandas DataFrame based on the existing columns
import pandas as pd
dic = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],                                          
'Cost':[10000, 5000, 15000, 2000]})                                                        
data = pd.DataFrame(dic)                                                                   
data['Discount_Price'] = data['Cost'] - (0.05 * data['Cost'])                              
print(data)                                                                                

#output:-#        Date    Event   Cost  Discount_Price
         #0  10/2/2011    Music  10000          9500.0
         #1  11/2/2011   Poetry   5000          4750.0
         #2  12/2/2011  Theatre  15000         14250.0
         #3  13/2/2011   Comedy   2000          1900.0
  
                                #(or)

#2. Create a sample dataframe with Date and Event and Cost
import pandas as pd
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
'Cost':[10000, 5000, 15000, 2000]})
print(df)

# Applying 5% of discount in ocst coluimn 
def apply_discount(Cost):
    return Cost * 0.95

df['New_Cost'] = df['Cost'].apply(apply_discount)
print(df)

#OUTPUT

# output before discount
"""
        Date    Event   Cost
0  10/2/2011    Music  10000
1  11/2/2011   Poetry   5000
2  12/2/2011  Theatre  15000
3  13/2/2011   Comedy   2000


# Output after appying 5% of discount

        Date    Event   Cost  New_Cost
0  10/2/2011    Music  10000    9500.0
1  11/2/2011   Poetry   5000    4750.0
2  12/2/2011  Theatre  15000   14250.0
3  13/2/2011   Comedy   2000    1900.0
"""       
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

#5.find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    char_index = {}
    start = 0
    max_length = 0
    for i, c in enumerate(s):
        if c in char_index:
            start = max(start, char_index[c])
        char_index[c] = i
        max_length = max(max_length, i - start )
    return max_length
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  
s = "pwwkew"
print(lengthOfLongestSubstring(s))  

# Outputs: 3
# Outputs: 3                                
#------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#6.Given a string s, return the longest palindromic substring in s.
#s = "babad" Output: "bab"

def longestPalindrome(s: str) -> str:              #define a function  #s=string
    length = len(s)                                #length of s   'babad'    5:length
    index = -1                                          #-1:index
    maxlength = 0                                       #0:maxlength
    for i in range(length):                             #i:0
        for j in range(i, length):                      #j:0
            ispalindrome = 1                            #palindrome:1
            for k in range(0, ((j - i) // 2) + 1):      #k:0
                if s[i + k] != s[j - k]:
                    ispalindrome = 0
            if ispalindrome != 0 and j - i + 1 > maxlength:
                index = i
                maxlength = j - i + 1
    return s[index:index + maxlength]
if __name__ == "__main__":                   #class  #special verialble
    word = "babad"                                  #5 length
    print(longestPalindrome(word))                 #word in s  babad   

#output:-bab
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#3.Read the aatched csv file as dataframe.
#a.The price column contains some missing values.The missing values for apples need to be filled with the average price of apples
#b.find the difference between the maximum and minimum price of each product 
import pandas as pd
df = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\groceries.csv")
avg_prices = df.groupby("product_description")["price"].transform("mean")
df["price"].fillna(avg_prices, inplace=True)
print(df.loc[df['product_description'] == 'apple', ['product_description','price']])
# output:-
"""
#product_description     price
150               apple  1.900000
151               apple  1.900000
152               apple  1.900000
153               apple  1.900000
154               apple  2.077778
155               apple  1.900000
156               apple  1.900000
157               apple  1.900000
158               apple  1.900000
159               apple  1.900000
160               apple  2.077778
161               apple  1.900000
162               apple  1.900000
163               apple  2.200000
164               apple  2.200000
165               apple  2.200000
166               apple  2.200000
167               apple  2.200000
168               apple  2.200000
169               apple  2.200000
170               apple  2.200000
171               apple  2.200000
172               apple  2.200000
173               apple  2.200000
174               apple  2.200000
175               apple  2.200000
176               apple  2.077778
177               apple  2.200000
178               apple  2.200000
179               apple  2.200000
"""
#3b)
df = pd.read_csv("C:\\Users\\SMUTHYALA\\Desktop\\groceries.csv")
grouped = df.groupby("product_description")
max = grouped.max()['price']
min = grouped.min()['price']
difference = max.sub(min)
print(difference)
#output:-
"""
product_description
apple          0.3
butter-0.25    1.0
cucumber       0.4
grape          0.0
milk-1.5       0.5
onion          0.3
orange         0.3
plum           0.8
tomato         0.6
yogurt-1       1.0
Name: price, dtype: float64
"""
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#4.Given a  integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0
#Input: x = 123 op 321    x= -123 op : -321
#
def reverse_integer(x):
    if x < -2147483648 or x > 2147483647:          #32 bit value
        return 0
    reversed_str = str(x)[::-1]
    if x < 0:
        reversed_str = reversed_str[:-1]
        return -int(reversed_str)
    else:
        return int(reversed_str)
print(reverse_integer(123))  
print(reverse_integer(-123)) 

# Output: 321
# Output: -321

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#7.Write code to which meets below criteria credit card validator
import re                                     #re = regular expersion
n = int(input())
for t in range(n):
    credit = input().strip()
    credit_removed_hiphen = credit.replace('-','')
    valid = True
    length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))    
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
    if length_16 == True or length_19 == True:
        if consecutive == True:                                      #4424424424442444   valid
            valid=False                                              #5122-2368-7954-3214 valid
    else:                                                            #42536258796157867   invalid
        valid = False                                                #4424444424442444    invalid
    if valid == True:                                                #5122-2368-7954 - 3214   in valid
        print('Valid')                                               #44244x4424442444       invalid
    else:                                                            #0525362587961578        invalid
        print('Invalid')

#output:- #4424424424442444   valid
         #5122-2368-7954-3214 valid
         #42536258796157867   invalid
         #4424444424442444    invalid
         #5122-2368-7954 - 3214   in valid
         #44244x4424442444       invalid
         #0525362587961578        invalid
 
                            #or
# Credit card validator.
import re

def is_valid_credit_card(card_number):
  # Check that the card number starts with 4, 5, 6.
  if not re.match(r'^[4-6]', card_number):
    return False
  # Check card number is 16 digit and consists '-'.
  if not (bool(re.match(r'^\d{16}$', card_number)) or bool((re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number)))):
    return False
  # Check if card number consists of all digits.
  if not re.match(r'^[\d-]+$', card_number):
    return False
  # Check if card number have no 4 or more consecutive repeated digits
  if re.search(r'(\d)\1{3,}', card_number):
    return False

  return True

print(is_valid_credit_card('4253-6258-7961-5786'))  # True
print(is_valid_credit_card('4253625879615786'))     # True
print(is_valid_credit_card('4424424424442444'))     # True
print(is_valid_credit_card('5122-2368-7954-3214'))   # True
print(is_valid_credit_card('42536258796157867'))        # False
print(is_valid_credit_card('4424444424442444'))         # False
print(is_valid_credit_card('5122-2368-7954 - 3214'))    # False
print(is_valid_credit_card('44244x4424442444 '))        # False
print(is_valid_credit_card('0525362587961578'))         # False

#--------------------------------------------------------------------------------------------------------------------         
#---------------------------------------------------------------------------------------------------------------------
