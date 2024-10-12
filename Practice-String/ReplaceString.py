string = input("Please press any string: ")

replaceStringBefore = input("Please press the string you want to replace: ")

replaceStringAfter = input("Replace to: ")

result = string.replace(replaceStringBefore, replaceStringAfter)

print(f"The string before replace: {string}")

print(f"The string after replace: {result}")