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
import sys
print(sys.getrecursionlimit())


from time import sleep
def greek():
    print("Hello Bala")
    sleep(0.30)
    greek()
greek()


#count printed value

from time import sleep
count=0
def greek():
    global count
    print("Hello Bala",count)
    count=count+1
    sleep(0.30)
    greek()
greek()


#factorial using function


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
result=factorial(5)
print(result)


#factorial using recursive function


def factorial(n):
    if n==1:
        return 1
    
    return n*factorial(n-1)
result=factorial(5)
print(result)



#map function


a=[1,2,3,4,5]
result=map(lambda x:x*2,a)
print(list(result))

a=[1, 2, 3, 4, 5]
result=map(lambda x:x**2,a)
print(list(result))

n=[2, 5, 8, 10]
result=map(lambda x: f" Number is {x}",n)
print(list(result))


a=[1, 2, 3, 4, 5]
result=map(lambda x: x+5,a)
print(list(result))


words = ["bala", "ravi", "sam"]
result=map(lambda x:x.upper()+"!",words)
print(list(result))



word=[1, 2, 3, 4, 5]
result=map(lambda x:x*3,word)
print(list(result))


list1=["apple", "banana", "cherry"]
result=map(lambda x:x.capitalize(),list1)
print(list(result))


#filter

a=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x: x%2==0,a)
print(list(result))

#reduce

from functools import reduce

from functools import reduce

#find maximum

num=[3,5,8,9,1]
maximum=reduce(lambda x,y:x if x>y else y,num)
print(maximum)



# Multiply all numbers

num=[2,3,5,6,7]
multi=reduce(lambda x,y:x*y,num)
print(multi)


# Write a Python program using reduce() to find the sum of all even numbers in the list.
num = [1, 2, 3, 4, 5, 6, 7, 8]

result=reduce(lambda x,y: x+y if y%2==0 else x,num,0)
print(result)


#Enumerate


fruits = ['apple', 'banana', 'cherry']
for index,fruit in  enumerate (fruits):
  print(index,fruit)



#zip
list1=[1,2,3,4,5]
list2=["Bala","Sri","Vignesh","Guru","Mukesh"]

result=zip(list1,list2)
print(list(result))
