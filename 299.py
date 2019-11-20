class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        dict_A = {}
        dict_B = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in dict_A:
                    dict_A[secret[i]] = 0
                dict_A[secret[i]] += 1

                if guess[i] not in dict_B:
                    dict_B[guess[i]] = 0
                dict_B[guess[i]] += 1

        for k in dict_A.keys():
            if k in dict_B:
                B += min(dict_A[k], dict_B[k])

        return str(A) + "A" + str(B) + "B"


