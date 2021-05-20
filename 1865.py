class FindSumPairs:

    def __init__(self, nums1: 'List[int]', nums2: 'List[int]'): # using hashmap for nums1 and nums2 to speedup the lookup
        self.hmp1 = {}
        for n in nums1:
            if n not in self.hmp1:
                self.hmp1[n] = 0
            self.hmp1[n] += 1
        self.nums2 = nums2
        self.hmp2 = {}
        for n in nums2:
            if n not in self.hmp2:
                self.hmp2[n] = 0
            self.hmp2[n] += 1

    def add(self, index: int, val: int) -> None:
        self.hmp2[self.nums2[index]] -= 1
        if self.hmp2[self.nums2[index]] == 0:
            del self.hmp2[self.nums2[index]]
        self.nums2[index] += val
        if self.nums2[index] not in self.hmp2:
            self.hmp2[self.nums2[index]] = 0
        self.hmp2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        cnt = 0
        for k in self.hmp1.keys(): #go through the first list, and see of the remaining can be found in the second list
            if tot - k in self.hmp2:
                cnt += (self.hmp2[tot - k] * self.hmp1[k])
        return cnt




# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)