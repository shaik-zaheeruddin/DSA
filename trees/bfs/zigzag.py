from collections import deque
from implementation import bst

queue = deque()

queue.append(bst.root)
left = True
while queue:
  qLen = len(queue)
  for i in range(qLen):
    node = queue.popleft()
    print(node.key)

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
