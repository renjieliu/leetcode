class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def toNumber(s):
            return max("0", s.lstrip("0"))
        remove = 0
        arr = []
        for i, n in enumerate(num):
            while arr and arr[-1] > n: # keep popping as long as the it's smaller than the previous number
                arr.pop()
                remove += 1 
                if remove == k:
                    return toNumber("".join(arr) + num[i:])
            arr.append(n)
        total = len(num) - k # the length to keep 
        return "0" if len(arr) <= total else toNumber("".join(arr[:total]))
 
        


# previous approach

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         def toNumber(s): #take out the leading zeroes. If it's empty, just return 0 
#             for i in range(len(s)):
#                 if s[i]!= "0":
#                     return s[i:]
#             return "0"
        
#         arr = []
#         i = 0 
#         remove = 0
#         while i < len(num)-1: #find the number going down
#             arr.append(num[i])
#             while arr and arr[-1] > num[i+1]:
#                 arr.pop()
#                 remove += 1 
#                 if remove == k:
#                     arr.append(num[i+1:]) #add the rest to the arr
#                     i = len(num) #move the pointer to the end of the num and stop the iteration
#                     break
#             i+=1
    
#         arr.append(num[-1])
#         output = ""
#         for i in range(len(arr)): #take out the ones in stk, and form a string 
#             if len(output) == len(num) - k: #enough number is collected
#                 return toNumber(output)
#             output += arr[i]
        
#         return toNumber(output)
    
   
    



# previous approach

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         def toNumber(s): #take out the leading zeroes. If it's empty, just return 0 
#             for i in range(len(s)):
#                 if s[i]!= "0":
#                     return s[i:]
#             return "0"
        
#         arr = list(num)
#         stk = set()
#         stop = 0
#         i = 1 
#         while i < len(arr) and stop == 0: #find the number going down
#             if arr[i-1] > arr[i]:
#                 j = i-1 
#                 while j > -1 and arr[j] > arr[i]: # add all the previous larger than current 
#                     stk.add(j)
#                     if len(stk) == k:
#                         stop = 1
#                         break
#                     j-=1
#             i+=1 

#         output = ""
#         for i in range(len(arr)): #take out the ones in stk, and form a string 
#             if len(output) == len(num) - k: #enough number is collected
#                 return toNumber(output)
            
#             elif i not in stk:
#                 output += arr[i]
        
#         return toNumber(output)
    
    

    

# previous approach

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         if k == 0: return num
#         cnt = 0
#         t = []
#         for i in range(len(num) - 1):
#             t.append(num[i])
#             if num[i] > num[i + 1]:
#                 while t and t[-1] > num[i + 1]:
#                     t.pop()
#                     cnt += 1
#                     if cnt == k:
#                         t = ''.join(t)
#                         return str(int(t + num[i + 1:]))

#         t.append(num[-1])
#         if len(t) <= k - cnt:
#             return "0"
#         return str(int(''.join(t)[:-(k - cnt)]))

# OLD Solution
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         if len(num) == k:
#             return '0'
#         else:
#             if k == 0:
#                 return num
#             else:
#                 cnt = 0
#                 while cnt < k:
#                     found = 0
#                     for i in range(len(num) - 1):
#                         if num[i] > num[
#                             i + 1]:  # to find the first decending position, if it cannot be found, then dump the last element if the string
#                             found = 1
#                             cnt += 1
#                             num = num[:i] + num[i + 1:]
#                             break
#
#                     if found == 0:
#                         num = num[:-1]  # take out the last element
#                         cnt += 1
#
#             return '0' if num.lstrip('0') == "" else num.lstrip('0')
