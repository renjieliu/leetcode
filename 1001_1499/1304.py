class Solution:
    def sumZero(self, n: int) -> 'List[int]':
        output = []
        cnt = 0  # add a and -a to the output.
        if n % 2 == 0:
            while cnt < n:
                output.append(cnt + 1)
                output.append((cnt + 1) * -1)
                cnt += 2
            return output
        else:
            while cnt < n - 1:
                output.append(cnt + 1)
                output.append((cnt + 1) * -1)
                cnt += 2
            return output + [0]

