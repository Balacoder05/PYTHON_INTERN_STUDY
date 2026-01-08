# Python Loops

# 1.For Loop  
# 2.While loop 

# while loop:

data=["bala",25,"sri",27,"gothu",32]
n=len(data)
i=0
while i<n:
    print(data[i])
    i=i+1

#for loop

#count even numbers between 1 to 50

for i in range(1,50+1):
    if i%2==0:
        print(i)
