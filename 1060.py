class Solution:
    def missingElement(self, nums: 'List[int]', k: int) -> int:
        full_length = nums[-1] - nums[0]+1
        missing = full_length - len(nums)
        if k > missing: #if outside the right bound, then add the rest of the missing number..
            return nums[-1] + (k-missing)
        else:  #check in the current array
            cnt = 0
            i=0
            while i < len(nums)-1:
                curr = nums[i]
                while curr+1 != nums[i+1]:
                    curr += 1
                    cnt +=1
                    if cnt == k:
                        return curr
                i+=1