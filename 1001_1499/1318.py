class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = str(bin(a)).replace('0b', '')
        bin_b = str(bin(b)).replace('0b', '')
        target = str(bin(c)).replace('0b','')

        bin_a = '0'* (32 - len(bin_a)) + bin_a
        bin_b = '0'* (32 - len(bin_b)) + bin_b
        target = '0'* (32 - len(target)) + target
        #print(bin_a, bin_b, target)
        output = 0
        for i in range(len(target)):
            if target[i] == '1':
                if bin_a[i] == bin_b[i] == '0' :
                    output += 1
            elif target[i] == '0':
                if bin_a[i] != bin_b[i]:
                    output +=1                
                elif bin_a[i] == bin_b[i] == '1':
                    output +=2
        return output

