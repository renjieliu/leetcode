class Solution:
    def countMaxOrSubsets(self, nums: 'List[int]') -> int:
        def combo(output, arr, cnt, v, targetLength): #find all the combination in nums 
            if cnt == targetLength: 
                if v > output[0]:
                    output[0] = v
                    output[1] = 1
                elif v == output[0]:
                    output[1] += 1
            else:
                for i in range(len(arr)):
                    combo(output, arr[i+1:], cnt+1, (v|arr[i]) if v!=None else arr[i], targetLength)
        
        output = [-float('inf'), 0] #[max, count ]
        
        for targetLength in range(1, len(nums)+1):
            combo(output, nums, 0, None, targetLength)

        return output[1]

