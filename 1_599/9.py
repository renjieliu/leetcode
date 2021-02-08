def isPalindrome(x):
    if x < 0:
        return False
    else:
        output = ""
        for i in range(-1, -1 * len(str(x)) - 1, -1):
            output += str(x)[i]
        if output == str(x):
            return True
        else:
            return False


print(isPalindrome(10))