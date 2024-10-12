string = input("Please press any string: ")

def checkPalindrome(string):
    checkStr = "".join(reversed(string))
    if(checkStr == string):
        return True
    return False

if(checkPalindrome(string)):
    print(f"{string} is the palindrome string")
else:
    print(f"{string} is not palindrome string")