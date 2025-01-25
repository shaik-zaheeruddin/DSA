from implementation import BinarySearchTree
from collections import deque

bst = BinarySearchTree()
bst.insert(10)
bst.insert(12)
bst.insert(14)

queue = deque()

queue.append(bst.root)

while queue:
  qLen = len(queue)
  for i in range(qLen):
    node = queue.popleft()
    print(node.key)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)


