#Python Functions

#Creating a Function


def my_function():
    print("Hello this is my first function")

# Calling a Function

def my_function():
    print("Hello this my first calling function")

my_function()

#function real timeb example

def validate_login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Username or Password"
        
        
print(validate_login("admin", "1234"))
print(validate_login("bala", "0000"))


#Return

def add(a,b):
    return a+b
p=add(10,20)
print(p)

def add(a,b):
    return a+b
print(add(10,20))

#arguments

def add(a,b):

    return a+b
print(add(20,30))

















#lambda function

# Check a number is Even or Odd

answer=lambda x: "Even" if x%2==0 else "odd"
print(answer(7))

# Write a lambda function to find the square of a number.

answer=lambda a:a*a 
print(answer(5))

# Write a lambda function to find the maximum of two numbers.


answer=lambda a,b: a if a>b else b
print(answer(5,2))


#using function to pattern

def pattern(a):
    for i in range(a):
        for j in range(a):
            print("*",end=" ")
        print()
pattern(5)


# Recursive Function

