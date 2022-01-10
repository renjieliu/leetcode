class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #return bin(int(a, 2) + int(b,2))[2:] #one-liner solution
        a, b = list(a), list(b)
        output = ""
        carry = 0
        while a or b: #add corresponding bit, and carry over the digit if sum >= 2
            t = (int(a.pop()) if a else 0) + (int(b.pop()) if b else 0) + carry 
            carry = 1 if t > 1 else 0
            output = str(t%2) + output
        return ("1" if carry else "") + output


# previous approach             
# class Solution:
#     def addBinary(self, a: str, b: str) -> str: 
#         pad = len(a) - len(b)
#         if pad < 0: a ='0'*abs(pad) + a
#         else:b = '0'*abs(pad) + b
#         carry = 0
#         output = ''
#         for i in range(len(b)-1, -1, -1):
#             curr = int(a[i]) + int(b[i]) + carry
#             #print(curr,int(a[i]) ,  int(b[i]) )
#             if curr >= 2:
#                 carry = 1
#                 output = str(curr%2) + output
#             else:
#                 carry = 0
#                 output = str(curr) + output
        
#         return output if carry == 0 else '1' + output
        

# previous approach
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         pad = len(a) - len(b)
#         if pad < 0:
#             a = '0' * abs(pad) + a
#         else:
#             b = '0' * abs(pad) + b
#         carry = 0
#         output = ''
#         for i in range(len(b) - 1, -1, -1):
#             curr = int(a[i]) + int(b[i]) + carry
#             # print(curr,int(a[i]) ,  int(b[i]) )
#             if curr >= 2:
#                 carry = 1
#                 output = str(curr % 2) + output
#             else:
#                 carry = 0
#                 output = str(curr) + output

#         return output if carry == 0 else '1' + output


