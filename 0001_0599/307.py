class NumArray:

    def __init__(self, nums: 'List[int]'): #this is to build the segment tree O(n)
        n = len(nums)
        total = 1
        layer = 0
        while 2**layer < n:
            layer += 1
            total += 2**layer
        self.seg = [0] * total
        self.nums = nums
        def buildSeg(nums, seg, node, start, end):
            if start == end:
                seg[node] = nums[start]
            else:
                mid = (start+end)//2
                left = buildSeg(nums, seg, node*2+1, start, mid)
                right = buildSeg(nums, seg, node*2+2, mid+1, end)
                seg[node] = left + right
            return seg[node]
        buildSeg(nums, self.seg, 0, 0, n-1)
        #print(self.seg)



    def update(self, index: int, val: int) -> None: # to update the segment tree O(logn)
        def updateSeg(seg, node, idx, val, start, end):
            if start == end:
                seg[node] = val
            else:
                mid = (start + end)//2
                if idx <= mid:
                    updateSeg(seg, node*2+1, idx, val, start, mid)
                else:
                    updateSeg(seg, node*2+2, idx, val, mid+1, end)

                seg[node] = seg[node*2+1] + seg[node*2+2]

        updateSeg(self.seg, 0, index, val, 0, len(self.nums)-1)



    def sumRange(self, left: int, right: int) -> int: # to query O(logn)
        def query(seg, node, left, right,start, end):
            #print(left, right, start, end)
            if left > end or right < start:
                return 0
            elif start >= left and end <= right:
                return seg[node]
            elif start == end:
                return seg[node]
            mid = (start+end) // 2
            return query(seg, node*2+1, left, right, start, mid) + query(seg, node*2+2, left, right, mid+1, end)

        return query(self.seg, 0, left, right, 0, len(self.nums)-1)









# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)





# previous approach
# import math
#
# class NumArray:
#
#     def __init__(self, nums: 'List[int]'):
#
#         def buildTree(in_arr, in_tree, currNode, currNodeRange):
#             if currNodeRange[0] == currNodeRange[1]:
#                 in_tree[currNode] = in_arr[currNodeRange[0]]
#             else:
#                 mid = sum(currNodeRange)//2
#                 left_child = 2 * mid +1
#                 right_child = left_child + 1
#                 buildTree(in_arr, in_tree, left_child, [currNodeRange[0], mid])
#                 buildTree(in_arr, in_tree, right_child, [mid+1,currNodeRange[1]])
#                 in_tree[currNode]  = in_tree[left_child] + in_tree[right_child]
#
#         self.arr = nums.copy()
#
#         if len(self.arr) <2:
#             self.tree = self.arr
#         else:
#             nodes_to_be_filled = len(nums)*2 - 1
#             layers_for_the_nodes = math.log(nodes_to_be_filled, 2)//1 + 1
#             nodes_total = 2**layers_for_the_nodes - 1
#             self.tree = [0] * int(nodes_total)
#
#             buildTree(self.arr, self.tree, 0, [0, len(nums)-1])
#
#     def update(self, i: int, val: int) -> None:
#         def updateTree(in_arr, in_tree, currNode, currNodeRange, i, val):
#             if currNodeRange[0] == currNodeRange[1]:
#                 in_arr[i] = val
#                 in_tree[currNode] = val
#             else:
#                 mid = sum(currNodeRange)//2
#                 left_child = 2 * mid +1
#                 right_child = left_child + 1
#                 if i <= mid:
#                     updateTree(in_arr, in_tree, left_child, [currNodeRange[0], mid], i, val)
#                 else:
#                     updateTree(in_arr, in_tree, right_child, [mid+1, currNodeRange[1]], i, val)
#
#                 in_tree[currNode] = in_tree[left_child] + in_tree[right_child]
#
#         updateTree(self.arr, self.tree, 0, [0, len(self.arr)-1], i, val)
#
#     def sumRange(self, i: int, j: int) -> int:
#         def query(in_arr, in_tree, currNode, currNodeRange, i, j):
#
#             if i>currNodeRange[1] or j < currNodeRange[0]:
#                 return 0
#             elif currNodeRange[0] == currNodeRange[1] or (currNodeRange[0]>= i and currNodeRange[1] <= j ) :
#                 return in_tree[currNode]
#
#             else:
#                 mid = sum(currNodeRange)//2
#                 left_child = 2 * mid +1
#                 right_child = left_child + 1
#                 left = query(in_arr, in_tree, left_child, [currNodeRange[0], mid], i, j)
#                 right = query(in_arr, in_tree, right_child, [mid+1, currNodeRange[1]], i, j)
#                 return left + right
#
#         return query(self.arr, self.tree, 0, [0, len(self.arr)-1], i, j)
#
#
#
# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(i,val)
# # param_2 = obj.sumRange(i,j)
#
#
#
#
#
#
#
