#The program count the numbers of times substring appear
string = input("Please press any string: ")

subString = input("Please press substring in this line: ")
def count(string, subString):
    return string.count(subString)

print(f"The number of times substring appear: {count(string, subString)}")