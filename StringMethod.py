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

# lstrip() method remove all of space in the start position of string
# if you need to remove all of space in the end position of string, you must use the rstrip() method
result = stringTest.lstrip()
print(f"This is the result of lstrip() method: \"{result}\"")

# find(<specify string>,[start],[end]) method result the first position of specify string in the string
# [start] and [end] is optional
result = stringTest.find("is",4,13)
print(f"This is the result of find() method: \"{result}\"")

# Another method same to the find() method is index()
# A big different of them is that: if find() method can not find the specify string position int the string, it will return -1
# But in this situation, the index() method will notify an error

#I bring it into a comment because if I run it, the error will appear and program will stop.

'''
result = stringTest.index("can not find this string")
print(f"This is the result of index() method: \"{result}\"")
'''

#"<separated>".join()