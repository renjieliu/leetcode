def coinChange(coins: 'List[int]', amount: int):
    if amount == 0:
        return 0
    elif amount < min(coins):
        return -1
    arr = [float('inf') for _ in range(amount + 1)]
    arr[0] = 0
    for curr in range(len(arr)):  # this is to populate the array.
        for c in coins:
            if c <= curr and arr[curr - c] != float('inf'):  # the place has been calculated before
                arr[curr] = min(arr[curr - c] + 1, arr[curr])

    if arr[amount] == float('inf'):
        return -1
    else:
        return arr[amount]


print(coinChange([1, 2, 5], 11))