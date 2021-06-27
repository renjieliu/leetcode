class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        output = ""
        for c in s:
            output += c
            while len(output) >= len(part) and output[-len(part):] == part:
                output = output[:-len(part)]
        return output

# previous approach
# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         while part in s:
#             s = s.replace(part, '')
#         return s

