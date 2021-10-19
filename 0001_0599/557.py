def reverseString(s):
    output = ""
    for i in range(len(s)-1, -1,-1):
        output += s[i]
    return  output

def reverseWords(s):
    wordList = list()
    wordList = str(s).split(" ")
    output  = ""
    for i in range(0,len(wordList)):
        output+=reverseString(wordList[i]) + " "
    return  output.strip(" ")


print(reverseWords("Let's take LeetCode contest"))