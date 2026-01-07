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


