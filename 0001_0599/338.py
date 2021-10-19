class Solution:
    def countBits(self, num: int) -> 'List[int]':
        output = []
        for i in range(num + 1):
            output.append(bin(i).count('1'))
        return output

#OLD Solution
# def countBits(num):
#     """
#     :type num: int
#     :rtype: List[int]
#     """
#     output = list()
#     for i in range(0, num+1):
#         bin_1 = str(bin(i)).replace("0b","")
#         bin_t = str(bin(i)).replace("0b","").replace("1", "")
#
#         output.append(len(bin_1) - len(bin_t))
#
#     return output
# print(countBits(5))
