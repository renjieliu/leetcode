class SparseVector:
    def __init__(self, nums: 'List[int]'):
        self.arr = nums

        # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([a * b for a, b in list(zip(self.arr, vec.arr))])

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)