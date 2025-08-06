class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder_traversal(root):
    res, stack = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

def preorder_traversal(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res

def postorder_traversal(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return res[::-1]

def level_order_traversal(root):
    from collections import deque
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res

def tree_height(root):
    if not root: return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def tree_diameter(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter
        if not node: return 0
        l = dfs(node.left)
        r = dfs(node.right)
        diameter = max(diameter, l + r)
        return 1 + max(l, r)
    dfs(root)
    return diameter

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q: return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right: return root
    return left or right

def mirror_tree(root):
    if root:
        root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

def insert_bst(root, val):
    if not root: return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def search_bst(root, val):
    if not root or root.val == val: return root
    if val < root.val: return search_bst(root.left, val)
    else: return search_bst(root.right, val)

def delete_bst(root, key):
    if not root: return None
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        min_larger = root.right
        while min_larger.left: min_larger = min_larger.left
        root.val = min_larger.val
        root.right = delete_bst(root.right, min_larger.val)
    return root

def validate_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if not (lo < root.val < hi): return False
    return validate_bst(root.left, lo, root.val) and validate_bst(root.right, root.val, hi)

def top_view(root):
    from collections import deque
    if not root: return []
    q = deque([(root, 0)])
    hd_node = {}
    while q:
        node, hd = q.popleft()
        if hd not in hd_node: hd_node[hd] = node.val
        if node.left: q.append((node.left, hd-1))
        if node.right: q.append((node.right, hd+1))
    return [hd_node[k] for k in sorted(hd_node)]

def bottom_view(root):
    from collections import deque
    if not root: return []
    q = deque([(root, 0)])
    hd_node = {}
    while q:
        node, hd = q.popleft()
        hd_node[hd] = node.val
        if node.left: q.append((node.left, hd-1))
        if node.right: q.append((node.right, hd+1))
    return [hd_node[k] for k in sorted(hd_node)]

def kth_smallest_bst(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.right

def kth_largest_bst(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.right
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.left
