def backspaceCompare(S: str, T: str):
    clean_1 = ""
    for i in S:
        if i == "#" and len(clean_1)>0:
            clean_1 = clean_1[0:-1]
        else:
            if i != "#":
                clean_1 = clean_1+ i


    clean_2 = ""
    for i in T:
        if i == "#" and len(clean_2)>0:
            clean_2 = clean_2[0:-1]
        else:
            if i != "#":
                clean_2 = clean_2 + i


    return True if clean_1 == clean_2 else False

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a##c", "#a#c"))
print(backspaceCompare("a#c", "b"))
