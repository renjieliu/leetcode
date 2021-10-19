class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pad = len(a) - len(b)
        if pad < 0:
            a = '0' * abs(pad) + a
        else:
            b = '0' * abs(pad) + b
        carry = 0
        output = ''
        for i in range(len(b) - 1, -1, -1):
            curr = int(a[i]) + int(b[i]) + carry
            # print(curr,int(a[i]) ,  int(b[i]) )
            if curr >= 2:
                carry = 1
                output = str(curr % 2) + output
            else:
                carry = 0
                output = str(curr) + output

        return output if carry == 0 else '1' + output
