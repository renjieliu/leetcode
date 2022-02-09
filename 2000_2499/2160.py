class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num > 0 : # take digits one by one
            arr.append(num%10)
            num //= 10
        arr.sort()  #[a, b, c, d]
        return arr[0]*10 + arr[-2] + arr[1]*10 + arr[-1] # greedy. a*10+c + b*10+d



