class Solution:
    def constructArray(self, n: int, k: int) -> 'List[int]':
        arr = [_ for _ in range(1, n+1)]
        if k == 1:
            return arr

        output = [arr.pop(0)]
        cnt = 0
        while arr: #pick the first and last item in term. Finally, put the rest (abs diff = 1) to the end
            if cnt %2 == 0:
                output.append(arr.pop())
            else:
                output.append(arr.pop(0))
            cnt += 1
            if cnt >= k-1:
                break
            # print(output)
        if arr == []:
            return output
        else:
            if abs(arr[0] - output[-1]) != 1:
                return output+arr[::-1]
            else:
                return output+arr


