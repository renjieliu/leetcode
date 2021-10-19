class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        # 4J+2S = tomatoSlices
        # J+S = cheeseSlices
        # find the root for above equation
        J = (tomatoSlices - 2*cheeseSlices)/2
        S = (tomatoSlices - 4*J)/2
        #print(J, S)
        if J < 0 or S < 0 :
            return []
        elif int(J) == J or int(S) == S:
            return [int(J),int(S)]
        else:
            return []
