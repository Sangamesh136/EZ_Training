class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)


    def add_first(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        return temp


    def add_last(self,value):
        node = Node(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        # node.next = None
        # print(node.value)
        return node

    def insertAt(self,value, i):
        node = Node(value)
        temp = self.head
        while i -1 > 0:
            temp = temp.next
            i -=1
        node.next = temp.next
        temp.next = node
        return node

    def delete_first(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_last(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deleteAt(self,i):
        temp = self.head
        while i - 1 > 0:
            temp = temp.next
            i -= 1
        temp.next = temp.next.next

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value, "-->", end=" ")
            temp = temp.next
        print("end")

if __name__ == "__main__":
    ll = LinkedList(10)
    ll.add_first(20)
    ll.add_last(20)

    ll.insertAt(40, 2)
    ll.deleteAt(2)
    ll.delete_first()
    ll.delete_last()
    ll.printLL()
