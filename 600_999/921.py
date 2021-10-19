def minAddToMakeValid(S: str):
    while S.find("()") != -1:
        S = S.replace("()", "")
    return len(S)


print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("()"))
print(minAddToMakeValid(")))((("))
print(minAddToMakeValid("()))(("))