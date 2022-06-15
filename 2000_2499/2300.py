class Solution:
    def successfulPairs(self, spells: 'List[int]', potions: 'List[int]', success: int) -> 'List[int]': # O( NlogN | N )
        def binFind(arr, v): # binary find how many elements >= v
            output = 0
            s = 0 
            e = len(arr)-1
            while s <= e :
                mid = s - (s-e)//2 
                if arr[mid] >= v:
                    output = len(arr)-1-mid+1 #how many elements >= v (last index - curr index + 1)
                    e = mid - 1
                else:
                    s = mid + 1
            return output 
        
        output = []
        potions.sort()
        for s in spells:
            #print(success/s)
            output.append(binFind(potions, success/s))
        return output
    


