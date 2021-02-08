class Solution:
    def reverseBits(self, n: int) -> int:
        b = str(bin(n)).replace('0b','')
        b_32 = '0'* (32-len(b)) + b
        return int(b_32[::-1],2)


# previous approach
# def reverseBits( n):
#     return int(  (str("0")*(32-len(str(bin(n)).replace("0b", "")) ) +   str(bin(n)).replace("0b", "") )[::-1],2)

#print(reverseBits(43261596))