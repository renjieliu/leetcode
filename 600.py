class Solution:
    def findIntegers(self, num):
        s = bin(num + 1)[2:]
        n = len(s)
        dp = [1, 2] + [0] * (n - 2)
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        flag, ans = 0, 0
        for i in range(n):
            if s[i] == "0": continue
            if flag == 1: break
            if i > 0 and s[i - 1] == "1": flag = 1
            ans += dp[-i - 1]

        return ans

# Let us consider n = 10100101101, then what numbers we can choose:

# Group 0XXXXXXXXXX,
# Group 100XXXXXXXX,
# Group 101000XXXXX,
# Group 10100100XXX,
# Group 101001010XX,
# where X can be any digit: 0 or 1. So, we need to found number of sequences with 0 and 1 without consecutive ones, and it is Fibonacci numbers. So, we use binary representation of number and traverse it from the start and check if we have two consecutive ones. If we have, we break, if not, we add corresponding Fibonacci number. Let us consider these groups and check how many options we have for each of them - start with last one, it have less options.

# Group 5. 101001010XX, where instead of XX we can put 00, 01, 11, that is F[2] = 3 cases.
# Group 4. 10100100XXX, where instead of XXX we can put 000, 001, 010, 100, 101, that is F[3] = 5 cases.
# Group 3. 101000XXXXX, where instead of XXXXX we can put 00000, 00001, 00010, 00100, 00101, 01000, 01001, 01010, 10000, 10001, 10010, 10100, 10101, that is F[5] = 13 cases.
# Group 2, 100XXXXXXXX where instead of XXXXXXXX we can put F[8] = 55 cases
# Group 1, 0XXXXXXXXXX, where instead of XXXXXXXXXX we can put F[10] = 144 cases.

# Why we have Fibonacci number of ways to create number without two consecuteve ones? You can check here https://math.stackexchange.com/questions/1280545/counting-binary-strings-of-length-n-with-no-two-adjacent-1s, but intuition is simple: if we have A_n number of n-digit binary numbers, than last element can be either 1, then we have A_{n-2} options or it can be 0, then we have A_{n-1} options.

# In total we have F[2] + F[3] + F[5] + F[8] + F[10] cases, which we return as answer.

# Complexity
# Time complexity is O(32), because we use binary representation of number. If we have unbounded n, complexity is O(m) = O(log n), where m is number of bits in this number (and if we need to give answer modulo some N to find Fibonacci numbers fast).



