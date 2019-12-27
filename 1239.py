class Solution:
    def maxLength(self, arr: 'List[str]') -> int:
        def findMax(curr, pos, arr):
            if pos == len(arr):
                return len(curr)
            else:
                A, B, C, found = 0, 0, 0, 0
                for c in arr[pos]:
                    if c in curr:
                        found = 1
                        break
                if len(arr[pos]) != len(set(arr[pos])): found = 1  # dups found witin the word itself.

                if found == 0:
                    take = curr + arr[pos]  # choose current word
                    A = findMax(take, pos + 1, arr)
                    B = findMax(curr, pos + 1, arr)  # skip current pos
                else:
                    C = findMax(curr, pos + 1, arr)  # skip current pos

                return max(A, B, C)

        i = 0
        output = 0
        while i < len(arr):
            w = arr[i]
            if len(w) != len(set(w)):
                i += 1
            else:
                output = max(output, findMax(w, i + 1, arr))
                i += 1
        return output