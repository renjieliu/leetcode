class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        x = 0
        while 3**x <=n:
            arr.append(3**x)
            x+=1
        def combo(length, n, arr, currLength, currSum):
            if currSum == n:
                return True
            elif currSum != n and currLength == length:
                return False
            else:
                for i in range(len(arr)):
                    res = combo(length, n, arr[i+1:], currLength+1, currSum+arr[i])
                    if res:
                        return True

        for i in range(1, len(arr)+1): #try different length to find a combination
            res = combo(i, n, arr, 0, 0 )
            if res:
                return True
        return False