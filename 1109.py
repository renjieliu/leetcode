def corpFlightBookings(bookings: 'List[List[int]]', n: int):
    #running sum
    output = [0] * (n+1)
    for i,j,k in bookings:
        output[i-1] += k
        output[j] -=k

    for i in range(1, n+1):
        output[i] += output[i-1]

    return output[:-1]


print(corpFlightBookings(bookings = [[1,2,10],[3,4,30]], n = 5))