# Arithmetic operators

# a=5 
# b=3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a  % b)
# print(a ** b)

# ASSIGMENT 

# x = 5
# x += 3     #  x =x + 3
# x -= 3  	# x = x - 3
# x *= 3	   # x = x * 3
# x /= 3   	#x = x / 3
# x //= 3 	#x = x // 3
# x %= 3	   # x = x % 3
# x **= 3 	#x = x ** 3
# print(x)

#comparision
# a = 10
# b = 5
# print(a > b) 
# print(a < b)
# print(a == b)
# print(a != b)
 

#logical
# and both condition must b True
#  or at least one condition must be True
#  not negative the condition False

# x = 10 
# y = 5
# print(x > 5 and y < 10)
# print(x > 5 and y > 10)
# print(not (x > 5))

# identity operator

# is  Returns True if both variables reference the same object	
# is not  Returns True if both variables reference different objects 

# a = [1, 2, 3]
# b = a  # Same reference
# c = [1, 2, 3]  # Different object

# print(a is b)   # True
# print(a is c)   # False
# print(a is not c)  # True  

  #Membership
#   in Returns True if value is in sequence	'a' in 'apple'	True
#   not in	Returns True if value is not in sequence	'z' not in 'apple'	True

# fruits = ["apple", "banana", "mango"]
# print("apple" in fruits)  
# print("grape" not in fruits)  
  
# Bitwise
# this operator is working for binary 

# &	AND 	    5 & 3 → 1
# |	|	OR
# ^	XOR	        5 ^ 3 → 6
# ~	NOT	~       5 → -6
# <<	Left Shift	5 << 1 → 10
# >>	Right Shift	5 >> 1 → 2


a = 5 
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)