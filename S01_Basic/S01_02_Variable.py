# personal information
name = "Victor"
age = 28
country = "Mexico"
favorite_phrase = "Start again and again"

print("Name: ", name)
print("Age: ", age)
print("Country: ", country)
print("Favorite Phrase: ", favorite_phrase)

# type of variables
#int
age = 28
print("Age: ", age, "Type: ", type(age))
#float
pi = 3.1416
print("Pi: ", pi, "Type: ", type(pi))
#string
name = "Victor"
print("Name: ", name, "Type: ", type(name))
#boolean
is_student = True
print("Is student: ", is_student, "Type: ", type(is_student))
#None
address = None      # None es un valor especial que representa la ausencia de un valor o una variable sin valor asignado.
print("Address: ", address, "Type: ", type(address))

#Strings
greeting = "Hello, World!"
print("Greeting: ", greeting, "Type: ", type(greeting))
#Concatenation
first_name = "Victor"
last_name = "Garcia"
full_name = first_name + " " + last_name
print("Full Name: ", full_name)
#String methods
print("Uppercase: ", greeting.upper())
print("Lowercase: ", greeting.lower())
print("Length: ", len(greeting))
print("Replace: ", greeting.replace("World", "Python"))
#f-strings
age = 28
print(f"My name is {name} and I am {age} years old.")
# slash for new line
print("Line 1\nLine 2\nLine 3")
#tab for tabulation
print("Column 1\tColumn 2\tColumn 3")
#raw string
raw_string = r"C:\Users\Victor\Documents"
print("Raw String: ", raw_string)
#multiline string
multiline_string = """This is a multiline string.
It can span multiple lines.
It preserves the formatting."""
print("Multiline String: ", multiline_string)
#string slicing
s = "Hello, World!"
print("First 5 characters: ", s[:5])
print("Last 6 characters: ", s[-6:])
#string formatting
name = "Victor"
age = 28
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String: ", formatted_string)
#f-string with expressions
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
#string interpolation
name = "Victor"
age = 28
print("My name is %s and I am %d years old." % (name, age))
#string methods
s = "Hello, World!"
print("Starts with 'Hello': ", s.startswith("Hello"))
print("Ends with 'World!': ", s.endswith("World!"))
print("Find 'o': ", s.find("o"))
print("Count 'o': ", s.count("o"))  
#string slicing with step
s = "Hello, World!"
print("Every second character: ", s[::2])
#string slicing with negative step
s = "Hello, World!"
print("Reversed string: ", s[::-1])
#string formatting with alignment
name = "Victor"
print(f"{name:<10} is left aligned.")
print(f"{name:>10} is right aligned.")
print(f"{name:^10} is centered.")
#string formatting with padding
number = 42
print(f"{number:05} is padded with zeros.")
#string formatting with precision
pi = 3.141592653589793
print(f"Pi: {pi:.2f} is rounded to 2 decimal places.")
#string formatting with width
name = "Victor"
print(f"{name:10} is padded to width 10.")
#string formatting with comma
number = 1000000
print(f"Number: {number:,} is formatted with commas.")  
#string formatting with percentage
percentage = 0.85
print(f"Percentage: {percentage:.2%} is formatted as percentage.")
#string formatting with scientific notation
number = 123456789
print(f"Number: {number:.2e} is formatted in scientific notation.")
#string formatting with hexadecimal
number = 255
print(f"Number: {number:x} is formatted in hexadecimal.")
#string formatting with octal
number = 255
print(f"Number: {number:o} is formatted in octal.")
#string formatting with binary
number = 255
print(f"Number: {number:b} is formatted in binary.")
#string formatting with character
number = 65
print(f"Character: {number:c} is formatted as character.")
#string formatting with percentage and width
percentage = 0.85
print(f"Percentage: {percentage:10.2%} is formatted as percentage with width 10.")
#string formatting with scientific notation and width
number = 123456789
print(f"Number: {number:15.2e} is formatted in scientific notation with width 15.")
# \\ for backslash
print("This is a backslash: \\")
# \' for single quote
print('It\'s a nice day!')
# \" for double quote
print("She said, \"Hello!\"")
# \n for new line
print("Line 1\nLine 2\nLine 3")
# \t for tab
print("Column 1\tColumn 2\tColumn 3")
# \r for carriage return
print("Hello, World!\rHi, Universe!")
# \b for backspace
print("Hello, World!\b\b\b\b\b\b\b\b\b\b\b\bHi, World!")
# \f for form feed
print("Line 1\fLine 2\fLine 3")
# \v for vertical tab
print("Line 1\vLine 2\vLine 3")
# \a for bell
print("This will make a sound: \a")
# \0 for null character
print("This is a null character: \0")
# \N{name} for Unicode character
print("This is a Unicode character: \N{smiling face with smiling eyes}")
# \u for Unicode character with 4 hex digits
print("This is a Unicode character: \u263A")
# \U for Unicode character with 8 hex digits
print("This is a Unicode character: \U0001F600")