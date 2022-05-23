# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int: #O(N2 | N)
        arr = [0] * n # to record how many people knows current person
        people = [0] * n # to record how many people current person knows
        for i in range(n):
            for j in range(n):
                if i != j:
                    t = knows(i, j)
                    arr[j] += t #add know to arr 
                    people[i] += t #add know to current people
        for i, a in enumerate(arr):
            if a == n-1 and people[i] == 0:
                return i
        # print(arr, people)
        return -1
    
    


# previous solution

# # The knows API is already defined for you.
# # return a bool, whether a knows b
# # def knows(a: int, b: int) -> bool:

# class Solution:
#     def findCelebrity(self, n: int) -> int:
#         cele = set()
#         for i in range(n):
#             if knows(0, i) == 1: # possible celebrity
#                 cele.add(i)

#         for i in range(1, n):
#             for c in cele:
#                 if knows(i,c) == 0: #if other people does not know him/her, curr is not a celebrity
#                     cele.remove(c)
#                     break

#         if cele == set():
#             return -1
#         else:
#             output = []
#             for c in cele: # check how many people the celebrity know
#                 cnt = 0
#                 for i in range(n):
#                     if knows(c, i) == 1:
#                         cnt +=1
#                 if cnt == 1 :
#                     output.append(c)
#             if len(output) == 1:
#                 return output[0]
#             else:
#                 return -1




