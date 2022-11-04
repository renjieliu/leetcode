class Solution:
    def minMutation(self, start: str, end: str, bank: 'List[str]') -> int: # O( 2**N | 1 ), N being the length of the bank
        if end not in bank: #if the end is not in the bank, it's invalid
            return -1
        else:
            def helper(change, curr, end, bank, output):
                if curr == end:
                    output[0] = min(output[0], change)
                else:
                    valid = lambda a, b: len([i for i in range(len(a)) if a[i]!=b[i]]) == 1 # if only one character difference
                    for i in range(len(bank)):
                        if valid(curr, bank[i]):
                            helper(change+1, bank[i], end, bank[:i] + bank[i+1:], output)
            
            output = [float('inf')]
            helper(0, start, end, bank, output)
            return output[0] if output[0] != float('inf') else -1
        
    
            



# previous solution

# class Solution:
#     def minMutation(self, start: str, end: str, bank: 'List[str]') -> int:
#         def diff(A,B):
#             cnt = 0
#             for i in range(len(A)): #There're 8 characters in total.
#                 if A[i] != B[i]:
#                     cnt +=1
#             return cnt
#         dp = [None for _ in bank] #initialize everything as -1, to record how many steps to reach end
#         find = -1
#         for i in range(len(bank)):
#             if bank[i] == end:
#                 dp[i] = 0
#                 find = i
#                 break
#         if find == -1: return -1 # end is not in the bank
#         curr = [find] #set end as current token
#         while curr: #this is to populate the dp
#             to_find = curr.pop(0)
#             i = 0
#             while i < len(bank):
#                 if dp[i] == None and diff(bank[i], bank[to_find]) == 1:
#                     dp[i] = dp[to_find] + 1
#                     curr.append(i)
#                 i+=1

#         output = float('inf')
#         i = 0
#         while i < len(bank):
#             if diff(bank[i], start) ==1 and dp[i] != None:
#                 output = min(dp[i]+1, output)
#             i+=1
#         return -1 if output == float('inf') else output




