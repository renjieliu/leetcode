class Solution:
    def reorderedPowerOf2(self, n: int) -> bool: # O( logN | logN )
        arr= [0] * 10 
        while n > 0: #get all the digit occurrence of n, logN complexity
            arr[n%10]+=1 
            n //= 10
        
        def isSame(arr, n): #compare if the converted n is the same as arr
            t = [0] * 10 
            while n > 0:
                t[n%10]+=1 
                n //= 10
            
            return arr == t
    
        return any(isSame(arr, 2**_) for _ in range(30)) # as long as any of the 2**x matches with the arr
    
    

# previous solution

# class Solution:
#     def reorderedPowerOf2(self, N: int) -> bool:
#         lkp = []
#         power = 0
#         while 2 ** power < 10 ** 9:
#             lkp.append(sorted(list(str(2 ** power))))
#             power += 1
#         return sorted(list(str(N))) in lkp



# previous approach
# def signature(n):
#     map = {}
#     sig = ""
#     for i in range(0, 10):
#         map[str(i)] = 0
#
#     for i in str(n):
#         map[i] += 1
#
#     for k, v in map.items():
#         sig += str(k) + "-" + str(v) + ','
#
#     return sig
#
#
# def reorderedPowerOf2(N: int):
#     #to find the signature of each number that falls between the range, and compare with the input
#     l = len(str(N))
#     curr = 0
#     output = []
#     start = 10**(l - 1)
#     end = round(N, -l + 1) * 10 - 1
#     while 2 ** curr < end:
#         if 2 ** curr >= start:
#             output.append(signature(2 ** curr))
#         curr += 1
#
#     if signature(N) in output:
#         return True
#     else:
#         return False
#
#
# print(reorderedPowerOf2(1))
# print(reorderedPowerOf2(10))
# print(reorderedPowerOf2(16))
# print(reorderedPowerOf2(24))
# print(reorderedPowerOf2(46))
# print(reorderedPowerOf2(1077341824))
