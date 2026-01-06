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





