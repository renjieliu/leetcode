class Solution:
    def displayTable(self, orders: 'List[List[str]]') -> 'List[List[str]]':
        hmp_food = {}
        hmp_table = {}
        for customer, table, food in orders:
            if food not in hmp_food:
                hmp_food[food] = {}
            if table not in hmp_food[food]:
                hmp_food[food][table] = 0
            if table not in hmp_table:
                hmp_table[table] = {}
            if food not in hmp_table[table]:
                hmp_table[table][food] = 0
            hmp_food[food][table] += 1
            hmp_table[table][food] += 1

        output = []
        output.append(["Table"] + sorted(hmp_food.keys()))  # add the food name to the title
        for i, c in enumerate(sorted(hmp_table.keys(), key=lambda x: int(x))):
            output.append([str(c)])
            for f in output[0][1:]:  # go thru the food
                if f not in hmp_table[c]:
                    output[-1].append("0")
                else:
                    output[-1].append(str(hmp_table[c][f]))
        return output



