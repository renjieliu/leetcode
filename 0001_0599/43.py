class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        output = 0
        for j in range(len(num2)-1, -1, -1): #from right to left. 
            local = 0 
            carry = 0
            for i in range(len(num1)-1, -1, -1):
                t = int(num2[j]) * int(num1[i]) + carry
                carry = t//10
                power_i = len(num1) - i - 1 #add t to the "front" of the local
                local += (t%10)*(10**power_i)
            
            local += carry * (10**len(num1)) # add the carry to the "front" of the local
            power_j = len(num2)-j-1
            output += local * (10**power_j)
        return str(output)




# previous approach
# class Solution:
#     def singleDigitM (self, str1, c1):
#         reminder = 0
#         add = 0
#         output = ""
#         for i in str1[::-1]:
#             reminder = (int(i) * int(c1) + add) % 10
#             add = (int(i) * int(c1) + add) //10
#             output = str(reminder) + output
#         if add==0:
#             return output
#         else:
#             return str(add) + output


#     def multiply(self, num1: str, num2: str) -> str:
#         short = num1 if len(num1)<=len(num2) else num2
#         long = num2 if short == num1 else num1
#         pos = 0
#         output = 0
#         for i in short[::-1]:
#             output += int(self.singleDigitM(long, i)) * (10**pos)
#             pos+=1
#         return str(output)

