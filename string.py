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


# Slice To the End

text2="balamurugan"
print(text2[2:])


# Negative Indexing

text3="nothing"
print(text3[-5:-1])




# Python - Modify Strings


# built-in methods

# Upper Case

text4="balamurugan"
print(text4.upper())

#lower

a = "Hello, World!"
print(a.lower())


# Remove Whitespace

c=" mannargudi! "
print(c.strip())


#Replace String

d="Bala"
print(d.replace("B","b"))

# Split String

e="balamurugan ,elangovan"
print(e.split())

# Python - String Concatenation

q="hello"
w="world"
print(q+w)

e="hello"
r="world"
t=e+" "+r
print(t)


# Python - Format - Strings

first="balamurugan"
second="elangovan"

third=f"my name is {first},my father name is {second}"

print(third)


# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)



# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

# Python - Escape Characters

# txt = "We are the so-called "Vikings" from the north." # error because of inside use double quation

txt = "We are the so-called \"Vikings\" from the north."
print(txt)




# Python - String Methods

#lower()

a="Hello"
print(a.upper()) #Convert to lowercase
print(a.lower())  #Convert to uppercase
print(a.capitalize())  #First letter uppercase
print(a.title()) #First letter of each word uppercase
print(a.strip())   #Remove spaces from both sides
print(a.replace("H","g")) #Replace text

text = "apple,banana,orange"  # Split string into list
print(text.split(","))

# join() – Join list into string

words = ["Hello", "World"]
print(" ".join(words))


# find() – Find position of text

print(a.find("hello"))


# startswith() – Check starting word

print(a.startswith("Hello"))

# endswith() – Check ending word

f="file.txt"

print(f.endswith(".txt"))



# count() – Count occurrences

c="banana"
print(c.count("b"))

# isalpha() – Check only letters

text = "Python"
print(text.isalpha())


#isdigit() – Check only numbers

text = "12345"
print(text.isdigit())


# isalnum() – Letters and numbers

text = "Python123"
print(text.isalnum())



