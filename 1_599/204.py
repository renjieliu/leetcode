class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        arr = [True] * n # from the question: LESS than a non-negative number, n.
        arr[0] = False
        arr[1] = False
        i = 2
        while i ** 2 < n:
            if arr[i] == True:
                curr = i*2
                while curr < n:
                    arr[curr] = False
                    curr += i
            i+=1
        return arr.count(True)



# previous approach
# class Solution:
#     def countPrimes(self, n: int) -> int: # sieve of Eratosthenes
#         if n <= 1 :
#             return 0
#         arr = [True for _ in range(n)]
#         arr[0] = False
#         arr[1] = False
#         i = 0
#         while i ** 2 < n:
#             if arr[i]:
#                 curr = i**2
#                 while curr < n:
#                     arr[curr] = False
#                     curr += i
#             i+=1
#         return arr.count(True)

# previous approach
# def countPrimes(n):
#     if n<3:
#         return 0
#     else:
#         prime = [1]*n
#         for i in range(2, int(n**0.5)+1 ):
#             prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
#
#     return sum(prime)-2 #this is for prime[0] and prime[1]
#
# print(countPrimes())

