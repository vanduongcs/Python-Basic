stringTest = "  This is a SIMPLE TESt and number: 1 2 3, and α  "

# upper() method convert all of the characters in the string from normal to upper case
result = stringTest.upper()
print(f"This is the result of upper() method: \"{result}\"")

# lower() method convert all of the characters in the string from upper case to lower case
result = stringTest.lower()
print(f"This is the result of lower() method: \"{result}\"")

# Same to the lower() method, but it's stronger than lower case because it can convert character outside the alphabet
result = stringTest.casefold()
print(f"This is the result of casefold() method: \"{result}\"")

# strip() method remove all of space in the start position and end position of string 
result = stringTest.strip()
print(f"This is the result of strip() method: \"{result}\"")

# lstrip() method remove all of space int the start position of string
result = stringTest.lstrip()
print(f"This is the result of lstrip() method: \"{result}\"")