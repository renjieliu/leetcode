class Solution:
    def numRescueBoats(self, people: 'List[int]', limit: int) -> int:
        people.sort()
        cnt = 0
        left = 0
        right =len(people)-1
        while left <=right:
            cnt +=1
            if people[right] + people[left] <= limit:
                right -=1
                left +=1
            else:
                right -=1
        return cnt

