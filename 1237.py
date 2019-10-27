"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        i = 1
        output = []
        while i<=1000:
            j = 1
            if customfunction.f(i,j) > z:
                return output
            while j <=1000:
                t = customfunction.f(i,j)
                if t== z:
                    output.append([i,j])
                    break
                elif t > z:
                    break
                j+=1

            i+=1

        return output







