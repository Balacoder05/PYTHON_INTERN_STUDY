# Conditional Statements in Python


# Question 1: Positive, Negative, or Zero

# Write a Python program to check whether a number is:

# Positive

# Negative

# Zero

number=int(input("Enter the number........"))
if number>0:
    print(f"{number}Positive")
elif number<0:
    print(f"{number}Negative")
else:
    print(f"{number}zero")



# 2.Write a Python program to check whether a given number is:

# Even

# Odd

number=int(input("Enter your number...."))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")






# EASY LEVEL – Question 3: Eligible to Vote

# Write a Python program to check whether a person is eligible to vote.


age=int(input("Enter your age...."))
if  age>=18:
    print(f"{age} eligible for voter")
else:
    print(f"{age}is not eligible for voter")





# ASY LEVEL – Question 4: Greater of Two Numbers

# Write a Python program to find the greater of two numbers.

# 📌 Rules

# Take two numbers as input

# Use if–else (or if–elif–else)


n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

if n > m:
    print(f"{n} is greater than {m}")
elif m > n:
    print(f"{m} is greater than {n}")
else:
    print("Both numbers are equal")


# Write a Python program to check whether a student is Pass or Fail.

marks = int(input("Enter your marks: "))

if marks >= 35:
    print(f"{marks} is Pass")
else:
    print(f"{marks} is Fail")




n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
o = int(input("Enter the third number: "))



# Write a Python program to find the largest among three numbers.

if n > m and n > o:
    print(n, "is the largest number")
elif m > n and m > o:
    print(m, "is the largest number")
else:
    print(o, "is the largest number")


# Write a Python program to assign grades based on marks.

    marks=int(input("Enter your marks.."))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B ")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")