def strWithout3a3b(A: 'int', B: 'int'):
    res = ""

    if A>=B:
        cnt_A = 0
        cnt_B = 0
        while cnt_A < A:
            if A - cnt_A >=2:
                res+="a"*2
                curr = 2
            else:
                res+="a"
                curr =1
            if cnt_B<B:
                res+= "b"
            cnt_A +=curr
            cnt_B +=1

        while cnt_B<B:
            res = res.replace("aa", "aba", 1)
            cnt_B+=1

    elif B > A:

        cnt_A = 0
        cnt_B = 0
        while cnt_B < B:
            if B - cnt_B >=2:
                res+="b"*2
                curr = 2
            else:
                res+="b"
                curr =1
            if cnt_A<A:
                res+= "a"
            cnt_B +=curr
            cnt_A +=1

        while cnt_A<A:
            res = res.replace("bb", "bab", 1)
            cnt_A+=1

    return res

print(strWithout3a3b(1,2))
print(strWithout3a3b(4,1))
print(strWithout3a3b(3,1))
print(strWithout3a3b(40,43))



