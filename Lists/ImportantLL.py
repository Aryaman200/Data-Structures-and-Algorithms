class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverse_linked_list_recursive(head):
    if head is None or head.next is None:
        return head
    p = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return p

def detect_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr, carry = dummy, 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        v = v1 + v2 + carry
        carry = v // 10
        curr.next = ListNode(v % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

def is_palindrome_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    p1, p2 = head, prev
    while p2:
        if p1.val != p2.val: return False
        p1, p2 = p1.next, p2.next
    return True
