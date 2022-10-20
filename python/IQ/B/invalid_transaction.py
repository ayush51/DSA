class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        import collections
        
        if not transactions:
            return []
        memo = collections.defaultdict(list)
        invalid_tran = set()
        
        for i, transaction in enumerate(transactions):
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(',') )
            
            if amount > 1000:
                invalid_tran.add(transaction)
            
            if name in memo:
                for tran in memo[name]:
                    _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in tran.split(','))
                    if abs(time-prev_time) <= 60 and prev_city != city:
                        invalid_tran.add(tran)
                        invalid_tran.add(transaction)
            memo[name].append(transaction)
        return invalid_tran
        

        
        sorting
        
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = sorted(transactions, key=lambda x: int(x.split(',')[1]))
        print(transactions)
        d, rst = collections.defaultdict(set), set()
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            for prev in set(d[name]):
                if int(time) - int(prev[1]) > 60:
                    d[name].remove(prev)
                elif prev[3] != city:
                    rst.add(trans)
                    rst.add(','.join(prev))
            if int(amount) > 1000:
                rst.add(trans)
            d[name].add((name, time, amount, city))
        
        
        o(n) + o(n)
        class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: [city]
                }
            else:
                if name not in r[time]:
                    r[time][name]=[city]
                else:
                    r[time][name].append(city)
        print(r)
                    
        
        for i in transactions:
            split = i.decode("utf-8").split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            print(time)
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (r[j][name][0] != city):
                    inv.append(i)
                    break
                                        
        return inv       
        
