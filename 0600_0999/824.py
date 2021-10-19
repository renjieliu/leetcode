def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    output =""
    temp =  str(S).split(" ")
    for i in range(0,len(temp)):
        if temp[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
            output+=temp[i]+ 'ma' + 'a'*(i+1) +" "
        else:
            output += temp[i][1:] + temp[i][0] + 'ma' + 'a'*(i+1) +" "

    return output.strip(" ")

print(toGoatLatin("I speak Goat Latin"))