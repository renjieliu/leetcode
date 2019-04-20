def validateStackSequences(pushed: 'List[int]', popped: 'List[int]'):
    if len(pushed) != len(popped):
        return False
    if len(pushed) == 0 and len(popped) ==0:
        return True
    
    if len(pushed)==1 and pushed[0] ==popped[0]:
        return True

    curr = [pushed[0]]
    pushed.pop(0)
    stk = []
    while pushed:
        if len(curr) ==0:
            curr.append(pushed[0])
            pushed.pop(0)
        elif curr[-1] != popped[0] or len(curr) ==0:
            curr.append(pushed[0])
            pushed.pop(0)
        else:
            curr.pop(-1)
            popped.pop(0)

    while curr:
        stk.append(curr.pop()) #what's left in the curr, compare with the rest of the popped.

    return stk == popped

print(validateStackSequences( pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print(validateStackSequences( pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print(validateStackSequences( pushed = [], popped = []))
print(validateStackSequences( pushed = [1], popped = [2]))
print(validateStackSequences( pushed = [1], popped = [1]))
print(validateStackSequences( pushed = [1,0], popped = [1,0]))


