class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        N-=1 # turn to 0 based
        K-=1 # turn to 0 based
        if K == 0 or N == 0: return 0 #first element will always be 0
        else:
            first = [0,1]
            if N == 1 :  return first[K]
            path = [] #1. left, 2. right
            while N > 1 :
                if K%2 == 0:
                    path.append(1) #current is the right child
                else:
                    path.append(2) # current is the left child
                K =  K//2
                N -= 1
            path = path[::-1]
            #print(path)
            output = first[K]
            for p in path:
                if p ==2:
                    output = abs(output-1) #0 to 1, 1 to 0
            return output