def reverseBits( n):
    return int(  (str("0")*(32-len(str(bin(n)).replace("0b", "")) ) +   str(bin(n)).replace("0b", "") )[::-1],2)

print(reverseBits(43261596))