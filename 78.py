def combo(n, k):
    if len(n)<=k:
        return [n]

    else:
        output = []
        for i in range(len(n)):
            rest = n[:i]+n[i+1:]

            for x in combo(rest,k):
                output.append(x)

    result = []
    for i in output:
        if i not in result:
            result.append(i)

    return result


def subsets(nums: 'List[int]') :
    output = []
    for i in range(1, len(nums)+1):
        for x in combo(nums, i):
            output.append(x)
    output.append([])
    return output


print(subsets([1,2,3]))