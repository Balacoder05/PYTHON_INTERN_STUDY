#Set

#mutable

#unordered

#{}

# not allow duplicate

#create set 

set1={1,2,3,4,}
print(set1)


#set methods

#add()

s={1,2,3,5}
s.add(4)
print(s)


#remove()

s.remove(1)
print(s)

#clear

s.clear()
print(s)

#copy

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)


#discard()

a={1,2,3,4}
a.discard(4)
print(a)

#pop

a={5,6,7,8}
a.pop()
print(a)

#union

a={1,2,3}
b={3,4,5}

c=a.union(b)

print(c)


#intersection

a={7,8,9}
b={7,9,6}
c=a.intersection(b)
print(c)


#difference

a={9,4,6}
b={8,4,3}
c=a.difference(b)
print(c)

#update
a={2,3,4}
b={5,6,7}

a.update(b)

print(a)


#symmetric_difference

a={1,2,3,4}
b={4,5,6,7}

print(a.symmetric_difference(b))


#intersection_update()

a={1,2,3}
b={4,5,6,2}

a.intersection_update(b)
print(a)

#Difference_update

a={1,2,3}
b={2,3,4}
a.difference_update(b)
print(a)


#symmetric_difference_update()

a={1,2,3}
b={2,3,4}

a.symmetric_difference_update(b)

print(a)

#issubset()

a={1,2}
b={1,2,3,4}

print(a.issubset(b))


#issuperset

a={1,2,3,4,5}
b={1,2,3,4}

print(a.issuperset(b))


#isdisjoint()

a={1,2,3}
b={4,5,6,7}

print(a.isdisjoint(b))


