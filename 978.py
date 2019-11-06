class Solution:
    def maxTurbulenceSize(A: 'List[int]'):
        if len(A) < 3:
            return len(set(A))  # to remove the duplicates, like [1,1]
        else:
            l, r, output = 0, 2, 0
            prev = A[1] - A[0]
            curr = 0
            while r < len(A):
                curr = A[r] - A[r - 1]
                if curr * prev > 0:
                    output = max(output, r - l)
                    l = r - 1
                elif curr * prev == 0:
                    if prev == 0:
                        if curr == 0:
                            output = max(1, output)
                            l = r
                        else:
                            output = max(output, r - l)
                            l = r - 1
                    else:
                        output = max(r - l, output)
                        l = r
                else:
                    output = max(output, r - l + 1)
                # print(A[r], 'L:', l, "R:" , r,  "PREV:", prev, "CURR:", curr,  "Output:", output)
                prev = curr
                r += 1

        return output

