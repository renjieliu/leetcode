class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        def isP(s):
            return s == s[::-1] and s != ""  # return if the s is a palindrome

        def helper(output, s, curr): #this is a simple DFS approach
            if len(s) == 0:
                output.append(curr)
            else:
                for i in range(len(s) + 1):
                    if isP(s[:i]):
                        helper(output, s[i:], curr + [s[:i]])

        output = []
        helper(output, s, [])
        return output


