class Solution:
    def getModifiedArray(self, length: int, updates: 'List[List[int]]') -> 'List[int]':
        arr = [0] * (length+1)
        for a, b, v in updates:
            arr[a] += v
            arr[b+1] += -v

        output = [arr[0]]
        for i in range(1, len(arr)):
            output.append(arr[i] + output[-1])
        return output[:-1]



#previous approach
# class Solution:
#     def getModifiedArray(self, length: int, updates: 'List[List[int]]') -> 'List[int]':
#         output = [0] * (length +1)
#         for s, e, v in updates:
#             output[s] += v
#             output[e+1] -= v
#         for i in range(1, len(output)):
#             output[i] += output[i-1]
#         return output[:-1]
#
