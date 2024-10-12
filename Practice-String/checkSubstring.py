
string = input("Please press any string: ")

subString = input("Please press any substring you want to check: ")

# Print the result: Substring exists or not exists in string
def checkSubstring(string, subString):
    if(string.find(subString)) == -1:
        print(f"{subString} is not exists within {string}")
    else:
        print(f"{subString} is exists within {string}")

# Run the function above
checkSubstring(string, subString)
