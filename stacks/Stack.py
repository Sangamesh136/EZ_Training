class Stack(Exception):
    def __init__(self):
        self._items = []
        self._size = 0
    def push(self, data):
        self._items.append(data)
        self._size += 1
        return data
    def peek(self):
        return self._items[-1]
    def pop(self):
        if(self._size == 0):
            raise Exception("Cant pop an empty stack")
        data = self._items[self._size - 1]
        self._items.pop()
        self._size -= 1
        return data
    def isEmpty(self):
        return self._size == 0
    def size(self):
        return self._size
    def get_data(self):
        return self._items

# class stack(Exception):
#     def __init__(self):
#         self.items = []
#         self.size = 0
#
#     def push(self, value):
#         self.items.append(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size == 0:
#             raise Exception("cant pop from an empty stack")
#         poped = self.items[-1]
#         self.items.pop()
#         self.size -= 1
#         return poped
#
#     def peek(self):
#         if self.size == 0:
#             raise Exception("no elements in the stack to peek")
#         return self.items[-1]
#
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def getData(self):
#         return self.items
#
#     def sizeOf(self):
#         return self.size
#
