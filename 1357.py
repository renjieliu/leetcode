class Cashier:
    def __init__(self, n: int, discount: int, products: 'List[int]', prices: 'List[int]'):
        self.gap = n
        self.cust_cnt = 0  # counter for the customer
        self.discount = discount
        self.prod = {}  # the prod-price list
        i = 0
        while i < len(products):
            curr = products[i]
            if curr not in self.prod:
                self.prod[curr] = prices[i]
            i += 1

    def getBill(self, product: 'List[int]', amount: 'List[int]') -> float:
        total = 0
        i = 0
        while i < len(product):
            p = product[i]
            curr_charge = self.prod[p] * amount[i]
            total += curr_charge
            i += 1
        self.cust_cnt += 1
        if self.cust_cnt == self.gap:
            self.cust_cnt = 0
            total *= (1 - self.discount / 100)
        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)