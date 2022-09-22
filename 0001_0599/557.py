class Solution:
    def reverseWords(self, s: str) -> str: # O( N | N )
        return ' '.join(_[::-1] for _ in s.split(' '))  #split the s, and reverse each part
    


# previous solution

# def reverseString(s):
#     output = ""
#     for i in range(len(s)-1, -1,-1):
#         output += s[i]
#     return  output

# def reverseWords(s):
#     wordList = list()
#     wordList = str(s).split(" ")
#     output  = ""
#     for i in range(0,len(wordList)):
#         output+=reverseString(wordList[i]) + " "
#     return  output.strip(" ")


# print(reverseWords("Let's take LeetCode contest"))



