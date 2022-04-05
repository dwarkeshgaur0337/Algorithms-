class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    current = head = Node(arr[0])
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        if head is None:
            head = new_node
            
        else:
            head.next = new_node
            head = head.next

        
        # new_node.next = head
        # head = new_node

    for i in range(len(arr)):
        print(current.data)
        current = current.next

