class Node:

    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class LinkedList:

    def __init__(self, values=[]):
        self._head = None
        for v in values:
            current_node = self._head
            self._head = Node(v)
            self._head.set_next(current_node)

    def __len__(self):
        count = 0
        current_node = self._head
        while (current_node != None):
            count += 1
            current_node = current_node.next()
        return count
    
    def __iter__(self):
        self.iter_node = self._head
        return self
    
    def __next__(self):
        if self.iter_node is None:
            raise StopIteration
        else:
            value = self.iter_node.value()
            self.iter_node = self.iter_node.next()
            return value

    def head(self):
        if self._head == None:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value):
        current_node = self._head
        self._head = Node(value)
        self._head.set_next(current_node)

    def pop(self):
        if self._head == None:
            raise EmptyListException('The list is empty.')
        value = self._head.value()
        self._head = self._head.next()
        return value

    def reversed(self):
        if self._head == None:
            return None
        
        prev_node = self._head
        current_node = self._head.next()
        while current_node != None:
            next_node = current_node.next()
            current_node.set_next(prev_node)
            prev_node = current_node
            current_node = next_node

        self._head.set_next(None)
        self._head = prev_node
        
        return self

class EmptyListException(Exception):

    def __init__(self, message):
        self.message = message

sut = LinkedList([])
x = sut.reversed()
list(x)
