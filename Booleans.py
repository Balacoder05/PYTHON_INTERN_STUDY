# Python Booleans (True ,False)

print(10>6)

print(20>30)



# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

# print(bool(0)) false

# Most Values are True

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Some Values are False


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# isinstance()

x=100
print(isinstance(x,int))



