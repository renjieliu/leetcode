class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        def helper(output, s, curr, start):
            if start == len(s): #at the end of the string, all prev partitons are palindrome
                output.append(curr)
            for i in range(start,len(s)):
                if s[start:i+1] == s[start:i+1][::-1]: # current partition is palindrome
                    helper(output, s, curr + [s[start:i+1]], i+1) # keep checking from the next position
        
        output = []
        helper(output, s, [], 0)
        return output
    
    


# class Solution:
#     def partition(self, s: str) -> 'List[List[str]]':
#         def isP(s):
#             return s == s[::-1] and s != ""  # return if the s is a palindrome

#         def helper(output, s, curr): #this is a simple DFS approach
#             if len(s) == 0:
#                 output.append(curr)
#             else:
#                 for i in range(len(s) + 1):
#                     if isP(s[:i]):
#                         helper(output, s[i:], curr + [s[:i]])

#         output = []
#         helper(output, s, [])
#         return output


