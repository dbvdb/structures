class Stack:
    def __init__(self, container=[]):
        self.size = len(container)
        self.container = container

    def push(self, value):
        """Push a new item in stack"""
        self.container = self.container + [value]

        self.size += 1

    def pop(self):
        """Pop an item from stack"""
        if self.size == 0:
            return -1

        return self.container.pop()

    def empty(self):
        """Stack is empty or not"""
        return self.size == 0

    def peek(self):
        """"""
        if self.size == 0:
            return -1

        return self.container[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(12)
    stack.push(12)
    stack.push(13)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
