class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        carry = 1 if digits[-1] == 9 else 0
        output = [0 if carry == 1 else (digits[-1] + 1)]
        for d in digits[:-1][::-1]:
            if carry == 1:
                if d == 9:
                    output.append(0)
                else:
                    output.append(d + carry)
                    carry = 0
            else:
                output.append(d)
        if carry == 1:
            output.append(1)
        return output[::-1]

# Previous approach
# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     temp = ""
#     output = list()
#     for i in digits:
#         temp+=str(i)
#
#     for i in str(int(temp) + 1):
#         output.append(int(i))
#
#     return output
#
#
# print(plusOne([4,3,2,1]))
#
#
