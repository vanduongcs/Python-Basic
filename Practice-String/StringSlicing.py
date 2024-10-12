# Input any string
string = input("Please enter any string: ")

# Input the start position
startPosition = int(input("Please enter the start position: "))

# Input the start position
endPosition = int(input("Please enter the end position: "))

# Slicing the string
subString = string[startPosition-1:endPosition]

# Print them to the screen
print(f"This is the substring of {string} start from {startPosition} to {endPosition}: {subString}")