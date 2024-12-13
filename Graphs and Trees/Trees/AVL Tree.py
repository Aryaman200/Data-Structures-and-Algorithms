class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # Height of the node (used for balancing)

class AVLTree:
    def __init__(self):
        self.root = None  # Root of the tree
    
    def height(self, node):
        """Get the height of the node"""
        return node.height if node else 0
    
    def balance_factor(self, node):
        """Get the balance factor of a node (left height - right height)"""
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        """Update the height of a node"""
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        """Right rotation of the tree rooted at y"""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self.update_height(y)
        self.update_height(x)

        # Return the new root
        return x
    
    def left_rotate(self, x):
        """Left rotation of the tree rooted at x"""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self.update_height(x)
        self.update_height(y)

        # Return the new root
        return y
    
    def balance(self, node):
        """Balance the node by checking the balance factor and applying rotations"""
        balance_factor = self.balance_factor(node)

        # Left heavy
        if balance_factor > 1:
            if self.balance_factor(node.left) < 0:  # Left-Right case
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)  # Left-Left case

        # Right heavy
        if balance_factor < -1:
            if self.balance_factor(node.right) > 0:  # Right-Left case
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)  # Right-Right case

        # No imbalance
        return node
    
    def insert(self, node, data):
        """Insert a new node with given data into the AVL tree and balance the tree"""
        if not node:
            return Node(data)

        # Perform normal BST insert
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        # Update height of the ancestor node
        self.update_height(node)

        # Balance the node
        return self.balance(node)
    
    def search(self, node, data):
        """Search for a node with given data"""
        if not node:
            return None
        if node.data == data:
            return node
        elif data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
    
    def inorder(self, node):
        """In-order traversal (left, root, right)"""
        if node:
            self.inorder(node.left)
            print(node.data, end=" -> ")
            self.inorder(node.right)
    
    def preorder(self, node):
        """Pre-order traversal (root, left, right)"""
        if node:
            print(node.data, end=" -> ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        """Post-order traversal (left, right, root)"""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" -> ")
    
    def display(self):
        """Display the tree in in-order traversal"""
        if self.root:
            print("In-order Traversal: ", end="")
            self.inorder(self.root)
            print("None")
        else:
            print("Tree is empty.")
    
def menu():
    avl_tree = AVLTree()

    while True:
        print("\nMenu:")
        print("1. Insert element")
        print("2. Search element")
        print("3. In-order traversal")
        print("4. Pre-order traversal")
        print("5. Post-order traversal")
        print("6. Display tree")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to insert: "))
            avl_tree.root = avl_tree.insert(avl_tree.root, data)
            print(f"Element {data} inserted into the tree.")
        elif choice == 2:
            data = int(input("Enter element to search: "))
            node = avl_tree.search(avl_tree.root, data)
            if node:
                print(f"Element {data} found in the tree.")
            else:
                print(f"Element {data} not found in the tree.")
        elif choice == 3:
            print("In-order Traversal: ", end="")
            avl_tree.inorder(avl_tree.root)
            print()
        elif choice == 4:
            print("Pre-order Traversal: ", end="")
            avl_tree.preorder(avl_tree.root)
            print()
        elif choice == 5:
            print("Post-order Traversal: ", end="")
            avl_tree.postorder(avl_tree.root)
            print()
        elif choice == 6:
            avl_tree.display()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
