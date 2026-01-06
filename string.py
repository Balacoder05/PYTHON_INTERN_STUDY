# Strings

print('hello')
print("Hello")

#Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#Assign String to a Variable

a="Hello"
print(a)


# Multiline Strings

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Strings are Arrays


a = "Hello, World!"
print(a[1])


# Looping Through a String

for i in "balamurugan":
    print(i,end=" ")


# String Length

c="balamurugan"
print(len(c))


# Check String(in)

d="python programming is very easy"
print("python" in d)

# Use it in an if statement:

e="python programming in english"
if "english" in e:
    print("yes,'english' is present")


# Check if NOT (not in)

txt = "The best things in life are free!"
print("expensive" not in txt)


# Use it in an if statement:


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Python - Slicing Strings

text="python"
print(text[0:3])

# Slice From the Start

text1="programming"
print(text1[:7])