class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> int: # Time: O(N), Space: O(N)
        gas += gas 
        cost += cost
        curr = 0
        arr = []
        for i in range(len(gas)):
            curr += gas[i] - cost[i] 
            if curr < 0: #if current total is less than 0, just add -1
                arr.append(-1) 
                curr = 0 
            else:
                arr.append(curr)
        
        # print(arr)
        negPos = [float('inf') for _ in gas] + [float('inf')] #to record the first -1 on the right or itself
        
        
        for i in range(len(arr)-1, -1, -1): # find the first negative on the right, or itself
            if arr[i] < 0:
                negPos[i] = i
            else:
                negPos[i] = negPos[i+1]
        
        # print(negPos)
        for i in range(len(gas)//2):
            if negPos[i]-i >= len(gas)//2 + 1: #current total non negative length
                return i 
        
        return -1
    
    

# previous approach

# class Solution:
#     def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> int:
#         length = len(gas)
#         gas = gas + gas
#         cost = cost + cost

#         for i in range(len(gas)):
#             currGas = 0
#             startOver = 0
#             rem = 0
#             for j in range(i, i + length):
#                 currGas = rem + gas[j]
#                 rem = currGas - cost[j]
#                 if rem < 0:
#                     startOver = 1
#                     break
#             if startOver == 0:
#                 return i

#             if i >= length:
#                 return -1