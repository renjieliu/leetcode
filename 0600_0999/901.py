class StockSpanner:

    def __init__(self): 
        self.dp = [] #[idx, cnt] , idx == the first index with number <= curr, and cnt numbers are in between
        self.arr = [] # num
        

    def next(self, price: int) -> int: # O( N | N )
        if self.arr == []:
            self.arr.append(price)
            self.dp.append([0, 1])
        else: 
            stop = len(self.arr)-1 
            cnt = 1 
            while price >= self.arr[stop]:
                cnt += self.dp[stop][1]
                stop = self.dp[stop][0]-1 # to check if current price is larger than the previous threshold 
                if stop < 0:
                    break
            self.arr.append(price)
            self.dp.append([stop+1, cnt]) # number at "stopped" index is either -1, or > price
            
        return self.dp[-1][1]  # return the count
            
            
            
            



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)






# previous solution

# class StockSpanner:
#     def __init__(self):
#         self.stk = []
#         self.dp = []  # [startIndex, cnt]

#     def next(self, price: int) -> int:
#         if len(self.stk) == 0:
#             self.stk.append(price)
#             self.dp.append([0, 1])
#         else:
#             if price >= self.stk[-1]:  # the last added element
#                 cnt = 1  # itself
#                 nextcheck = len(self.stk) - 1
#                 while price >= self.stk[nextcheck]:
#                     cnt += self.dp[nextcheck][1]
#                     nextcheck = self.dp[nextcheck][0] - 1
#                     if nextcheck < 0: break
#                 self.stk.append(price)
#                 self.dp.append([nextcheck + 1, cnt])

#             else:
#                 self.stk.append(price)
#                 self.dp.append([len(self.stk) - 1, 1])

#         # print(self.dp)

#         return self.dp[-1][1]





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Approach 1
# class StockSpanner:
#     def __init__(self):
#         self.stk = []
#         self.rem = []
#
#     def next(self, price: int) -> int:
#         self.stk.append(price)
#         self.rem.append(1)
#         # below is to crash the stk and return the final result
#         while self.rem:
#             if len(self.rem) == 1:
#                 break
#             else:
#                 if self.stk[-2] <= self.stk[-1]:
#                     self.stk[-2] = self.stk[-1]
#                     self.stk.pop()
#                     self.rem[-1] += self.rem[-2]
#                     self.rem[-2] = self.rem[-1]
#                     self.rem.pop()
#                 else:
#                     break
#
#         return self.rem[-1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)