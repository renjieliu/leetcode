class Solution:
    def wateringPlants(self, plants: 'List[int]', capacity: int) -> int:
        cnt = 0
        k = capacity
        for i in range(len(plants)-1):
            cnt += 1 # plant current flower
            capacity -= plants[i] # remaining of the can 
            if capacity < plants[i+1]: # refill the can, walk to the front, and come back
                cnt += (i+1)*2 
                capacity = k 
        cnt += 1 # for the last flower
        return cnt

    