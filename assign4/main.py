# Conditional Statements (If / Else)
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Loops (For / While) y repeat krnly hota h 
for i in range(5):
    print(i)


count = 0
while count < 5:
    print(count)
    count += 1

# Break / Continue / Pass
# Yeh loop ke behavior ko change karte hain:

# break: loop ko rok deta hai

# continue: agle round (iteration) pe chala jata hai

# pass: kuch nahi karta, sirf jagah bharne ke liye hota hai


for i in range(5):
    if i == 3:
        break
    print(i)



# FUNCTIONS

# Function ek aisa block hota hai jo aik baar likhne ke baad baar baar chalay ja sakta hai.

def greet(name):
    print("Hello", name)

greet("Ali")
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


# Built-in Functions:
# Yeh woh functions hain jo Python mein pehle se hote hain, jaise:

# print()

# len()

# range()

# type()

# int(), str(), etc.

# Custom Functions:
# Jo tum khud banate ho apne kaam ke liye.

#  Summary Table:
# Topic	       Example	               Kaam kya karta hai
# if/else	   if age > 18:  	    Condition check karta hai
# for loop	   for i in range(5):	 Kaam ko baar baar repeat karta hai
# while loop	while x < 10:	     Jab tak condition true ho, chalta hai
# function	    def myFunc():	     Code ko reuse karne ke liye

# 9 Exception Handling in Python (Errors se bachao)
# Exception handling ka matlab hai errors se bachna ya unhein handle karna taake program crash na ho aur gracefully kaam karta rahe.

# x = 5
# y = 0
# print(x / y)  # Error: ZeroDivisionError



# Solution: try / except ka use
# Hum try block mein wo code likhte hain jo error de sakta hai, aur except block mein batate hain ke agar error aaye to kya karna hai.

try:
    x = int(input("5: "))
    y = int(input("8: "))
    result = x / y
    print("Result:", result)
except:
    print("some thing went wrong! Error .")
    
    


# catch

try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number, not letters!")



# block

try:
    f = open("file.txt", "r")
    data = f.read()
except:
    print("File not found")
finally:
    print("This will always run, whether an error occurs or not")


# File Handling 
# File handling ka matlab hai Python se file banana, read karna, write karna, ya usay close karna.

#  4 Main Modes of File Handling:

# Mode	  Use      	Description
# 'r'	  Read	    File read karta hai (default mode)
# 'w'	  Write   	File overwrite karta hai (purani cheezen mita deta hai)
# 'a'	  Append	File ke end mein nayi cheezen add karta hai
# 'x'	  Create	Nayi file banata hai, agar already hai to error deta hai


#  Basic Syntax:

# file = open("filename.txt", "mode")
# # do something with file
# file.close()
# # Example 1: File ko read karna ('r')

try:
    f = open("demo.txt", "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("File not found!")
#  Example 2: File mein likhna ('w')

f = open("demo.txt", "w")
f.write("Hello, this is my first file.\n")
f.write("Python is great!")
f.close
# Note: Agar file exist karti hai, to ye sab kuch overwrite kar dega.

#  Example 3: File mein cheezain add karna ('a')

f = open("demo.txt", "a")
f.write("\nThis line was added later.")
f.close()
# Example 4: File line-by-line read karna

f = open("demo.txt", "r")
for line in f:
    print(line.strip())
f.close()
#  Best Practice: with statement (auto close)

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# yahan file automatically close ho jati hai

# THE MATH AND DATE TIME CALANDER
#  math maodule

# Ye module mathematical functions ke liye hota hai, jaise ke square root, power, sin, cos, factorial, etc.

import math

print(math.sqrt(16))        # Square root: 4.0
print(math.pow(2, 3))       # Power: 2^3 = 8.0
print(math.factorial(5))    # Factorial: 5! = 120
print(math.pi)              # Value of Pi

# Kuch Useful math Functions:
# math.sqrt(x) → square root

# math.pow(x, y) → power

# math.factorial(x) → factorial

# math.ceil(x) → upar wala integer

# math.floor(x) → neeche wala integer

# math.pi → 3.1415...




# datetime Module
from datetime import datetime, date, timedelta

now = datetime.now()
print("Current date and time:", now)

today = date.today()
print("Today's date:", today)

# Date Difference
d1 = date(2025, 4, 17)
d2 = date(2025, 1, 1)
diff = d1 - d2
print("Days difference:", diff.days)

# Add 5 days
future_date = today + timedelta(days=5)
print("Date after 5 days:", future_date)



# datetime.now() → current date & time

# date.today() → sirf date

# timedelta(days=n) → din add/subtract karne ke liye

# strftime('%d-%m-%Y') → date formatting


# calnder module

# Ye module calendar banane, weekday check karne, aur leap year jaanchne ke liye use hota hai.


import calendar

print(calendar.month(2025, 4))   # April 2025 ka calendar
print(calendar.isleap(2024))     # Leap year hai ya nahi (True/False)
print(calendar.weekday(2025, 4, 17))  # Kis din hai? (0=Monday)

# Poore saal ka calendar
print(calendar.calendar(2025))

# calendar.month(year, month) → specific month ka calendar

# calendar.calendar(year) → full year ka calendar

# calendar.isleap(year) → leap year hai ya nahi

# calendar.weekday(y, m, d) → weekday return karta hai (0=Monday ... 6=Sunday)










# # from typing import Union
# # type



# # module 3rd party

# # import random
# # print(random.randint(1,10))


# # from add import addittion
# # addittion.add(6,4)


# import requests as req
# import pprint

# reponse = req.get("https://www.asharib.xyz/api/profile")
# pprint.pprint(reponse.json())



# # import requests as req
# # import pprint

# # # Make API request
# # response = req.get("https://www.asharib.xyz/api/profile")

# # # Check status code
# # if response.status_code == 200:
# #     print("Success! Status code:", response.status_code)
# #     pprint.pprint(response.json())
# # else:
# #     print("Failed! Status code:", response.status_code)
# #     print("Error message:", response.text)





# teacher_name = ("sir ameen")
