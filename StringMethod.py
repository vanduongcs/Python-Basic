stringTest = "  This is a SIMPLE TESt    "

#upper() method convert all of the characters in the string from normal to upper case
result = stringTest.upper()
print(f"This is the result of upper() method: \"{result}\"")

#lower() method convert all of the characters in the string from upper case to lower case
result = stringTest.lower()
print(f"This is the result of lower() method: \"{result}\"")

#Same to the lower() method, but it's stronger than lower case because it can convert character outside the alphabet
result = stringTest.casefold()

