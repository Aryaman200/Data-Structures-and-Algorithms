class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_value(self, target_value, data):
        current = self.head
        while current and current.data != target_value:
            current = current.next
        if not current:
            raise ValueError(f"Value {target_value} not found in the list.")
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            raise ValueError("List is empty.")
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            raise ValueError("List is empty.")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if not self.head:
            raise ValueError("List is empty.")
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if not current.next:
            raise ValueError(f"Value {value} not found in the list.")
        current.next = current.next.next

    def display(self, separator=" -> "):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        print(separator.join(map(str, result)) + " -> None")

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def recursive_traverse(self, node=None):
        if node is None:
            node = self.head
        if node:
            print(node.data, end=" -> ")
            self.recursive_traverse(node.next)
        else:
            print("None")

    def linear_search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def recursive_linear_search(self, node, value, index=0):
        """Recursive Linear Search that returns index of the value if found."""
        if not node:
            return -1
        if node.data == value:
            return index
        return self.recursive_linear_search(node.next, value, index + 1)

    def binary_search(self, value):
        sorted_list = self.to_list()
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] == value:
                return mid
            elif sorted_list[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def bubble_sort(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def selection_sort(self):
        current = self.head
        while current:
            min_node = current
            runner = current.next
            while runner:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next
            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def insertion_sort(self):
        if not self.head:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    def quick_sort(self):
        if not self.head or not self.head.next:
            return
        self.head = self._quick_sort(self.head)

    def _quick_sort(self, head):
        if not head or not head.next:
            return head
        pivot = head
        left, right = None, None
        current = head.next
        while current:
            if current.data < pivot.data:
                if not left:
                    left = current
                else:
                    left_tail = left
                    while left_tail.next:
                        left_tail = left_tail.next
                    left_tail.next = current
            else:
                if not right:
                    right = current
                else:
                    right_tail = right
                    while right_tail.next:
                        right_tail = right_tail.next
                    right_tail.next = current
            current = current.next
        if left:
            left = self._quick_sort(left)
        if right:
            right = self._quick_sort(right)
        left_tail = left
        while left_tail and left_tail.next:
            left_tail = left_tail.next
        if left_tail:
            left_tail.next = pivot
        pivot.next = right
        return left if left else pivot

    def merge_sort(self):
        if not self.head or not self.head.next:
            return
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        left = self._merge_sort(head)
        right = self._merge_sort(middle)
        return self._merge(left, right)

    def _get_middle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        prev = None
        while head != middle:
            prev = head
            head = head.next
        prev.next = None
        return middle

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        return result

def menu():
    sll = SinglyLinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert after value")
        print("4. Delete at beginning")
        print("5. Delete at end")
        print("6. Delete value")
        print("7. Display list")
        print("8. Traverse (iterative)")
        print("9. Traverse (recursive)")
        print("10. Linear Search")
        print("11. Recursive Linear Search")
        print("12. Binary Search")
        print("13. Bubble Sort")
        print("14. Selection Sort")
        print("15. Insertion Sort")
        print("16. Quick Sort")
        print("17. Merge Sort")
        print("18. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert at beginning: "))
            sll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at end: "))
            sll.insert_at_end(data)
        elif choice == 3:
            target_value = int(input("Enter target value to insert after: "))
            data = int(input("Enter data to insert: "))
            try:
                sll.insert_after_value(target_value, data)
            except ValueError as e:
                print(e)
        elif choice == 4:
            try:
                sll.delete_at_beginning()
            except ValueError as e:
                print(e)
        elif choice == 5:
            try:
                sll.delete_at_end()
            except ValueError as e:
                print(e)
        elif choice == 6:
            value = int(input("Enter value to delete: "))
            try:
                sll.delete_value(value)
            except ValueError as e:
                print(e)
        elif choice == 7:
            sll.display()
        elif choice == 8:
            sll.traverse()
        elif choice == 9:
            sll.recursive_traverse()
        elif choice == 10:
            value = int(input("Enter value to search: "))
            index = sll.linear_search(value)
            print(f"Linear Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 11:
            value = int(input("Enter value to search: "))
            index = sll.recursive_linear_search(sll.head, value)
            print(f"Recursive Linear Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 12:
            value = int(input("Enter value to search: "))
            index = sll.binary_search(value)
            print(f"Binary Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 13:
            sll.bubble_sort()
            sll.display()
        elif choice == 14:
            sll.selection_sort()
            sll.display()
        elif choice == 15:
            sll.insertion_sort()
            sll.display()
        elif choice == 16:
            sll.quick_sort()
            sll.display()
        elif choice == 17:
            sll.merge_sort()
            sll.display()
        elif choice == 18:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
