class Solution:
    def construct2DArray(self, original: 'List[int]', m: int, n: int) -> 'List[List[int]]':
        if len(original) != m*n:
            return []
        else:
            output = [[]]
            for i in range(len(original)):
                output[-1].append(original[i])
                if len(output[-1]) == n and i < len(original)-1:
                    output.append([])
            return output


# previous approach
# class Solution:
#     def construct2DArray(self, original: 'List[int]', m: int, n: int) -> 'List[List[int]]':
#         if len(original) != m*n:
#             return []
#         else:
#             output = [[]]
#             while original:
#                 output[-1].append(original.pop(0))
#                 if len(output[-1]) == n and original:
#                     output.append([])
#             return output
#
#
#
