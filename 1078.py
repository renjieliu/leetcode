def findOcurrences(text: str, first: str, second: str):
    output = []
    t = text.split(" ")
    if len(t) <3 :
        return output
    for i in range(len(t)-2):
        if t[i] == first and t[i+1]== second:
            output.append(t[i+2])

    return output

print(findOcurrences( text = "alice is a good girl she is a good student", first = "a", second = "good"))
print(findOcurrences( text = "we will we will rock you", first = "we", second = "will"))

