#List

#any data type can be stored

# Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#List items are indexed, the first item has index [0], the second item has index [1] etc

#Ordered

#Mutable data type

#Use Square Brackets

#Allow duplicate

#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


list1=[1,2,3,4,5]
print(type(list1))

# Access Items

list2=["car","bike","van"]
print(list2[0])

# Negative Indexing

list3=["bus","van","bike"]
print(list3[-1])


# Range of Indexes

list4=["bus","van","bike"]
print(list3[0:2])


# Change Item Value

list5=["car","van","bike"]
list5[2]="aeroplane"
print(list5)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Add List Items

# append

# To add an item to the end of the list, use the append()

list6=["orange","apple","mango"]

list6.append("bala")

print(list6)



# Insert Items

# To insert a list item at a specified index, use the insert() method.

list7=["bala","vicky","arun"]
list7.insert(1,"guru")
print(list7)


# Extend List

# To append elements from another list to the current list, use the extend() method.

list1=["apple","orange","mango"]
list2=["car","van","bike"]

list1.extend(list2)
print(list1)


# Add Any Iterable

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

list3=[1,2,3,4]
tuple1=("bala","sri")

list3.extend(tuple1)

print(list3)


# Remove List Items

# The remove() method removes the specified item.


list4=["banana","car","van"]

list4.remove("car")

print(list4)

# Remove Specified Index (pop)

list5=[1,2,3,4,5]
list5.pop(1)
print(list5)


#del

# The del keyword also removes the specified index


# list6=[1,2,3,4,5]
# del list6
# print(list6)


# Clear the List

# he clear() method empties the list.

list7=["bala","sri","vignesh"]
list7.clear()
print(list7)


# Loop Lists

a=[1,2,3,4,5]
for i in a:
    print(i)


# oop Through the Index Numbers

a=[1,2,3,4,5]
for i in range(len(a)):
    print(i)


# Using a While Loop


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# List Comprehension

# List comprehension is a short and simple way to create a list using a loop.


# newlist = [expression for item in iterable if condition == True]


fruits = ['apple', 'banana', 'cherry']

num=[1,2,3,4,5]
list2=[x*x for x in num]
print(list2)


# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]


#sort

b=[1,6,3,4,5,2]
b.sort()
print(b)


#list methods


# append()	Adds an element at the end of the list

list1=[1,2,3,4,5]
list1.append("python")
print(list1)


# clear()

# clear()	Removes all the elements from the list

list1=[1,2,3,4,5]
list1.clear()
print(list1)


# copy()	Returns a copy of the list

list2=[1,2,3,4,5]

a=list2.copy()
print(a)


# count()	Returns the number of elements with the specified value

list3=[1,2,3,4,4,4,5]

b=list3.count(4)

print(b)


# extend()	Add the elements of a list (or any iterable), to the end of the current list

a=["car","van","banana"]
b=[1,2,3]

a.extend(b)

print(a)


# index()	
# Returns the index of the first element with the specified value

# Syntax
# list.index(elmnt, start, end)

a=[1,2,3,4,5]
print(a.index(1))


# insert()

# Adds an element at the specified position


fruits = ['apple', 'banana', 'cherry']

fruits.insert(2,"car")

print(fruits)


# pop()	

# Removes the element at the specified position


g=[1,2,3,4,5]
g.pop()
print(g)


# remove()	
# Removes the item with the specified value


list11=[1,2,3,4,5]
list11.remove(1)
print(list11)

# reverse()	

# Reverses the order of the list

mylist=["apple","Banana","camel"]
mylist.reverse()
print(mylist)


# sort()	
# Sorts the list

c=[1,2,3,5,6,4]
c.sort()
print(c)

