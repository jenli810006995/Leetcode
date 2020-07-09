'''
referred to https://blog.csdn.net/fuxuemingzhu/article/details/79253237
'''
# Solution 1:

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # an empty stack
        

    def push(self, x: int) -> None:
        '''
        :type x : int
        :rtype: void
        '''
        if not self.stack:
            self.stack.append((x,x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))     

    def pop(self) -> None:
        '''
        :rtype: void
        '''
        self.stack.pop()
        
    def top(self) -> int:
        '''
        :rtype: int
        '''
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        '''
        :rtype: int
        '''
        return self.stack[-1][1]

# Solution 2:

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x: int) -> None:
        '''
        :type x : int
        :rtype: void
        '''
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self) -> None:
        '''
        :rtype: void
        '''
        self.stack.pop()
        self.min.pop()
        
    def top(self) -> int:
        '''
        :rtype: int
        '''
        return self.stack[-1]
        

    def getMin(self) -> int:
        '''
        :rtype: int
        '''
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
