def invalidTransactions( transactions: 'List[str]'):
    def name(s):
        return s.split(",")[0]

    def time(s):
        return int(s.split(",")[1])

    def amount(s):
        return int(s.split(",")[2])

    def place(s):
        return s.split(",")[3]

    check = [-1]*len(transactions)
    transactions.sort()
    output = []
    for i in range(len(transactions)):
        curr_name = name(transactions[i])
        curr_time = time(transactions[i])
        time_1 =  curr_time - 60
        time_2 = curr_time+60
        curr_amount= amount(transactions[i])
        curr_place = place(transactions[i])
        if curr_amount >=1000:
            check[i] = 1
        for j in range(i+1, len(transactions)):
            if name(transactions[j]) == curr_name:
                if time_1 <= time(transactions[j]) <= time_2 and place(transactions[j])!= curr_place:
                    check[i] = 1
                    check[j] = 1
            else:
                break



    for i in range(len(check)):
        if check[i]==1:
            output.append(transactions[i])


    return output

print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv", "alice,50,1200,beijing"]))
print(invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))
print(invalidTransactions(transactions = ["xnova,261,1949,chicago","bob,206,1284,chicago","xnova,420,996,bangkok","chalicefy,704,1269,chicago","iris,124,329,bangkok","xnova,791,700,amsterdam","chalicefy,572,697,budapest","chalicefy,231,310,chicago","chalicefy,763,857,chicago","maybe,837,198,amsterdam","lee,99,940,bangkok","bob,132,1219,barcelona","lee,69,857,barcelona","lee,607,275,budapest","chalicefy,709,1171,amsterdam"]))
print(invalidTransactions(transactions = ["chalicefy,639,1283,beijing","maybe,324,192,frankfurt","bob,627,974,amsterdam","alex,962,125,chicago","iris,849,36,beijing","chalicefy,70,415,bangkok","chalicefy,112,467,frankfurt","xnova,358,82,barcelona","chalicefy,180,543,beijing","xnova,624,572,budapest","lee,651,1761,chicago","alex,991,1698,budapest","bob,531,700,amsterdam","chalicefy,926,478,budapest","iris,235,1993,frankfurt","alex,107,812,beijing","maybe,199,1313,barcelona"]))





