from collections import deque
from DSA.trees.bfs.bfs_implementation import bst

queue = deque()

queue.append(bst.root)
left = True
while queue:
  qLen = len(queue)
  for i in range(qLen):
    node = queue.popleft()
    print('qLen ', qLen)
    print('key ', node.key)
    print('node.left ', node.left.key if node.left else None)
    print('node.right ', node.right.key if node.right else None)

    if left:
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    if not left:
      if node.right:
        queue.append(node.right)
      if node.left:
        queue.append(node.left)

  left = not left
