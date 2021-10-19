class Solution:
    def minDominoRotations(self, A: 'List[int]', B: 'List[int]') -> int:
        curr = A[0]
        swap_A_1 = 0
        for i in range(len(A)):
            if A[i] != curr:
                if B[i] != curr:
                    swap_A_1 = float('inf')
                    break
                else:
                    swap_A_1 += 1

        curr = B[0]
        swap_A_2 = 0
        for i in range(len(A)):
            if A[i] != curr:
                if B[i] != curr:
                    swap_A_2 = float('inf')
                    break
                else:
                    swap_A_2 += 1
        swap_A = min(swap_A_1, swap_A_2)

        curr = B[0]
        swap_B_1 = 0
        for i in range(len(B)):
            if B[i] != curr:
                if A[i] != curr:
                    swap_B_1 = float('inf')
                    break
                else:
                    swap_B_1 += 1
        curr = A[0]
        swap_B_2 = 0
        for i in range(len(B)):
            if B[i] != curr:
                if A[i] != curr:
                    swap_B_2 = float('inf')
                    break
                else:
                    swap_B_2 += 1
        swap_B = min(swap_B_1, swap_B_2)

        return -1 if min(swap_A, swap_B) == float('inf') else min(swap_A, swap_B)















