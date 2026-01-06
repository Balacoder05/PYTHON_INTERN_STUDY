# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

a=10
print(type(a))


b=20.5

print(type(b))

c=5+20j

print(c)

print(type(c))

x=memoryview(bytes(5))
print(x)
print(type(x))




# Setting the Data Type

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# Setting the Specific Data Type


d=str("printing string")
print(type(d))


# Python Numbers


# int
# float
# complex


e=1  #int
f=2.5 #float
g=3+4j #complex

print(type(e))
print(type(f))
print(type(g))




# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number

import random

print(random.randrange(1,100))


a=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(a))


# Specify a Variable Type

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)



x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
