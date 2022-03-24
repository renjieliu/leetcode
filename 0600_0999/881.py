class Solution:
    def numRescueBoats(self, people: 'List[int]', limit: int) -> int:
        people.sort()
        r=len(people)-1
        l=0
        cnt = 0 
        while l<=r: #there're still people left
            cnt += 1 
            if l < r and people[r] + people[l] <= limit: #people at the front of the line can go on the same boat
                l+=1
            r-= 1
        return cnt
    


# previous approach

# class Solution:
#     def numRescueBoats(self, people: 'List[int]', limit: int) -> int:
#         people.sort()
#         cnt = 0
#         left = 0
#         right =len(people)-1
#         while left <=right:
#             cnt +=1
#             if people[right] + people[left] <= limit:
#                 right -=1
#                 left +=1
#             else:
#                 right -=1
#         return cnt



# previous approach

# class Solution:
#     def numRescueBoats(self, people: 'List[int]', limit: int) -> int:
#         cnt = 0
#         people.sort()
#         r = len(people) - 1
#         l = 0
#         while r >= 0:
#             curr = people[r]
#             if curr != float('inf'):
#                 if curr == limit:
#                     cnt += 1
#                     people[r] = float('inf')
#                 else:
#                     rem = limit - curr
#                     if people[l] <= rem:
#                         people[l] = float('inf')
#                         l+=1
#                     people[r] = float('inf')
#                     cnt += 1

#             r -= 1

#         return cnt


