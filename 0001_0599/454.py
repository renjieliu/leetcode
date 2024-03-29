class Solution:
    def fourSumCount(self, nums1: 'List[int]', nums2: 'List[int]', nums3: 'List[int]', nums4: 'List[int]') -> int:
        def build(arr1, arr2):
            hmp = defaultdict(int)
            for i in range(len(arr1)):
                for j in range(len(arr2)):
                    hmp[arr1[i] + arr2[j]]+=1
            return hmp
        A = build(nums1, nums2)
        B = build(nums3, nums4)
        # print(hmp_1)
        # print(hmp_2)
        output = 0
        for k, v in A.items(): #for each k, check how many -k are in the B
            output += v*B[-k]
        return output 
                

        
# previous approach 

# class Solution:
#     def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> int:
#         hmp_AB = {}
#         hmp_CD = {}

#         for i in range(len(A)):
#             for j in range(len(B)):
#                 curr = A[i] + B[j]
#                 if curr not in hmp_AB:
#                     hmp_AB[curr] = 0
#                 hmp_AB[curr] += 1

#                 curr = C[i] + D[j]
#                 if curr not in hmp_CD:
#                     hmp_CD[curr] = 0
#                 hmp_CD[curr] += 1

#         output = 0

#         # print('AB', hmp_AB)
#         # print('CD', hmp_CD)

#         for k, v in hmp_AB.items():
#             if -k in hmp_CD:
#                 output += v * hmp_CD[-k]
#         return output



# previous approach
# def fourSumCount(A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]'):
#     result = {}
#     cnt = 0
#
#     for i in range(len(A)):
#         for j in range(len(B)):
#             if A[i] + B[j] not in result.keys():
#                 result[A[i] + B[j]] = 0
#             result[A[i] + B[j]] +=1
#
#     for x in range(len(C)):
#         for y in range(len(D)):
#             if -1*(C[x] + D[y]) in result.keys():
#                 cnt += result[-1*(C[x] + D[y])]
#
#
#
#     # result = []
#     # for i in range(len(A)):
#     #     for j in range(len(C)):
#     #         result.append(A[i] + C[j])
#     #
#     # for i in range(len(B)):
#     #     for j in range(len(D)):
#     #         if -(B[i] + D[j]) in result:
#     #             cnt+=1
#     #
#     # result = []
#     # for i in range(len(A)):
#     #     for j in range(len(D)):
#     #         result.append(A[i] + D[j])
#     #
#     # for i in range(len(B)):
#     #     for j in range(len(C)):
#     #         if -(B[i] + C[j]) in result:
#     #             cnt+=1
#
#
#     return cnt
#
# # print(fourSumCount([ 1, 2]
# # ,[-2,-1]
# # ,[-1, 2]
# # ,[ 0, 2]))
#
# print(fourSumCount([-1,-1]
# ,[-1,1]
# ,[-1,1]
# ,[1,-1]))