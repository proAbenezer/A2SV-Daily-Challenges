# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:
    
    def __init__(self):
        self.randomHashMap = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        res  = val not in self.randomHashMap
        if res:
            self.randomHashMap[val] = len(self.randomList)
            self.randomList.append(val)
        return res
    def remove(self, val: int) -> bool:
       res = val in self.randomHashMap
       if res:
        index = self.randomHashMap[val]
        lastValue = self.randomList[-1]
        self.randomList[index] = lastValue
        self.randomList.pop()
        self.randomHashMap[lastValue] = index
        del self.randomHashMap[val]
       return res

    def getRandom(self) -> int:
        return random.choice(self.randomList)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()