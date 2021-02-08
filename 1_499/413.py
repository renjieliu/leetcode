def numberOfArithmeticSlices(A: "List[int]"):
    base = 0
    length = 1
    output = 0

    if len(A)<3 :
        return 0

    else:
        base = A[1] - A[0]
        for i in range(len(A)-1):
            if A[i+1] - A[i] ==base:
                length +=1
            else:
                if length < 3:
                    length = 2
                    base = A[i+1] - A[i]
                else:
                    end = length -2 #  sum(1..X) = (x+1)*x/2
                    output+= (1+end) * end//2

                    length = 2
                    base = A[i+1] - A[i]

        if length >=3:
            end = length -2 #  sum(1..X) = (x+1)*x/2
            output+= (1+end) * end//2

        return output

print( numberOfArithmeticSlices([1, 2, 3, 4,5,6,6,6,6,6,6,6,6,6,6,6,6,-1,12,12,12]))

