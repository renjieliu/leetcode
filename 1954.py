class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        #n == 1: (Edge = 2+1+2+1+2+1+2+1)
        #n == 2: (n==1 + (newEdge = 4+3+2+3 + 4+3+2+3 + 4+3+2+3 + 4+3+2+3))
        #n == 3: (n==2 + (newEdge = 6+5+4+3+4+5 + 6+5+4+3+4+5 + 6+5+4+3+4+5 + 6+5+4+3+4+5) )
        total = 0
        n = 0
        while total < neededApples:
            n+=1
            start = n
            end = n*2
            eachEdge = ( (start+end)*(end-start+1)//2) * 2  - 2*n - n
            #print(n, eachEdge)
            total += 4* eachEdge

        return 2*n*4 #perimeter = 4 * each edge


