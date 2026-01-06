# Python Operators

# Operators are used to perform operations on variables and values.

print(10+20)

# Arithmetic Operators

# Arithmetic operators are used with numeric values to perform common mathematical operations

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)  #/ - Division (returns a float)
print(x % y)
print(x ** y)  #15⁴ = 15 × 15 × 15 × 15 = 50625
print(x // y)  #Division without remainder (only integer part),15 ÷ 4 → 3 (ignore 0.75),Output: 3
# // - Floor division (returns an integer)


# Assignment Operators

# Assignment operators are used to assign values to variables:


# Walrus Operator

# The Walrus Operator := is used to assign a value to a variable as part of an expression.

if (n := len("Python")) > 5:
    print("Length is", n)


x = 10;

x += 5; 
print("x += 5 ->", x); 

x -= 3; 
print("x -= 3 ->", x);

x *= 2; 
print("x *= 2 ->", x);

x /= 4; 
print("x /= 4 ->", x);

x %= 3; 
print("x %= 3 ->", x);

x //= 2; 
print("x //= 2 ->", x);

x **= 3; 
print("x **= 3 ->", x);


# Comparison Operators

# Comparison operators are used to compare two values

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Logical Operators

# and 

x=5

print(x > 3 and  x < 10)

# or

x = 5

print(x > 3 or x < 4)

# not

x = 5

print(not(x > 3 and x < 10))


# Identity Operators

# is (Returns True if both variables are the same object)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


# is not  (The is not operator returns True if both variables do not point to the same object)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal



# Membership Operators



# in

# Membership operators are used to test if a sequence is presented in an object

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


# not in

# Returns True if a sequence with the specified value is not present in the object


fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)



# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers

print(bin(10))