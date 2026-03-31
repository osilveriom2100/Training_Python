# conversión de tipos de datos
a = 10
# str is the default type of input, so we can also convert it back to a string
a = str(a)
print("The number you entered is:", a)
# converting the input to an integer
a = int(a)
print("The number you entered plus 10 is:", a + 10)
# converting the input to a float
a = float(a)
print("The number you entered multiplied by 2 is:", a * 2)

# boolean conversion, any non-empty string is considered True, while an empty string is considered False
# bool() 
# falsy values: False, None, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), empty sequences and collections 
# (e.g., '', (), [], {}, set(), range(0))
# truthy values: all other values that are not falsy, including non-empty strings, non-zero numbers, 
# and non-empty collections
b = "True"
b = bool(b)
print("The boolean value of the string 'True' is:", b)
b = ""
b = bool(b)
print("The boolean value of an empty string is:", b)
b = 1
b = bool(b)
print("The boolean value of the number 1 is:", b)
b = 0
b = bool(b)
print("The boolean value of the number 0 is:", b)
b = []
b = bool(b)
print("The boolean value of an empty list is:", b)
b = [1, 2, 3]
b = bool(b)
print("The boolean value of a non-empty list is:", b)
b = None
b = bool(b)
print("The boolean value of None is:", b)
