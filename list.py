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