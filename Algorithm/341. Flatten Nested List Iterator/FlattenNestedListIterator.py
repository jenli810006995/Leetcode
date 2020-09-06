'''
referred to http://bookshadow.com/weblog/2016/04/17/leetcode-flatten-nested-list-iterator/
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.list = nestedList
    
    def next(self) -> int:
        return self.stack.pop()
         
    def hasNext(self) -> bool:
        while self.list or self.stack:
            if not self.stack:
                self.stack.append(self.list.pop(0)) # pop delete the top most element
            while self.stack and not self.stack[-1].isInteger():
                top = self.stack.pop().getList()
                for e in top[::-1]:
                    self.stack.append(e)
            if self.stack and self.stack[-1].isInteger():
                return True
        return False
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Time: 9/6/2020

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.array = []
        def fill(nl):
            for ni in nl:
                if ni.isInteger():
                    self.array.append(ni.getInteger())
                else:
                    fill(ni.getList())
        fill(nestedList)
        self.index = 0
        
    def next(self) -> int:
        i = self.index
        self.index += 1
        return self.array[i]
       
    def hasNext(self) -> bool:
        return self.index < len(self.array)

## Link: https://leetcode.com/problems/flatten-nested-list-iterator/
## Reference: http://sdytlm.github.io/blog/2016/08/12/leetcode-flatten-nested-list-iterator/
