class Solution:
    def similarRGB(self, color: str) -> str: #O( N ** 3 | 1 )
        dist = lambda a, b: -(int(a[1:3], 16) - int(b[1:3], 16))**2 - (int(a[3:5], 16) - int(b[3:5], 16)) **2 - (int(a[5:7], 16) - int(b[5:7], 16)) ** 2
        curr = -float('inf')
        s = '0123456789abcdef' # try all the possible combination and find the one with highest dist.
        cnt = 0
        for a in s:
            for b in s:
                for c in s:
                    d = dist(color, '#' + a*2+b*2+c*2)
                    if d > curr:
                        curr = d
                        output = '#' + a*2+b*2+c*2
        return output
    
 

# previous solution

# class Solution:
#     def similarRGB(self, color: str) -> str:
#         similarity  = -float('inf')
#         output = ""
#         r = int(color[1:3],16)
#         g = int(color[3:5],16)
#         b = int(color[5:],16)
#         for i in range(16):
#             for j in range(16):
#                 for k in range(16):
#                     x = (str(hex(i))*2).replace("0x", "")
#                     y = (str(hex(j))*2).replace("0x", "")
#                     z = (str(hex(k))*2).replace("0x", "")
#                     curr = -(int(x,16)-r)**2 - (int(y,16)-g)**2 - (int(z,16) -b)**2
#                     if curr >= similarity:
#                         similarity = curr
#                         output = ("#" + x + y + z)
#         return output


