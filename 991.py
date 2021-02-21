class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0
        elif X > Y:
            return X - Y
        else:
            arr = [Y]  # all the check point to reach to
            while Y > X:
                if Y % 2 == 1:  # since it can only substract, need +1 and // 2, in order to reach the checkpoing
                    Y = (Y + 1) // 2
                else:
                    Y = Y // 2
                arr.append(Y)

            cnt = 0
            arr = arr[::-1]
            # print(arr)
            cnt += X - arr[0]
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] * 2:
                    cnt += 1
                else:
                    cnt += 2  # (a*2)-1
            return cnt
