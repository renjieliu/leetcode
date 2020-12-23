class Solution:
    def nextGreaterElement(self, n: int) -> int:
        limit = 2 ** 31
        t = str(n)[::-1] #reverse, and check if can find a number that is smaller than the previous met, if so, swap
        if len(t) == 1:
            return -1
        else:
            prev = [t[0]]
            for i in range(1, len(t)):
                curr = t[i]
                if curr < prev[-1]:  # smaller than the max, it can be swapped
                    for j in range(len(prev)):
                        if prev[j] > curr:
                            prev[j], curr = curr, prev[j]  # swap the curr and prev[j]
                            break
                    candidate = "".join(sorted(prev, reverse=True)) + curr
                    rest = t[i + 1:]
                    output = (candidate + rest)[::-1]
                    return int(output) if int(output) < limit else -1
                else:
                    prev.append(curr)
                    prev.sort()
            return -1

# previous approach
# def nextGreaterElement(n: int) -> int:
#     if len(str(n)) == 1:
#         return -1
#
#     tmp = str(n)
#     found =0
#
#     for i in range(len(tmp)-1, 0, -1):
#         if tmp[i] > tmp[i-1]:
#             root = tmp[:i-1] + tmp[i]
#             rest = "".join(sorted(tmp[i-1]+ tmp[i+1:]))
#             found = 1
#
#     return root+rest if found == 1 else -1
#
#
# print(nextGreaterElement(12))
# print(nextGreaterElement(21))
# print(nextGreaterElement(987564321))
# print(nextGreaterElement(230241)) # 230421 # 230412
# print(nextGreaterElement(34123451))
# print(nextGreaterElement(33333334))
# print(nextGreaterElement(9999999989))
# print(nextGreaterElement(12443322)) #13222344
#
#


