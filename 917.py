class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        tmp = ""
        s = list(s)
        for i in range(len(s)):
            curr = s[i]
            if 65 <= ord(curr) <= 90 or 97<=ord(curr) <=122:
                tmp+=curr
                s[i] = "A"
        tmp = list(tmp)
        for i in range(len(s)):
            if s[i] == "A":
                s[i] = tmp.pop() #pop from the tail for reverse

        return "".join(s)


# previous approach
# def reverseOnlyLetters(S: 'str'):
#     temp = ""
#     for i in S:
#         if 65<=ord(i)<=90 or 97 <= ord(i) <=122:
#             temp += i
#
#     temp = temp [::-1] #reverse
#     output = ""
#     curr = 0
#     for i in S:
#         if not(65<=ord(i)<=90 or 97 <= ord(i) <=122): #if it's not a letter, then put it to the current position
#             output+=i
#         else:
#             output+=temp[curr] #if it's a letter, then find the letter in the reversed string.
#             curr+=1
#
#     return output
#
# print(reverseOnlyLetters("ab-cd"))
# print(reverseOnlyLetters("a-bC-dEf-ghIj"))
# print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))



