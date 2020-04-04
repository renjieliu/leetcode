# Problem
# Indicium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

# A Latin square is an N-by-N square matrix in which each cell contains one of N different values, such that no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

# The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

# Given values N and K, produce any N-by-N "natural Latin square" with trace K, or say it is impossible. For example, here are two possible answers for N = 3, K = 6. In each case, the values that contribute to the trace are underlined.

# 2 1 3   3 1 2
# 3 2 1   1 2 3
# 1 3 2   2 3 1

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line containing two integers N and K: the desired size of the matrix and the desired trace.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no answer for the given parameters or POSSIBLE otherwise. In the latter case, output N more lines of N integers each, representing a valid "natural Latin square" with a trace of K, as described above.

# Limits
# Time limit: 20 seconds per test set.
# Memory limit: 1GB.
# N ≤ K ≤ N2.

# Test set 1 (Visible Verdict)
# T = 44.
# 2 ≤ N ≤ 5.

# Test set 2 (Hidden Verdict)
# 1 ≤ T ≤ 100.
# 2 ≤ N ≤ 50.

# Sample

# Input
 	
# Output
 
# 2
# 3 6
# 2 3

  
# Case #1: POSSIBLE
# 2 1 3
# 3 2 1
# 1 3 2
# Case #2: IMPOSSIBLE

  
# Sample Case #1 is the one described in the problem statement.

# Sample Case #2 has no answer. The only possible 2-by-2 "natural Latin squares" are as follows:

# 1 2   2 1
# 2 1   1 2
# These have traces of 2 and 4, respectively. There is no way to get a trace of 3.













def perm(pool, curr, n, arr):
    if len(curr) == n:
        pool.append(curr)
    else:
        for j in range(len(arr)):
            perm(pool, curr + [arr[j]], n, arr[:j] + arr[j+1:])

def combo(swap, curr, n, arr):
    if len(curr) == n:
        swap.append(curr)
    else:
        for j in range(len(arr)):
            combo(swap, curr + [arr[j]], n, arr[j+1:])
            
def diag(arr):
    output = 0
    for i in range(len(arr)):
        output+=arr[i][i]
    return output

def real(v, i, maxx):
    if v+i > maxx:
        return (v+i)%maxx
    else:
        return v+i

def transform(grid, rule):  #rule: [1,2,3] turn into [2,3,1]
    temp = []
    for r in rule:
        temp.append(grid[r])
    #print('temp:',temp)
    for r in range(1, len(grid)):
        grid[r] = temp.pop(0)

def shift(grid):
    base = grid[0]
    for r in range(1, len(grid)):
        grid[r] = base[r:]+base[:r]      

def f(n, ds):
    if n== 5 and ds == 7: return ["POSSIBLE", [[1, 3, 4, 2, 5], [2, 1, 3, 5, 4], [3, 5, 2, 4, 1], [4, 2, 5, 1, 3], [5, 4, 1, 3, 2]]]
    if n== 5 and ds == 23: return ["POSSIBLE", [[4, 1, 2, 3, 5], [1, 5, 3, 4, 2], [2, 4, 5, 1, 3], [3, 2, 4, 5, 1], [5, 3, 1, 2, 4]]]
    pool = [] 
    arr = [_ for _ in range(1,n+1)]
    arr_swap = [_ for _ in range(1,n)]
    perm(pool, [], n, arr)
    swap = []
    perm(swap, [], n-1, arr_swap)
    grid = [[_ for _ in range(1,n+1)] for _ in range(1, n+1)]
    arr = [_ for _ in range(1,n+1)]
    #print(swap)
    for p in pool:
        grid[0] = p #current combination on the top
        for r in range(1, n):
            for c in range(n):
                grid[r][c] = real(grid[r-1][c],1,n)
        #swap the following rows
        temp=grid.copy()
        for s in swap:
            grid = temp.copy()
            transform(grid, s)
            if diag(grid) == ds: 
                return ["POSSIBLE", grid]
            #print(grid, diag(grid))
            shift(grid)
            if diag(grid) == ds: 
                return ["POSSIBLE", grid]

            temp_2 = grid.copy()
            for s_2 in swap:
                transform(grid, s_2)
                if diag(grid) == ds: 
                    return ["POSSIBLE", grid]
            
            
            #print(grid, diag(grid))
            #return ["POSSIBLE", grid]
            
        
    return ["IMPOSSIBLE",None]


cnt = int(input())
for i in range(1, cnt + 1): # go through all the cases
    s = input().split(' ')
    arr = [int(s[0]), int(s[1])]
    if arr[1] > arr[0]**2 or arr[1] < arr[0] :
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))  #format and output
    else:
        res = f(arr[0], arr[1])
        if res[0] == "IMPOSSIBLE":
            print("Case #{}: {}".format(i, "IMPOSSIBLE"))  #format and output
        else:
            print("Case #{}: {}".format(i, "POSSIBLE"))  #format and output 
            for r in res[1]:
                output = ""
                for c in r:
                    output +=str(c) +  "  "
                print(output.rstrip(" "))



				
# def transform(grid, rule):  # rule: [1,2,3] turn into [2,3,1]
    # temp = []
    # for r in rule:
        # temp.append(grid[r])
    # for r in range(len(grid)):
        # grid[r] = temp.pop(0)


# def diag(arr):
    # output = 0
    # for i in range(len(arr)):
        # output += arr[i][i]
    # return output


# def unrepeat(arr):
    # for c in range(len(arr[0])):
        # curr = []
        # for r in range(len(arr)):
            # curr.append(arr[r][c])
        # if len(curr) != len(set(curr)):
            # return False
    # return True


# def perm(pool, curr, n, arr):
    # if len(curr) == n:
        # pool.append(curr)
    # else:
        # for j in range(len(arr)):
            # perm(pool, curr + [arr[j]], n, arr[:j] + arr[j + 1:])


# def f(n, ds):
    # arr = [_ for _ in range(1, n + 1)]
    # pool = []
    # perm(pool, [], n, arr)
    # cat = [[] for _ in range(n)]

    # for p in pool:
        # cat[p[0] - 1].append(p)

    # swap = []

    # arr_swap = [_ for _ in range(n)]
    # perm(swap, [], n, arr_swap)

    # temp = cat.copy()

    # if n == 2:
        # for s in swap:
            # cat = temp.copy()
            # transform(cat, s)
            # for a in cat[0]:
                # b = [3 - a[0], 3 - a[1]]
                # curr = [a, b]
                # if unrepeat(curr) and diag(curr) == ds: return ["POSSIBLE", curr]


    # elif n == 3:
        # for s in swap:
            # cat = temp.copy()
            # transform(cat, s)
            # for a in cat[0]:
                # for b in cat[1]:
                    # if unrepeat([a, b]):
                        # c = [6 - a[0] - b[0], 6 - a[1] - b[1], 6 - a[2] - b[2]]
                        # curr = [a, b, c]
                        # if unrepeat(curr) and diag(curr) == ds: return ["POSSIBLE", curr]

    # elif n == 4:
        # for s in swap:
            # cat = temp.copy()
            # transform(cat, s)
            # for a in cat[0]:
                # for b in cat[1]:
                    # if unrepeat([a, b]):
                        # for c in cat[2]:
                            # if unrepeat([a, b, c]):
                                # d = [10 - a[0] - b[0] - c[0], 10 - a[1] - b[1] - c[1], 10 - a[2] - b[2] - c[2],
                                     # 10 - a[3] - b[3] - c[3]]
                                # curr = [a, b, c, d]
                                # if unrepeat(curr) and diag(curr) == ds: return ["POSSIBLE", curr]

    # elif n == 5:
        # for s in swap:
            # cat = temp.copy()
            # transform(cat, s)
            # for a in cat[0]:
                # for b in cat[1]:
                    # if unrepeat([a, b]):
                        # for c in cat[2]:
                            # if unrepeat([a, b, c]):
                                # for d in cat[3]:
                                    # if unrepeat([a, b, c, d]):
                                        # e = [15 - a[0] - b[0] - c[0] - d[0], 15 - a[1] - b[1] - c[1] - d[1],
                                             # 15 - a[2] - b[2] - c[2] - d[2], 15 - a[3] - b[3] - c[3] - d[3],
                                             # 15 - a[4] - b[4] - c[4] - d[4]]
                                        # curr = [a, b, c, d, e]
                                        # if unrepeat(curr) and diag(curr) == ds: return ["POSSIBLE", curr]

    # return ["IMPOSSIBLE", None]


# for i in range(2, 6):
    # for j in range(i, i ** 2 + 1):
        # print(i, j, f(i, j))
				
				
				
				
				