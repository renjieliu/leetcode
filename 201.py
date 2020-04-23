class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m * n == 0:
            return 0
        else:
            m_bin = str(bin(m)).replace('0b', '')
            n_bin = str(bin(n)).replace('0b', '')
            output = ""
            for i in range(len(m_bin)):
                if m_bin[-(i + 1)] == "0" or n_bin[-(i + 1)] == "0":
                    output = "0" + output
                else:
                    if n - m >= 2 ** i:  # as long as there's 0 (power of 2) in between, the result will be 0.
                        output = "0" + output
                    else:
                        output = "1" + output
            return int(output, 2)
