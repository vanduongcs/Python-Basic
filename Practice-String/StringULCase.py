string = input("Please press any string: ")

uString = string.upper()
print(f"The string after use upper() method: {uString}")

lString = string.lower()
print(f"The string after use lower() method: {lString}")

# Another way to get a lower string:
lString2 = string.casefold()
print(f"Another result of lower case string use casefold() method: {lString2}")