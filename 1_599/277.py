# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        cele = set()
        for i in range(n):
            if knows(0, i) == 1: # possible celebrity
                cele.add(i)

        for i in range(1, n):
            for c in cele:
                if knows(i,c) == 0: #if other people does not know him/her, curr is not a celebrity
                    cele.remove(c)
                    break

        if cele == set():
            return -1
        else:
            output = []
            for c in cele: # check how many people the celebrity know
                cnt = 0
                for i in range(n):
                    if knows(c, i) == 1:
                        cnt +=1
                if cnt == 1 :
                    output.append(c)
            if len(output) == 1:
                return output[0]
            else:
                return -1

                    