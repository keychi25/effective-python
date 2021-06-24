"""
    内部状態の欠損状態を扱うにはsetdefaultではなく，defalutdict（collections）を使う．
"""
from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
visits.add('Japan', 'Tokyo')

print(visits.data)
# defaultdict(<class 'set'>, {'England': {'Bath', 'London'}, 'Japan': {'Tokyo'}})