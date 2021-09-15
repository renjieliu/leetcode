class Solution:
    def maxTurbulenceSize(self, arr: 'List[int]') -> int:
        if len(arr) == 1:
            return 1
        else:
            output = 1
            cnt = 1
            for i in range(1, len(arr)):
                if i == 1:
                    if arr[i] > arr[i-1]:
                        output = max(output, cnt+1)
                        cnt += 1
                        sig = -1 # next one should be smaller
                    elif arr[i] < arr[i-1]:
                        output = max(output, cnt +1)
                        cnt += 1
                        sig = 1 # next one should be larger
                    elif arr[i] == arr[i-1]:
                        output = max(output, 1)
                        cnt = 1
                        sig = 0 # next one can be anything
                else:
                    if sig == 0:
                        if arr[i] > arr[i-1]:
                            output = max(output, cnt+1)
                            cnt += 1
                            sig = -1 # next one should be smaller
                        elif arr[i] < arr[i-1]:
                            output = max(output, cnt +1)
                            cnt += 1
                            sig = 1 # next one should be larger
                        elif arr[i] == arr[i-1]:
                            output = max(output, 1)
                            cnt = 1
                            sig = 0 # next one can be anything

                    else:
                        if arr[i] > arr[i-1]:
                            if sig == 1:
                                output = max(output, cnt+1)
                                cnt += 1
                                sig = -1 # next one should be smaller
                            else:
                                sig = -1 # next one should be smaller
                                cnt = 2
                        elif arr[i] < arr[i-1]:
                            if sig == -1:
                                output = max(output, cnt+1)
                                cnt += 1
                                sig = 1 # next one should be larger
                            else:
                                sig = 1 # next one should be larger
                                cnt = 2

                        elif arr[i] == arr[i-1]:
                            cnt = 1
                            sig = 0 # next one can be anything

                # print(i, arr[i], sig, cnt)
            return output



# previous approach
# class Solution:
#     def maxTurbulenceSize(A: 'List[int]'):
#         if len(A) < 3:
#             return len(set(A))  # to remove the duplicates, like [1,1]
#         else:
#             l, r, output = 0, 2, 0
#             prev = A[1] - A[0]
#             curr = 0
#             while r < len(A):
#                 curr = A[r] - A[r - 1]
#                 if curr * prev > 0:
#                     output = max(output, r - l)
#                     l = r - 1
#                 elif curr * prev == 0:
#                     if prev == 0:
#                         if curr == 0:
#                             output = max(1, output)
#                             l = r
#                         else:
#                             output = max(output, r - l)
#                             l = r - 1
#                     else:
#                         output = max(r - l, output)
#                         l = r
#                 else:
#                     output = max(output, r - l + 1)
#                 # print(A[r], 'L:', l, "R:" , r,  "PREV:", prev, "CURR:", curr,  "Output:", output)
#                 prev = curr
#                 r += 1
#
#         return output
#
#
