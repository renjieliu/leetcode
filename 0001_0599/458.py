class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int: # RL 20220805 copied solution, O( 1 | 1 )
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))
    
    

# previous solution 

# import math;

# class Solution:
#     def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
#         states = minutesToTest // minutesToDie + 1
#         return math.ceil(math.log(buckets) / math.log(states))


