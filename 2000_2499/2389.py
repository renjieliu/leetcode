class Solution:
    def answerQueries(self, nums: 'List[int]', queries: 'List[int]') -> 'List[int]': # O( NlogN | N )
        pre = [0]
        for n in sorted(nums): # prefix sum for the sorted(nums)
            pre.append(pre[-1] + n)
        pre.pop(0)
        
        def binFind(arr, v): # find the last index in the arr, with value <= v 
            s = 0 
            e = len(arr)-1
            output = 0
            while s <= e:
                mid = s - (s-e) //2 
                if arr[mid] > v:
                    e = mid - 1 
                else:
                    s = mid + 1 
            return s

        return [binFind(pre, q) for q in queries] 
                    
