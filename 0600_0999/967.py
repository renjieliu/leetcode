class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> 'List[int]': # O( N*K | N*K )
        cnt = 1 
        stk = [1,2,3,4,5,6,7,8,9]
        while cnt < n: # BFS to get all the possible numbers from current digit
            nxt = []
            while stk:
                curr = stk.pop()
                d = curr % 10 
                if d + k < 10:
                    nxt.append(curr*10+d+k)
                if k != 0 and d - k >= 0 : # if it's valid and k != 0, k==0 has been added with d+k. No need to add again.
                    nxt.append(curr*10+d-k)
            stk = nxt             
            cnt += 1 
        return stk
        
        



# previous solution

# class Solution:
#     def numsSameConsecDiff(self, N: int, K: int) -> 'List[int]':
#         output = []
#         for i in range(1, 10):
#             stk = [str(i)]
#             while stk and len(stk[0]) < N:
#                 curr = stk.pop(0)
#                 if 0 <= int(curr[-1]) - K <= 9:
#                     stk.append(curr + str(int(curr[-1]) - K))
#                 if 0 <= int(curr[-1]) + K <= 9:
#                     stk.append(curr + str(int(curr[-1]) + K))
#             for s in stk:
#                 if len(s) == N:
#                     output.append(int(s))

#         if N == 1:
#             output.append(0)

#         return sorted(list(set(output)))




# previous solution

# class Solution:
#     def numsSameConsecDiff(self, N, K):
#         #N - digits
#         #K - diff
#         temp = [str(_) for _ in range(10)]
#         output = []
#         width = 1
#         iter = 0
#         while width < N:
#             length = len(temp)
#             while iter < length:
#                 curr = temp[iter]
#                 cal_add = int(str(curr)[-1])+K
#                 if cal_add <10:
#                     temp.append ( str(curr) + str(cal_add))
#                 cal_minus = int(str(curr)[-1])-K
#                 if cal_minus >=0 and cal_minus!=cal_add:
#                     temp.append( str(curr) + str(cal_minus) )

#                 iter+=1

#            # print(temp)

#             width+=1

#         for i in temp:
#             o = int(i)
#             if len(str(o))== N:
#                 output.append(o)

#         return output


# previous solution 

# class Solution:
#     def numsSameConsecDiff(self, N, K):
#         #N - digits
#         #K - diff
#         temp =[0,1,2,3,4,5,6,7,8,9]
#         output = []
#         width = 1
#         iter = 0
#         while width < N:

#             length = len(temp)
#             while iter < length:
#                 curr = temp[iter]

#                 cal_add = int(str(curr)[-1])+K
#                 if cal_add <10:
#                     temp.append ( str(curr) + str(cal_add))
#                 cal_minus = int(str(curr)[-1])-K
#                 if cal_minus >=0:
#                     temp.append( str(curr) + str(cal_minus) )

#                 iter+=1

#            # print(temp)

#             width+=1

#         for i in temp:
#             if len(str(int(i)))== N:
#                 output.append(int(i))

#         return list(set(output))



