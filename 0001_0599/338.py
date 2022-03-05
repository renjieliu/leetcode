class Solution:
    def countBits(self, n: int) -> 'List[int]':
        def count(v): #count 1 bit of v
            cnt = 0
            while v>0:
                cnt += v % 2 #if current is odd or even
                v >>= 1
            return cnt
        
        arr = []
        for i in range(n+1):
            arr.append(count(i))
        return arr
    


# previous approach

# class Solution:
#     def countBits(self, num: int) -> 'List[int]':
#         output = []
#         for i in range(num + 1):
#             output.append(bin(i).count('1'))
#         return output

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
