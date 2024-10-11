stringTesting = 'THIS IS the string, which is the testing of me!'

# Convert all of character in the string to the lower case
    #stringTesting = stringTesting.lower()
    #print(f"It is the string after the above method: {stringTesting}")

# Same to the lower() method, but it's wider range than lower()
    #stringTesting = stringTesting.casefold()
    #print(f"It is the string after the above method: {stringTesting}")

# This method convert all the words in this string: each words will change to this: The first character will be upper case, other characters will be lower case
    #stringTesting = stringTesting.title()
    #print(f"It is the string after the above method: {stringTesting}")


# Find method

position = stringTesting.find("IS")
print(f"The result of the find method: {position}")