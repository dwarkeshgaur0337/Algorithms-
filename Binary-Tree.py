
class Node:
    def __init__(self, key) -> None:
        self.right = None
        self.left = None 
        self.val = key


    def PreOrder(self):
        print(self.val, end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.val, end=" ")
        if self.right:
            self.right.InOrder()

    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()

        print(self.val, end=" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)

    print(root.InOrder())

    