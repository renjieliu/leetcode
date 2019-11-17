class Solution:
    def encode(self, num: int) -> str:  # find the diff b/w the number and 2**i - 1, replace the 2**i - 1 to 000..and add the diff
        if num == 0:
            return ""
        elif num == 1:
            return "0"
        elif num == 2:
            return "1"
        else:
            i = 0
            while True:
                if 2 ** i <= num:  # to find how many digits it should be
                    i += 1
                else:
                    break
            if num == 2 ** i - 1:
                return "0" * i
            else:
                start = 2 ** (i - 1) - 1
                start_bin = list(str(bin(start)).replace("0b", "").replace("1", "0"))
                diff = num - start
                diff_bin = list(str(bin(diff)).replace("0b", ""))
                output = ""
                while diff_bin and start_bin:
                    output = str(int(diff_bin.pop()) + int(start_bin.pop())) + output

                output = ''.join(start_bin) + output

            return output
