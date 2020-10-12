class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2 or len(B) < 2 or sorted(list(A)) != sorted(list(B)):  # character unmatched
            return False
        else:
            cnt = 0
            for i in range(len(A)):
                cnt += 1 if A[i] != B[i] else 0
            if cnt == 2:
                return True
            elif cnt > 2:
                return False
            elif cnt == 0:
                if len(set(A)) < len(A):  # the character appears more than once in A, swap it to make it same
                    return True
                else:
                    return False

