# control flow
# IF, ELIF, ELSE

age = 18

if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You can apply for a driving license.")
else:
    print("You are too young.")



day = "Monday"

match day:
    case "Monday":
        print("Start of the week!")
    case "Friday":
        print("Weekend is near!")
    case _:
        print("It's a regular day.")


# LOOP

fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)


# RANGE

for i in range(1, 6):  # 1 to 5
    print(i)

# WHILE

count = 0

while count < 5:
    print("Count is:", count)
    count += 1  # Increment


# LOOP CONTROL

for num in range(1, 10):
    if num == 5:
        break  # Stop loop at 5
    print(num)

# CONTINUE STATEMENT 

for num in range(1, 6):
    if num == 3:
        continue  # Skip number 3
    print(num)


# pass statement

for i in range(5):
    if i == 2:
        pass  # Do nothing for 2
    else:
        print(i)

        # list

# make list
fruits = ["apple", "banana", "cherry"]

# add items in list
fruits.append("orange")

print(fruits)

#  list m kisi khas value ko change krna ho usk number likhy g r wo name 

fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)

# # item remove in list
fruits = ["apple", "banana", "cherry"]
fruits.remove("cherry")
print(fruits)


# use loop in full items

fruits = ["apple", "banana", "cherry" , "mango"]

for fruit in fruits:
    print(fruit)


# list k length maloom krny kly

fruits = ["apple", "banana", "cherry"]
print(len(fruits))


# tuple

# make tuple
numbers = (10, 20, 30, 40)
print(numbers)

# tuple k kisi index m mojood value k hasil krna:
numbers = (10, 20, 30, 40)

print(numbers[1])  # Output: 20


# # tuple ko change nai kia jaskta y error dy
# numbers = (10, 20, 30, 40)
# numbers[1] = 50  # TypeError

#loop in tuple

numbers = (10, 20, 30, 40)
for num in numbers:
    print(num)

# length maloom krna


numbers = (10, 20, 30, 40)

print(len(numbers))

# dictionary


# make dictionary
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}

# kisi khas key k value hasil krna

print(student["name"])  # Output: Ali 

# اdict m new key-value add krna
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}
student["city"] = "Karachi"
print(student)

# kisi khas value ko update krna

student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}
student["age"] = 24

# kisi key ko delet krna
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}
del student["course"]
print(student)

# dictiony m key value k all couple m loop chlata skta h
student = {
    "name": "Ali ,Ahmed , Asif",
    "age": 22,
    "course": "Python"
}
for key, value in student.items():
     print(f"{key}: {value}")


# dictionary k length maloom krna
student = {
    "name": "Ali ,Ahmed , Asif",
    "age": 22,
    "course": "Python"
}
print(len(student))

# list

mixed: list   = ["hello", 42, 3.14, True]
print("mixed   = ", mixed)

# simple set
# 
my_set = {1, 2, 3, 4, 5}
print(set)



# items duplicate m only one time h  show hngy
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5}


# empty set
numbers = set()

# Set m items add krna
numbers.add(10)
numbers.add(20)
numbers.add(30)
print(numbers)


# # Set m items romove krna
numbers(10 , 20 , 30 , 40)

numbers.remove(20)  # اagr item mojood na ho to error dy g
print(numbers)


numbers.discard(30)  #agr item mojod na ho to error nai dy g
print(numbers)  # Output: {10}


# option in set


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (A اور B all items
print(A | B)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (A اور B same itmes
print(A & B)  # Output: {3, 4}

# Difference (wo items jo A m na ho B m ho)
print(A - B)  # Output: {1, 2}

# Symmetric Difference   (wo items jo A r B dono m mojood h na ho)
print(A ^ B)  # Output: {1, 2, 5, 6}



# frozen set

# make frozen set
my_frozenset = frozenset([1, 2, 3, 4, 5])


my_frozenset.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'


my_frozenset.remove(3)  # AttributeError: 'frozenset' object has no attribute 'remove'


A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])  

print(A | B)  # Output: frozenset({1, 2, 3, 4, 5}) line wise counting
print(A & B)  # Output: frozenset({3}) same number


