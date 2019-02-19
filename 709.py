def toLowerCase(str: 'str'):
    output = ""
    for i in str:
        if ord(i) >=65 and ord(i)<=90:
            output+= chr(ord(i)+32)
        else:
            output+=i
    return  output



print(toLowerCase("ASDFA adf"))
print(toLowerCase("12983749241!SS@#$!"))
