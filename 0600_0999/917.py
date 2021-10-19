class Solution: # RL 20210914: 2 pointers approach
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1
        letter = lambda x: 1 if (65<=ord(x)<=90 or 97 <= ord(x)<=122) else 0
        while l <= r: #2 pointers, once meet letters on the left and right, just swap them
            while l < r and letter(s[l]) == 0:
                l+=1
            while r > l and letter(s[r]) == 0:
                r-=1
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
            # print(s)
        return "".join(s)


# previous approach
# class Solution:
#     def reverseOnlyLetters(self, s: str) -> str:
#         tmp = ""
#         s = list(s)
#         for i in range(len(s)):
#             curr = s[i]
#             if 65 <= ord(curr) <= 90 or 97<=ord(curr) <=122:
#                 tmp+=curr
#                 s[i] = "A"
#         tmp = list(tmp)
#         for i in range(len(s)):
#             if s[i] == "A":
#                 s[i] = tmp.pop() #pop from the tail for reverse
#
#         return "".join(s)


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



