def lexicalOrder(n: int):
    t = [str(_) for _ in range(1, n + 1)]
    output = []
    t.sort()
    for i in t:
        output.append(int(i))
    return output


print(lexicalOrder(150))