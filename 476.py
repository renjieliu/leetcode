class Solution:
    def findComplement(self, num: int) -> int:
        t = bin(num).replace("0b", "")
        return int ("".join(map(lambda x: "0" if x == "1" else "1", t)),base=2)


##OLD SOLUTION:

# def findComplement(num):
#     """
#     :type num: int
#     :rtype: int
#     """
#     output = ""
#     b = str(bin(num)).replace("0b", "")
#     #print(b)
#     for i in range(0, len(b)):
#         output+= str(0) if b[i] == "1" else str(1)
#     #print(output)
#     return int(output, 2)
#
# print(findComplement(0))
#



