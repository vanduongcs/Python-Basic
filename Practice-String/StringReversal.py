# Method 1: Using the build-in method in python
print("The first method is that: ")
string = input("Please press any string: ")

# This method concatenate the reversal string after init string
result = "".join(reversed(string))
print(f"The string after reverse: {result}")

#Method 2: Using string slicing
print("\nThe second method is that: ")
secondString = input("Please press any string: ")

'''
 This method concatenate the string with that means: Start from zero and end at string end position by the step with value: -1
    For example: Step = 1 will act like here: position: 0 -> 1 -> 2 -> 3
    More example: Step = -1 will act like here: position: -1 -> -2 -> -3 -> -4
'''

result = secondString[::-1]
print(f"The string after reverse: {result}")