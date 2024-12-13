class Node:
    def __init__(self, data):
        self.data = data  # Store the data of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

class BinaryTree:
    def __init__(self):
        self.root = None  # Initialize an empty tree with no root
    
    def insert(self, data):
        """ Insert data into the binary tree. For simplicity, we'll insert 
        elements as left children of existing nodes, creating a "linked-list-like" structure. """
        new_node = Node(data)
        if not self.root:
            self.root = new_node  # If the tree is empty, set the new node as the root
        else:
            current = self.root
            while current.left:  # Traverse to the leftmost node
                current = current.left
            current.left = new_node  # Insert as left child of the current node
        print(f"Inserted {data} into the tree.")
    
    def inorder(self, node):
        """ Perform an in-order traversal (left, root, right). """
        if node:
            self.inorder(node.left)  # Traverse left subtree
            print(node.data, end=" -> ")  # Visit the node
            self.inorder(node.right)  # Traverse right subtree

    def preorder(self, node):
        """ Perform a pre-order traversal (root, left, right). """
        if node:
            print(node.data, end=" -> ")  # Visit the node
            self.preorder(node.left)  # Traverse left subtree
            self.preorder(node.right)  # Traverse right subtree
    
    def postorder(self, node):
        """ Perform a post-order traversal (left, right, root). """
        if node:
            self.postorder(node.left)  # Traverse left subtree
            self.postorder(node.right)  # Traverse right subtree
            print(node.data, end=" -> ")  # Visit the node
    
    def search(self, data):
        """ Search for a node with specific data in the binary tree. """
        current = self.root
        while current:
            if current.data == data:
                return True  # Found the data
            elif current.left and current.data > data:
                current = current.left  # Move to the left if data is smaller
            else:
                current = current.right  # Move to the right if data is greater
        return False  # Data not found in the tree

    def display(self):
        """ Display the tree in in-order traversal (left, root, right). """
        if self.root:
            print("In-order Traversal: ")
            self.inorder(self.root)
            print("None")
        else:
            print("Tree is empty.")
    
def menu():
    tree = BinaryTree()

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
            tree.insert(data)
        elif choice == 2:
            data = int(input("Enter element to search: "))
            if tree.search(data):
                print(f"Element {data} found in the tree.")
            else:
                print(f"Element {data} not found in the tree.")
        elif choice == 3:
            print("In-order Traversal: ", end="")
            tree.inorder(tree.root)
            print()
        elif choice == 4:
            print("Pre-order Traversal: ", end="")
            tree.preorder(tree.root)
            print()
        elif choice == 5:
            print("Post-order Traversal: ", end="")
            tree.postorder(tree.root)
            print()
        elif choice == 6:
            tree.display()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
