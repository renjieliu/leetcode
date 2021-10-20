def totalFruit(tree: 'List[int]'):
    if len(tree)<=2:
        return len(tree)
    i, last_changed_pos, j = 0, 0, 1

    output = -float('inf')
    met= {tree[0]:1}
    while j < len(tree):
        curr = tree[j]
        if curr == tree[j-1]:
            met[curr] += 1
        else: # if different from previous
            if curr not in met:  # if new
                met[curr] = 0
            met[curr] += 1
            if len(met.keys()) ==2:
                last_changed_pos = j
            elif len(met.keys()) == 3:
                #print('---', last_changed_pos-1)
                del met[tree[last_changed_pos-1]]
                output = max(j - i, output)
                i = last_changed_pos
                last_changed_pos = j


        j+=1
        #print(j, last_changed_pos, met, output)
    return max(j-i, output)


print(totalFruit([1,2,1])) #3
print(totalFruit([0,1,2,2])) #3
print(totalFruit([1,2,3,2,2])) #4
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4])) #5
print(totalFruit([3,3,3,1,2,1,1,2,3,3,43,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1,3,3,3,1,2,1,1])) #5