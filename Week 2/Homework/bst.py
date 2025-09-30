class NodeTree():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
    
    def insertNode(self, key):
        if key < self.value:
            if self.left is None:
                self.left = NodeTree(key)
            else:
                self.left.insertNode(key)
        
        elif key > self.value:
            if self.right is None:
                self.right = NodeTree(key)
            else:
                self.right.insertNode(key)

    def searchNode(self, key) -> bool:
        if key == self.value:
            return True
        elif key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.searchNode(key)

        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.searchNode(key)

def main():
    root = NodeTree(15)

    for val in [10, 18, 8, 12, 16, 20, 5, 11]:
        root.insertNode(val)

    userSearch = 9
    print(f"Found {userSearch}" if root.searchNode(userSearch) else "Cannot find it")

    userSearch = 5
    print(f"Found {userSearch} in the bst" if root.searchNode(userSearch) else "Cannot find it")

    userSearch = 11
    print(f"Found {userSearch} in the bst" if root.searchNode(userSearch) else "Cannot find it")

if __name__ == "__main__":
    main()