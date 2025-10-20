class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return f"DoctorNode({self.name!r})"



class DoctorTree:

    def __init__(self):

        self.root = None

    def _find(self, node, name):

        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self._find(node.left, name)
        if left_search:
            return left_search
        return self._find(node.right, name)

    def insert(self, parent_name, child_name, side):
        if self.root is None:
            raise ValueError("Tree has no root. Please set tree.root first.")

        parent = self._find(self.root, parent_name)
        if not parent:
            raise ValueError(f"Parent '{parent_name}' not found in the tree.")

        side = side.lower()
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        if side == "left":
            if parent.left is not None:
                raise ValueError(f"{parent_name} already has a left report.")
            parent.left = DoctorNode(child_name)
        else:
            if parent.right is not None:
                raise ValueError(f"{parent_name} already has a right report.")
            parent.right = DoctorNode(child_name)

    # ---------------------------
    # Traversal Methods
    # ---------------------------
    def preorder(self, node):

        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):

        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):

        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# ---------------------------
# Test Section
# ---------------------------
if __name__ == "__main__":
    # Build the example doctor tree
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Display traversal results
    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Expected Output:
    # Preorder: ['Dr. Croft', 'Dr. Phan', 'Dr. Morgan', 'Dr. Carson', 'Dr. Goldsmith']
    # Inorder:  ['Dr. Morgan', 'Dr. Phan', 'Dr. Carson', 'Dr. Croft', 'Dr. Goldsmith']
    # Postorder:['Dr. Morgan', 'Dr. Carson', 'Dr. Phan', 'Dr. Goldsmith', 'Dr. Croft']

    # Example edge case: inserting under invalid parent
    try:
        tree.insert("Dr. Who", "Dr. Strange", "left")
    except ValueError as e:
        print("Error:", e)




# Test your DoctorTree and DoctorNode classes here
