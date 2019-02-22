def buddyStrings(A: 'str', B: 'str'):
    change = 0
    a_swap_1 = ""
    b_swap_1 = ""
    find = 0
    dups = 0
    c = []
    if len(A)!=len(B):
        return False

    else:
        for i in A:  # check if string has all unique character.
            if i in c:
                dups = 1
                break
            else:
                c.append(i)

        for i in range(0, len(A)):
            if A[i] !=  B[i] and a_swap_1 == "":
                change += 1
                a_swap_1 = A[i]
                b_swap_1 = B[i]
            elif A[i] != B[i] and a_swap_1 != "":
                change +=1
                if A[i] == b_swap_1 and B[i] ==a_swap_1:
                    find += 1
            if change > 2:
                return False

        if (A==B and len(A)>0 and dups  ==1 ) or (change == 2 and find==1):
            return True
        else:
            return False

print(buddyStrings("ab", "ba"))
print(buddyStrings("aa", "aa"))
print(buddyStrings("ab", "ab"))
print(buddyStrings("", "ab"))
print(buddyStrings("aaaaaaabc", "aaaaaaacb"))
print(buddyStrings("", ""))
print(buddyStrings("abab", "abab"))
