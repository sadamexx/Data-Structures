class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        #self.length = 0

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def setNext(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def addToTail(self, value):
        new_node = Node(value)## calling the class node to create a new node
        #if head and tail are both none
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #this means that there is a head, there must also be a tail
            #set the old tail to next, and point to new node
            self.tail.next = new_node
            #set new tail to new node
            self.tail = new_node

    def pop_Tail(self):
        #if we have an empty linked list
        if self.head is None:
            return None
        #if we have only a single value in list
        if self.head is self.tail:
            value = self.head.getValue()
            self.head = None
            self.tail = None
            return value
        #if we have more than one value in list
        current = self.head
        new_tail = current
        while current.next is not self.tail:
            new_tail = current
            current = current.next
            self.tail = new_tail
            self.tail.next = None
            return current


ll = Node(1)
ll.setNext(Node(2))
