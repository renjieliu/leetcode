class Solution:
    def minPartitions(self, n: str) -> int: #O(K | 1), K is the length of n
        return int(max(n)) #just to check the max digits in the n. Other digits can be manipulated with 0 or 1
            
        
        
        
# previous solution

# class Solution:
#     def minPartitions(self, n: str) -> int: #just need to find the max of the string, as others can be tweaked to 0
#         return int(max(n))

