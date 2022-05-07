class Solution:
    def findPermutation(self, s: str) -> 'List[int]': #O(N | N)
        stk = [1] #initialize the stack
        output = []
        for i, c in enumerate(s): # go through the string
            if c == "I":
                while stk:
                    output.append(stk.pop())
            stk.append(i+2) #add the following number to the stack
            
        while stk: # add the rest to the output
            output.append(stk.pop())
        
        return output
    


# class Solution:
#     def findPermutation(self, s: str) -> 'List[int]': #O(N | N)
#         output = [] 
#         stk = [1]
#         for i, c in enumerate(s): # mono stk
#             if c == "I": # pop the previous stack
#                 while stk:
#                     output.append(stk.pop())
#             stk.append(i+2) # add the current to the stack
        
#         while stk: #take out the rest of the stk
#             output.append(stk.pop())
#         return output
    


# previous solution

# class Solution:
#     def findPermutation(self, s: str) -> 'List[int]':  # "DI" [2,1,3]
#         def reverse(arr, s, e):  # reverse arr, from s to e
#             t = arr[s:e + 1][::-1]
#             for _ in range(s, e + 1):
#                 arr[_] = t.pop(0)

#         output = [_ + 1 for _ in range(len(s) + 1)]
#         i = 0
#         d_cnt = 0
#         while i < len(s):
#             if s[i] == 'D':
#                 d_cnt += 1
#             elif s[i] == 'I':
#                 if d_cnt != 0:
#                     start = i - d_cnt
#                     end = i
#                     reverse(output, start, end)  # reverse the digits with continuous d's
#                     d_cnt = 0
#             i += 1

#         if d_cnt != 0:
#             start = i - d_cnt
#             end = i
#             reverse(output, start, end)

#         return output




