class TreeNode:

    def __init__(self, key):
        self.key = key  # Value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child


class BinarySearchTree:

    def __init__(self):
        self.root = None  # Initialize the root of the BST

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # print(node.key)
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """Perform in-order traversal of the BST."""
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.key)
            self._inorder_recursive(node.right, elements)


    def insert(self, key):
        """Insert a new key into the BST and return a message."""
        if self.root is None:
            self.root = TreeNode(key)
            return f"Inserted {key} as the root node."
        else:
            return self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
                return f"Inserted {key} to the left of {node.key}."
            else:
                return self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
                return f"Inserted {key} to the right of {node.key}."
            else:
                return self._insert_recursive(node.right, key)
        else:
            return f"Key {key} already exists in the BST."



