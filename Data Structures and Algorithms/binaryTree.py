import collections

class BinaryTree:

    def __init__(self,value,left=None,right=None):

        self.data = value
        self.left = left
        self.right = right


    def preorderTraversal(self, numSpaces=0):

        print(" "*numSpaces, self.data)

        if self.left is not None:
            self.left.preorderTraversal(numSpaces+2)
        if self.right is not None:
            self.right.preorderTraversal(numSpaces+2)


    def postorderTraversal(self, numSpaces=0):

        if self.left is not None:
            self.left.postorderTraversal(numSpaces+2)
        if self.right is not None:
            self.right.postorderTraversal(numSpaces+2)

        print(" "*numSpaces, self.data)


    def inorderTraversal(self, numSpaces=0):

        if self.left is not None:
            self.left.inorderTraversal(numSpaces+2)

        print(" "*numSpaces,self.data)

        if self.right is not None:
            self.right.inorderTraversal(numSpaces+2)


    def dfs(self,searchValue):

        print(self.data)
        if self.data == searchValue:
            return self

        if self.left is not None:
            left = self.left.dfs(searchValue)
            if left is not None:
                return left

        if self.right is not None:
            right = self.right.dfs(searchValue)
            if right is not None:
                return right

        return None


    def bfs(self, searchValue):

        nodesQueue = collections.deque()
        nodesQueue.append(self)

        while(len(nodesQueue) != 0):
            
            curElt = nodesQueue.popleft()
            
            print(curElt.data)
            if curElt.data == searchValue:
                return curElt

            if curElt.left is not None:
                nodesQueue.append(curElt.left)

            if curElt.right is not None:
                nodesQueue.append(curElt.right)

##        if self.left is not None and self.left.data == searchValue:
##            return self.left
##
##        if self.right is not None and self.right.data == searchValue:
##            return self.right
##
##        if self.left is not None:
##            left = self.left.bfs(searchValue)
##            if left is not None:
##                return left
##
##        if self.right is not None:
##            right = self.right.bfs(searchValue)
##            if right is not None:
##                return right

        return None

if __name__ == '__main__':

    tree = BinaryTree('+')
    tree1 = BinaryTree(1)
    treeStar = BinaryTree('*')
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)

    tree.left = tree1
    tree.right = treeStar
    treeStar.left = tree2
    treeStar.right = tree3

##    tree1 = BinaryTree(1)
##    tree2 = BinaryTree(2)
##    tree3 = BinaryTree(3)
##    tree4 = BinaryTree(4)
##    tree5 = BinaryTree(5)
##    tree6 = BinaryTree(6)
##    tree7 = BinaryTree(7)
##    tree8 = BinaryTree(8)
##
##    tree1.left = tree2
##    tree2.left = tree3
##    tree2.right = tree4
##    
##    tree1.right = tree5
##    tree5.left = tree6
##    tree5.right = tree7
##    tree7.right = tree8

    print("Preorder Traversal:")
    tree.preorderTraversal()
    print()

    print("Postorder Traversal:")
    tree.postorderTraversal()
    print()

    print("Inorder Traversal:")
    tree.inorderTraversal()
    print()

    print("BFS searching for 8. Traversed Elements:")
    elt = tree1.bfs(8)

    if elt is None:
        print("Element not found")
    else:
        print("Element found!! Element is",elt.data)
