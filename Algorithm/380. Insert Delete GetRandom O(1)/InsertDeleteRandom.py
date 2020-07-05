'''
referred to http://bookshadow.com/weblog/2016/08/04/leetcode-insert-delete-getrandom-o1/
'''
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # dataMap and dataList
        
        self.dataMap = {}
        self.dataList = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dataMap:
            return False
        self.dataMap[val] = len(self.dataList)
        self.dataList.append(val)
        return True
    

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dataMap:
            return False
        idx = self.dataMap[val]
        tail = self.dataList.pop()
        if idx < len(self.dataList):
            self.dataList[idx] = tail
            self.dataMap[tail] = idx
        del self.dataMap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.dataList)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
