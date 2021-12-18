class Solution:
    def atMostNGivenDigitSet(self, digits: 'List[str]', n: int) -> int:
        cnt = 0 
        n = str(n)
        for i in range(1, len(n)):
            cnt += (len(digits))**i
        output = [0]
        def dfs(output, digits, n):
            if n:
                d = sum([1 for d in digits if d < n[0]]) #digit less than current first digit 
                L = len(digits) # length of the digits
                P = len(n)-1 
                # print(d, L, P)
                if len(n) == 1 and n[0] in digits: #last digit
                    d += 1 
                output[0] += d * (L**P) # premutation, d * (all digits ** rest)
                if n[0] in digits : #if d == 0, no need to move on.
                    dfs(output,digits, n[1:])               

        dfs(output,digits, n)
        # print(output)   
        return cnt + output[0]
            

            
# previous approach
# class Solution:
#     def atMostNGivenDigitSet(self, digits: 'List[str]', n: int) -> int:
#         output = [0]
#         for i in range(1, len(str(n))):  # for the first x-1 digits, pick any from the nums..
#             output[0] += (len(digits) ** i)
#         # print(output)
#         digits.sort()

#         def helper(output, target, arr):  # iterate through each digit. if <, same as above,  if == check the rest
#             for i, d in enumerate(arr):  # to calculate the same length
#                 if d < target[0]:
#                     output[0] += (len(arr) ** (len(target) - 1))
#                 elif d == target[0]:
#                     if len(target[1:]) == 0:
#                         output[0] += 1
#                     else:
#                         helper(output, target[1:], arr)
#                 elif d > target[0]:
#                     break

#         helper(output, str(n), digits)

#         return output[0]
