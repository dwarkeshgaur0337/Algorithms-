class newNode:
    def __init__(self, k) -> None:
        self.key = k
        self.left = self.right = None

def calculateDepth(node):
    d = 0
    while (node is not None):
        d+=1
        node = node.left
    return d 

def isPerfectBinary(root, d, level = 0):
    if root is None:
        return True 

    if (root.left is None and root.right is None):
        return (d==level+1)

    return (isPerfectBinary(root.left,d,level +1) and isPerfectBinary(root.right,d,level+1))


if __name__ == "__main__":
    
    root = None
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    print(isPerfectBinary(root,calculateDepth(root)))

