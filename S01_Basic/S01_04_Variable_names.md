# Variable naming rules
## 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
## 2. Variable names can contain letters, digits (0-9), and underscores (_).
## 3. Variable names cannot start with a digit.
## 4. Variable names cannot contain spaces.
## 5. Variable names cannot be a reserved keyword in Python 
(e.g., if, else, while, for, etc.).
## 6. snake_case is the convention for variable names in Python, which means using lowercase letters and underscores to separate words 
(e.g., my_variable_name).
## 7. Variable names should be descriptive and meaningful to improve code readability 
(e.g., age, name, is_student).
## 8. Constance: Variable names that are meant to be constant (unchanging) are often written in uppercase letters with underscores 
(e.g., PI = 3.1416).
## 9. PascalCase: Variable names that are meant to represent classes or types are often written in PascalCase (e.g., MyClass, UserType).
## 10. boolean variables often start with "is", "has", "can", or "should" to indicate their purpose 
(e.g., is_active, has_permission, can_edit, should_update).
## 11. Avoid using single-character variable names (e.g., x, y, z) unless they are used in a very limited scope 
(e.g., loop counters).

# Strings

```python
greeting = "Hello, World!"
print("Greeting: ", greeting, "Type: ", type(greeting)) 
```

**Output:**

```
Greeting: Hello, World! Type: <class 'str'>
```

# Concatenation

```python
first_name = "Victor"
last_name = "Garcia"
full_name = first_name + " " + last_name
print("Full Name: ", full_name)
```

**Output:**

```
Full Name: Victor Garcia
```

# String methods

```python
print("Uppercase: ", greeting.upper())
print("Lowercase: ", greeting.lower())
print("Length: ", len(greeting))
print("Replace: ", greeting.replace("World", "Python"))
```

**Output:**

```
Uppercase: HELLO, WORLD!
Lowercase: hello, world!
Length: 13
Replace: Hello, Python!
```
# f-strings

```python
age = 28
print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```
My name is Victor and I am 28 years old.
```

# slash for new line

```python
print("Line 1\nLine 2\nLine 3")
```

**Output:**

```
Line 1
Line 2
Line 3
```

# tab for tabulation

```python
print("Column 1\tColumn 2\tColumn 3")
```

**Output:**

```
Column 1	Column 2	Column 3
```

# raw string

```python
raw_string = r"C:\Users\Victor\Documents"
print("Raw String: ", raw_string)
```

**Output:**

```
Raw String: C:\Users\Victor\Documents
```

# multiline string

```python
multiline_string = """This is a multiline string.
It can span multiple lines.
It preserves the formatting."""
print("Multiline String: ", multiline_string)
```

**Output:**

```
Multiline String: This is a multiline string.
It can span multiple lines.
It preserves the formatting.
```

# string slicing

```python
s = "Hello, World!"
print("First 5 characters: ", s[:5])
print("Last 6 characters: ", s[-6:])
```

**Output:**

```
First 5 characters: Hello
Last 6 characters: World!
```
# string formatting

```python
name = "Victor"
age = 28
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String: ", formatted_string)
```

**Output:**

```
Formatted String: My name is Victor and I am 28 years old.
```

# f-string with expressions

```python
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
```

**Output:**

```
The sum of 5 and 10 is 15.
```

# string interpolation

```python
name = "Victor"
age = 28
print("My name is %s and I am %d years old." % (name, age))
```

**Output:**

```
My name is Victor and I am 28 years old.
```

# string methods

```python
s = "Hello, World!"
print("Starts with 'Hello': ", s.startswith("Hello"))
print("Ends with 'World!': ", s.endswith("World!"))
print("Find 'o': ", s.find("o"))
print("Count 'o': ", s.count("o"))  
```

**Output:**

```
Starts with 'Hello': True
Ends with 'World!': True
Find 'o': 4
Count 'o': 2
```

# string slicing with step

```python
s = "Hello, World!"
print("Every second character: ", s[::2])
```

**Output:**

```
Every second character: Hlo ol!
```

# string slicing with negative step

```python
s = "Hello, World!"
print("Reversed string: ", s[::-1])
```

**Output:**

```
Reversed string: !dlroW ,olleH
```
# string formatting with alignment

```python
name = "Victor"
print(f"{name:<10} is left aligned.")
print(f"{name:>10} is right aligned.")
print(f"{name:^10} is centered.")
```

**Output:**

```
Victor     is left aligned.
    Victor is right aligned.
  Victor   is centered.
```

# string formatting with padding

```python
number = 42
print(f"{number:05} is padded with zeros.")
```

# string formatting with precision

```python
pi = 3.141592653589793
print(f"Pi: {pi:.2f} is rounded to 2 decimal places.")
```

# string formatting with width

```python
name = "Victor"
print(f"{name:10} is padded to width 10.")
```

# string formatting with comma

```python
number = 1000000
print(f"Number: {number:,} is formatted with commas.")  
```

# string formatting with percentage

```python
percentage = 0.85
print(f"Percentage: {percentage:.2%} is formatted as percentage.")
```
# string formatting with scientific notation

```python
number = 123456789
print(f"Number: {number:.2e} is formatted in scientific notation.")
```

# string formatting with hexadecimal

```python
number = 255
print(f"Number: {number:x} is formatted in hexadecimal.")
```

# string formatting with octal

```python
number = 255
print(f"Number: {number:o} is formatted in octal.")
```

# string formatting with binary

```python
number = 255
print(f"Number: {number:b} is formatted in binary.")
```

# string formatting with character

```python
number = 65
print(f"Character: {number:c} is formatted as character.")
```
# string formatting with percentage and width

```python
percentage = 0.85
print(f"Percentage: {percentage:10.2%} is formatted as percentage with width 10.")
```

# string formatting with scientific notation and width

```python
number = 123456789
print(f"Number: {number:15.2e} is formatted in scientific notation with width 15.")
```

# \\ for backslash

```python
print("This is a backslash: \\")
```

# \' for single quote

```python
print('It\'s a nice day!')
```

# \" for double quote

```python
print("She said, \"Hello!\"")
```

# \n for new line

```python
print("Line 1\nLine 2\nLine 3")
```

# \t for tab

```python
print("Column 1\tColumn 2\tColumn 3")
```

# \r for carriage return

```python
print("Hello, World!\rHi, Universe!")
```

# \b for backspace

```python
print("Hello, World!\b\b\b\b\b\b\b\b\b\b\b\bHi, World!")
```

# \f for form feed

```python
print("Line 1\fLine 2\fLine 3")
```

# \v for vertical tab

```python
print("Line 1\vLine 2\vLine 3")
```

# \a for bell

```python
print("This will make a sound: \a")
```

# \0 for null character

```python
print("This is a null character: \0")
```

# \N{name} for Unicode character

```python
print("This is a Unicode character: \N{smiling face with smiling eyes}")
```

# \u for Unicode character with 4 hex digits

```python
print("This is a Unicode character: \u263A")
```

# \U for Unicode character with 8 hex digits

```python
print("This is a Unicode character: \U0001F600")
```

