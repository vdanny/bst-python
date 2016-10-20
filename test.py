from binary_search_tree import *

T = int(raw_input('Input number of nodes: '))
myTree = Tree()
root = None
for i in range(T):
    question = 'Input data no. ' + str(i+1) + ': '
    data = int(raw_input(question))
    root = myTree.insert(root,data)

print "Binary Search Tree Traversal"
print "============================"
print "InOrder:"
myTree.inOrder(root)

print "\nPostOrder:"
myTree.postOrder(root)

print "\nPreOrder:"
myTree.preOrder(root)

print "\nLevel Order:"
myTree.levelOrder(root)
height = myTree.getHeight(root)
print "\nHeight of tree: ", height
