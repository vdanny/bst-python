import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
        
class Tree:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self,root):
        if root == None:
            return -1
        else:
            left = self.getHeight(root.left)
            right = self.getHeight(root.right)

            if left > right:
                return left + 1
            else:
                return right + 1

    def inOrder(self, root):
        if root != None:
            # go to left nodes
            self.inOrder(root.left)

            # process current
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()

            # go to right nodes
            self.inOrder(root.right)

    def postOrder(self, root):
        if root != None:
            # go to left nodes
            self.postOrder(root.left)
            
            # go to right nodes
            self.postOrder(root.right)
            
            # process current
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()

    # Depth First Search
    def preOrder(self, root):
        if root != None:
            # process current
            sys.stdout.write(str(root.data) + " ")
            sys.stdout.flush()
            
            # go to left nodes
            self.preOrder(root.left)
            
            # go to right nodes
            self.preOrder(root.right)

    # Breadth First Search
    queue = []
    def levelOrder(self, root):
        if root != None:
            # start with root in queue
            self.queue.append(root)

            i = 0
            cur = self.queue[i]
            while cur != None:

                # process current
                sys.stdout.write(str(cur.data) + " ")
                sys.stdout.flush()

                # append the queue with left and right node if exists
                if cur.left != None:
                    self.queue.append(cur.left)
                if cur.right != None:
                    self.queue.append(cur.right)

                # move to next node in queue
                i+=1
                if i < len(self.queue):
                    cur = self.queue[i]
                else:
                    cur = None

