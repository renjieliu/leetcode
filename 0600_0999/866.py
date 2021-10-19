def isPrime(n):
    if n < 1:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0

    return 1


def primePalindrome( N: int) -> int:
    if N < 10:
        list = [ 2, 3, 5, 7]
        for i in list:
            if i > N:
                return i
        return 11

    for j in range(1, 8):
        for i in range(10 ** (j - 1), 10 ** j):
            s = str(i)
            s1 = s + s[::-1]
            if int(s1) >= N and isPrime(int(s1)):
                return int(s1)

        for i in range(10 ** (j - 1), 10 ** j):
            s = str(i)
            s1 = s + s[:-1][::-1]
            if int(s1) >= N and isPrime(int(s1)):
                return int(s1)


print(primePalindrome(999))