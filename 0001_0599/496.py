class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        hmp = {} #record the next larget element for each number in nums2
        stk = [] #the monotone stk
        for n in nums2:
            if stk == []:
                stk.append(n)
            else:
                while stk and n > stk[-1]: #current number is greater than the top of the stk
                    hmp[stk.pop()] = n
                stk.append(n)
        while stk:
            hmp[stk.pop()] = -1
        
        
        output = []
        for n in nums1:
            output.append(hmp[n]) 
        
        return output
    



# previous approach
# class Solution:
#     def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
#         hmp = {}
#         stk = [] #monotone stack
#         for n in nums2:
#             if stk:
#                 if n < stk[-1]: #if current number is < stk head, add to stk
#                     stk.append(n)
#                 else: # current number is larger than any one in the stk
#                     while stk and n > stk[-1]:
#                         hmp[stk.pop()] = n
#             stk.append(n)
        
#         while stk: #clear the remaining items in the stk
#             hmp[stk.pop(0)] = -1
        
#         output = []
#         for n in nums1:
#             output.append(hmp[n])
#         return output
            
        

# previous approach
# class Solution:
#     def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
#         output = []
#         for n in nums1:
#             loc = float('inf')
#             for i in range(len(nums2)):
#                 find = 0
#                 if nums2[i] == n: 
#                     loc = i
#                 if nums2[i] > n and i > loc:
#                     output.append(nums2[i])
#                     find =1 
#                     break 
#             if find == 0:
#                 output.append(-1)
        
#         return output
 

# previous approach
# def nextGreaterElement(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     x1 = nums1
#     x2 = nums2
#     output = list()
#     for i in range(0, len(x1)):
#         found = -1
#         index = x2.index(x1[i])
#         for j in range(index, len(x2)):
#             if x2[j] > x1[i]:
#                 found = x2[j]
#                 break

#         output.append(found)

#     return output

# print(nextGreaterElement([2,4], [1,2,3,4]))


