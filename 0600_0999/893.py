class Solution:
    def numSpecialEquivGroups(self, A: 'List[str]') -> int:
        def f(w): # check khow many times the letter is on the even, and on the odd position
            arr = [0] * 52
            for i, c in enumerate(w):
                arr[ord(c)-ord('a') + 26*(i%2)] += 1
            return tuple(arr)
        return len({f(w) for w in A})


# previous approach
# class Solution:
#     def numSpecialEquivGroups(self, A: 'List[str]') -> int:
#         def isSE(a, b): #same characters on the odd / even index.Then they can be swapped.
#             if len(a) != len(b):
#                 return False
#             else:
#                 odd_a = []
#                 even_a = []
#                 odd_b = []
#                 even_b = []
#                 for i, c in enumerate(a):
#                     if i % 2 ==0:
#                         even_a.append(c)
#                         even_b.append(b[i])
#                     else:
#                         odd_a.append(c)
#                         odd_b.append(b[i])
#                 return sorted(even_a) == sorted(even_b) and sorted(odd_a) == sorted(odd_b)
#
#         taken = [0] * len(A) # if the word has been taken as special equivalent with another
#         groups = []
#         for i in range(len(A)): # check one by one if they are special equivalent
#             if taken[i] == 0:
#                 groups.append([A[i]])
#                 taken[i] = 1
#                 for j in range(i+1, len(A)):
#                     if taken[j] == 0:
#                         if isSE(A[i], A[j]):
#                             taken[j] = 1
#                             groups[-1].append(A[j])
#
#
#         return len(groups)