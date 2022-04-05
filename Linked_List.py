from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        
        while last.next:
            last = last.next
        
        last.next = new_node

    def deleteNode(self, position):
        if self.head is None:
            return 

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return 
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break 

        if temp is None:
            return 

        if temp.next is None:
            return
        next = temp.next.next

        temp.next = None  




    


    