 #Tuples

tup=(1,2,3)
print(type(tup))

# Access Tuple Items

print(tup[0])


# Negative Indexing

print(tup[-1])


# Range of Indexes

print(tup[0:1])


#Tuple methods

#len()

print(len(tup))

# min and max

print(min(tup))

print(max(tup))

print(tup.count(1))

#index

print(tup.index(3))


 # tuple to list conversition

lst=list(tup)
print(type(lst))

#list to tuple conversion

tup1=tuple(lst)
print(type(tup1))
