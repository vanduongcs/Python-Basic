# Input the string
print("The first method is that: ")
string = input("Please press any string: ")

#Method 1: Using the build-in method in python
# This method concatenate the reversal string after init string
result = "".join(reversed(string))

print(f"The string after reverse: {result}")

#Method 2: Using string slicing
print("\nThe second method is that: ")
secondString = input("Please press any string: ")

result = secondString[::-1]

print(f"The string after reverse: {result}")
