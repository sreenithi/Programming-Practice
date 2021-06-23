class BinarySearchTree:

    def __init__(self,value):

        self.data = value
        self.left = None
        self.right = None

    def addChild(self, childValue):

        if childValue == self.data:
            print("Element already exists in tree! Duplicates not allowed")

        elif childValue < self.data:
            if self.left is None:
                self.left = BinarySearchTree(childValue)
            else:
                self.left.addChild(childValue)

        else:
            if self.right is None:
                self.right = BinarySearchTree(childValue)
            else:
                self.right.addChild(childValue)            


    def removeNode(self, nodeValue):

        if self.data == nodeValue:

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            minNode = self.right

            while minNode.left is not None:
                minNode = minNode.left

            self.data = minNode.data

            self.right.removeNode(minNode.data)
                 

        elif nodeValue < self.data:
            self.left = self.left.removeNode(nodeValue)

        else:
            self.right = self.right.removeNode(nodeValue)

        return self
      

    def preorderTraversal(self, numSpaces=0):

        print(" "*numSpaces, self.data)

        if self.left is not None:
            self.left.preorderTraversal(numSpaces+2)
        if self.right is not None:
            self.right.preorderTraversal(numSpaces+2)


    def postorderTraversal(self,numSpaces=0):

        if self.left is not None:
            self.left.postorderTraversal(numSpaces+2)
        if self.right is not None:
            self.right.postorderTraversal(numSpaces+2)

        print(" "*numSpaces, self.data)


    def inorderTraversal(self, numSpaces=0):

        if self.left is not None:
            self.left.inorderTraversal(numSpaces+2)

        print(" "*numSpaces, self.data)

        if self.right is not None:
            self.right.inorderTraversal(numSpaces+2)


    def binarySearch(self, searchNum):

        print(self.data)
        if self.data == searchNum:
            return self
        
        elif searchNum < self.data:
            if self.left is None:
                return None
            else:
                return self.left.binarySearch(searchNum)

        else:
            if self.right is None:
                return None
            else:
                return self.right.binarySearch(searchNum)


if __name__ == '__main__':

    tree = BinarySearchTree(5)

    tree.addChild(2)
    tree.addChild(1)
    tree.addChild(3)
    tree.addChild(4)

    tree.addChild(8)
    tree.addChild(6)
    tree.addChild(5)
    tree.addChild(7)

    tree.addChild(11)
    tree.addChild(10)
    tree.addChild(9)
    tree.addChild(15)
    tree.addChild(12)
    tree.addChild(13)


    print("Preorder Traversal:")
    tree.preorderTraversal()
    print()

    print("Postorder Traversal:")
    tree.postorderTraversal()
    print()

    print("Inorder Traversal:")
    tree.inorderTraversal()
    print()

    print("BFS searching for 11. Traversed Elements:")
    elt = tree.binarySearch(11)

    if elt is None:
        print("Element not found")
    else:
        print("Element found!! Element is",elt.data)


    print("Searching for 12. Traversed Elements:")
    elt = tree.binarySearch(15)

    if elt is None:
        print("Element not found")
    else:
        print("Element found!! Element is",elt.data)


    print("\nChecking for non existing elements")
    print("Searching for -2")
    result = tree.binarySearch(-2)
    if result is None:
        print("Element not found")
    else:
        print("Element found!! Element is",result.data)
        

    print("\nSearching for 20")
    result = tree.binarySearch(20)
    if result is None:
        print("Element not found")
    else:
        print("Element found!! Element is",result.data)

    tree.removeNode(11)

    tree.inorderTraversal()

    print("getting height of node 5")
##    node8 = tree.binarySearch(8)
    height5 = tree.getMaxHeight()

    print("height of node 5:",height5)
    
