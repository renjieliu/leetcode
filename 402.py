class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        else:
            if k == 0:
                return num
            else:
                cnt = 0
                while cnt < k:
                    found = 0
                    for i in range(len(num) - 1):
                        if num[i] > num[
                            i + 1]:  # to find the first decending position, if it cannot be found, then dump the last element if the string
                            found = 1
                            cnt += 1
                            num = num[:i] + num[i + 1:]
                            break

                    if found == 0:
                        num = num[:-1]  # take out the last element
                        cnt += 1

            return '0' if num.lstrip('0') == "" else num.lstrip('0')
