class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.leaf = leaf  # True if leaf node, False if internal node
        self.keys = []  # List of keys in the node
        self.children = []  # List of child nodes

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Root node is initially a leaf
        self.t = t  # Minimum degree

    def search(self, key, node=None):
        """Search for a key in the B-tree."""
        if node is None:
            node = self.root

        # Find the first key greater than or equal to the key
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and node.keys[i] == key:
            return True  # Key found
        
        if node.leaf:
            return False  # Reached leaf and key is not found
        
        return self.search(key, node.children[i])  # Search in the appropriate child

    def insert(self, key):
        """Insert a key into the B-tree."""
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            # Root is full, need to split
            new_node = BTreeNode(self.t, False)
            new_node.children.append(self.root)
            self.split(new_node, 0)
            self.root = new_node
        
        self.insert_non_full(self.root, key)

    def split(self, parent, index):
        """Split a full child node into two and promote a key to the parent."""
        node = parent.children[index]
        new_node = BTreeNode(self.t, node.leaf)
        mid = len(node.keys) // 2
        mid_key = node.keys[mid]
        
        # Move the second half of the keys and children to the new node
        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]
        
        if not node.leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]
        
        # Insert the middle key into the parent node
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_node)

    def insert_non_full(self, node, key):
        """Insert a key into a node that is not full."""
        if node.leaf:
            # Insert the key in sorted order
            node.keys.append(key)
            node.keys.sort()
        else:
            # Find the child node where the key should go
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # If the child is full, split it
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1

            # Insert the key in the appropriate child
            self.insert_non_full(node.children[i], key)

    def inorder_traversal(self, node=None):
        """In-order traversal of the B-tree."""
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.inorder_traversal(node.children[i])
            print(node.keys[i], end=" ")
        
        if not node.leaf:
            self.inorder_traversal(node.children[-1])

    def display(self):
        """Display the B-tree."""
        print("In-order Traversal of the B-tree:")
        self.inorder_traversal(self.root)
        print()

def menu():
    btree = BTree(t=3)  # Minimum degree of the tree is 3

    while True:
        print("\nMenu:")
        print("1. Insert element")
        print("2. Search element")
        print("3. Display tree")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to insert: "))
            btree.insert(data)
            print(f"Element {data} inserted into the tree.")
        elif choice == 2:
            data = int(input("Enter element to search: "))
            if btree.search(data):
                print(f"Element {data} found in the tree.")
            else:
                print(f"Element {data} not found in the tree.")
        elif choice == 3:
            btree.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
