class SparseVector:
    def __init__(self, nums: 'List[int]'): # O( N | N ) 
        self.nonZero = {} # to record the non-zero loc
        for i, n in enumerate(nums):
            if n:
                self.nonZero[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int: # O( N | N ) 
        output = 0 
        for loc, v in self.nonZero.items(): 
            output += v * (vec.nonZero[loc] if loc in vec.nonZero else 0) # add only when the same loc in vec is also non-zero.             
        return output
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)






# previous solution

# class SparseVector:
#     def __init__(self, nums: 'List[int]'):
#         self.arr = nums

#         # Return the dotProduct of two sparse vectors

#     def dotProduct(self, vec: 'SparseVector') -> int:
#         return sum([a * b for a, b in list(zip(self.arr, vec.arr))])

# # Your SparseVector object will be instantiated and called as such:
# # v1 = SparseVector(nums1)
# # v2 = SparseVector(nums2)
# # ans = v1.dotProduct(v2)