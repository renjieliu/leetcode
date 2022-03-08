class Solution:
    def findStrobogrammatic(self, n: int) -> 'List[str]': # time + Space O( N*(5 ^ (N/2)) | N*(5 ^ (N/2)) )
        def perm(pool, curr, arr, n):
            if len(curr) == n: 
                pool.append(curr)
            else:
                for i in range(len(arr)):
                    perm(pool, curr+arr[i] , arr, n)
        
        def mirror(s):
            output = s
            for i in reversed(s):
                output += ("6" if i == "9" else ("9" if i == "6" else i))
            return output
            
        if n == 1:
            return ["0", "1", "8"]
        pool = []
        arr = ["0", "1", "6", "8","9"]
        perm(pool, "", arr, n//2) #build the first half
        if n%2 == 0:
            return [mirror(_) for _ in pool if _[0] != "0" ] # mirror the first half and attach, as long as the first character != "0"
        else:
            arr = [mirror(_) for _ in pool if _[0] != "0"] # insert 0, 1, 8 in the middle
            output = []
            for i in ["0", "1", "8"]:
                for a in arr:
                    output.append(a[:n//2] + i + a[n//2:])
            return output
                
                



# previous approach

# class Solution:
#     def findStrobogrammatic(self, n: int) -> 'List[str]':
#         def combo(A, B):
#             output = []
#             for a in A:
#                 for b in B:
#                     output.append(a + b)
#             return output

#         if n == 1:
#             return ['1', '8', '0']
#         else:
#             pool = ['1', '8', '0', '6', '9']
#             temp = ['']
#             i = 0
#             while i < n // 2:
#                 temp = combo(pool, temp)
#                 i += 1
#             output = []
#             if n % 2 == 0:
#                 for t in temp:
#                     if t[0] != '0':
#                         output.append(t + t[::-1].replace('6', '7').replace('9', '6').replace('7',
#                                                                                               '9'))  # reverse the first half, 9 to 6, and 6 to 9
#                 return output
#             else:
#                 for p in ['1', '8', '0']:
#                     for t in temp:
#                         if t[0] != '0':
#                             output.append(t + p + t[::-1].replace('6', '7').replace('9', '6').replace('7',
#                                                                                                       '9'))  # reverse the first half, plus 0, 1, 8, and flip 6 and 9
#                 return output





