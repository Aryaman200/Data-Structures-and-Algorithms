class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.is_leaf = leaf
        self.keys = []  # List of keys in the node
        self.children = []  # List of children nodes (internal nodes) or pointers to data (leaf nodes)


class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode(True)  # Root node is initially a leaf
        self.order = order  # Maximum number of keys in a node

    def search(self, key, node=None):
        if node is None:
            node = self.root

        # Traverse the leaf nodes for search
        if node.is_leaf:
            if key in node.keys:
                return True
            return False
        else:
            # Internal nodes - find child node to descend into
            for i in range(len(node.keys)):
                if key < node.keys[i]:
                    return self.search(key, node.children[i])
            return self.search(key, node.children[-1])

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            # Root node is full, split it
            new_node = BPlusTreeNode(False)
            new_node.children.append(root)
            self.split(new_node, 0)
            self.root = new_node

        # Insert in the appropriate leaf node
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        if node.is_leaf:
            # Leaf node, simply insert the key in the sorted order
            node.keys.append(key)
            node.keys.sort()
        else:
            # Internal node
            for i in range(len(node.keys)):
                if key < node.keys[i]:
                    self.insert_non_full(node.children[i], key)
                    return
            self.insert_non_full(node.children[-1], key)

    def split(self, parent, index):
        """Split a full node into two nodes and promote a key to the parent"""
        node = parent.children[index]
        new_node = BPlusTreeNode(node.is_leaf)

        mid = len(node.keys) // 2
        mid_key = node.keys[mid]

        # Move the second half of the keys to the new node
        new_node.keys = node.keys[mid:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

        # Insert the mid_key into the parent node
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_node)

    def traverse(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            print("Leaf:", node.keys)
        else:
            print("Internal:", node.keys)
            for child in node.children:
                self.traverse(child)

    def display(self):
        """Display the B+ tree in in-order traversal"""
        print("Tree Traversal:")
        self.traverse(self.root)


def menu():
    bptree = BPlusTree(order=4)

    while True:
        print("\nMenu:")
        print("1. Insert element")
        print("2. Search element")
        print("3. Display tree")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to insert: "))
            bptree.insert(data)
            print(f"Element {data} inserted into the tree.")
        elif choice == 2:
            data = int(input("Enter element to search: "))
            if bptree.search(data):
                print(f"Element {data} found in the tree.")
            else:
                print(f"Element {data} not found in the tree.")
        elif choice == 3:
            bptree.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
