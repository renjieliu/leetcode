class Solution:
    def reachNumber(self, target: int) -> int:
        def findLayer(N): # use binary search to find the smallest sum [1..number] greater or eq to N
            s = 1
            e = N
            while s<=e:
                mid = (s+e)//2
                t = (mid+1)*mid//2
                if t < N:
                    s = mid + 1
                else:
                    e = mid - 1
            return s #this is the min layer with the sum [1..number] > N
        #Based on the problem desciption, we can draw a tree to simulate the issue, and find the pattern in with the tree.
        #find the layer, if it's the target, return
        #if it's layer end is same even (odd), then return layer
        #if not, add layer, until is even (odd)
        goal = abs(target)
        if goal ==0:
            return 0
        else:
            #find the layer
            layer= findLayer(goal)
            t = layer*(1+layer)//2
            if goal%2==0:
                if t%2 ==0:
                    return layer
                else:
                    while t%2!=0:
                        layer+=1
                        t+=layer
                    return layer
            else:
                if t%2==1:
                    return layer
                else:
                    while t%2==0:
                        layer+=1
                        t+=layer
                    return layer

