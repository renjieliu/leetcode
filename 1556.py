class Solution:
    def thousandSeparator(self, n: int) -> str:
        output = ""
        cnt = 0
        for c in str(n)[::-1]:
            output = c + output
            cnt += 1
            if cnt == 3:
                output = "." + output
                cnt = 0
        return output[1:] if output[0] == '.' else output