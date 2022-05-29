class Solution:
    def maxProduct(self, words: 'List[str]') -> int: #O(N2 | N)
        output = 0
        arr = [set(w) for w in words]
        
        for i in range(len(arr)): # for each possible pair, check if there're common letters between the two. 
            for j in range(i+1, len(arr)):
                if arr[i] & arr[j] == set():
                    output = max(output, len(words[i]) * len(words[j]))
        return output
    


# previous solution

# class Solution:
#     def maxProduct(self, words: 'List[str]') -> int:
#         output = 0
#         arr = []
#         for w in words:
#             arr.append(set(w))
#         for i in range (len(arr)):
#             for j in range(i+1, len(arr)):
#                 if arr[i] & arr[j] == set():
#                     output = max(output, len(words[i]) * len(words[j]))
#         return output
