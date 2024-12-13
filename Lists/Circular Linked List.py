class Node:
    def __init__(self, data):
        # Node constructor to initialize a node with data and next pointer as None
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # CircularLinkedList constructor, starting with no nodes (head is None)
        self.head = None

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data)
        # If list is empty, create the first node, pointing to itself
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        # Traverse until we reach the last node
        while current.next != self.head:
            current = current.next
        # Insert new node and point it to the head to maintain circular structure
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, create the first node and link it to itself
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        # Traverse until we reach the last node
        while current.next != self.head:
            current = current.next
        # Add the new node at the end and link it back to the head
        current.next = new_node
        new_node.next = self.head

    def insert_after_value(self, target_value, data):
        # Insert a new node after a node with the specified value
        current = self.head
        # Traverse until we find the target node or return to the head (loop)
        while current and current.data != target_value:
            current = current.next
            if current == self.head:
                raise ValueError(f"Value {target_value} not found in the list.")
        # Create the new node and insert it after the current node
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        # Delete the node at the beginning of the list
        if not self.head:
            raise ValueError("List is empty.")
        if self.head.next == self.head:
            # If there’s only one node, set the list to empty
            self.head = None
            return
        current = self.head
        # Traverse until the last node (that points to the head)
        while current.next != self.head:
            current = current.next
        # Remove the first node and update the last node to point to the new head
        current.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        # Delete the node at the end of the list
        if not self.head:
            raise ValueError("List is empty.")
        if self.head.next == self.head:
            # If there’s only one node, set the list to empty
            self.head = None
            return
        current = self.head
        # Traverse to the last node
        while current.next != self.head:
            current = current.next
        # Find the previous node (one before the last node)
        prev = self.head
        while prev.next != current:
            prev = prev.next
        # Remove the last node by pointing the previous node to the head
        prev.next = self.head

    def delete_value(self, value):
        # Delete a specific node containing the value
        if not self.head:
            raise ValueError("List is empty.")
        if self.head.data == value:
            # If the node to delete is the head, we delete it from the beginning
            self.delete_at_beginning()
            return
        current = self.head
        # Traverse until we find the value or loop back to head
        while current.next != self.head and current.data != value:
            current = current.next
        if current.data != value:
            raise ValueError(f"Value {value} not found in the list.")
        # Find the previous node and point it to the next of the current node
        prev = self.head
        while prev.next != current:
            prev = prev.next
        prev.next = current.next

    def display(self):
        # Display the contents of the circular linked list
        if not self.head:
            print("List is empty.")
            return
        result = []
        current = self.head
        # Traverse the list and store the values in the result list
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        # Join the results with ' -> ' and display them
        print(" -> ".join(map(str, result)) + " -> (back to head)")

    def traverse(self):
        # Display the list using an iterative approach
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        # Traverse and print the data of each node
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def recursive_traverse(self, node=None):
        # Recursively traverse the list and print the nodes
        if node is None:
            node = self.head
        if node:
            print(node.data, end=" -> ")
            if node.next != self.head:
                self.recursive_traverse(node.next)
            else:
                print("(back to head)")

    def linear_search(self, value):
        # Perform a linear search for a value in the list
        if not self.head:
            return -1
        current = self.head
        index = 0
        # Traverse the list until we find the value or loop back to head
        while True:
            if current.data == value:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def recursive_linear_search(self, node, value, index=0):
        # Perform a recursive linear search for a value in the list
        if not node or node == self.head:
            return -1
        if node.data == value:
            return index
        return self.recursive_linear_search(node.next, value, index + 1)

    def binary_search(self, value):
        # Binary search requires a sorted list, so we first convert to a list
        sorted_list = self.to_list()
        left, right = 0, len(sorted_list) - 1
        # Perform standard binary search algorithm
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
        # Convert the circular linked list to a regular Python list for easier processing
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def bubble_sort(self):
        # Sort the list using bubble sort algorithm
        if not self.head:
            return
        swapped = True
        # Continue sorting until no more swaps are needed
        while swapped:
            swapped = False
            current = self.head
            # Traverse the list and swap nodes if they are in the wrong order
            while current.next != self.head:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def selection_sort(self):
        # Sort the list using selection sort algorithm
        if not self.head:
            return
        current = self.head
        while current:
            # Find the minimum node in the unsorted part of the list
            min_node = current
            runner = current.next
            while runner != self.head:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next
            # Swap the current node with the minimum node
            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def insertion_sort(self):
        # Sort the list using insertion sort algorithm
        if not self.head:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            # Insert the node into the sorted list
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next != self.head and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_list

    def quick_sort(self):
        # Sort the list using the quicksort algorithm
        if not self.head or not self.head.next:
            return
        self.head = self._quick_sort(self.head)

    def _quick_sort(self, head):
        # Helper method to perform quicksort
        if not head or not head.next:
            return head
        pivot = head
        left, right = None, None
        current = head.next
        while current != self.head:
            if current.data < pivot.data:
                if not left:
                    left = current
                else:
                    left_tail = left
                    while left_tail.next != self.head:
                        left_tail = left_tail.next
                    left_tail.next = current
            else:
                if not right:
                    right = current
                else:
                    right_tail = right
                    while right_tail.next != self.head:
                        right_tail = right_tail.next
                    right_tail.next = current
            current = current.next
        if left:
            left = self._quick_sort(left)
        if right:
            right = self._quick_sort(right)
        left_tail = left
        while left_tail and left_tail.next != self.head:
            left_tail = left_tail.next
        if left_tail:
            left_tail.next = pivot
        pivot.next = right
        return left if left else pivot

    def merge_sort(self):
        # Sort the list using merge sort algorithm
        if not self.head or not self.head.next:
            return
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        # Helper method to perform merge sort
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        left = self._merge_sort(head)
        right = self._merge_sort(middle)
        return self._merge(left, right)

    def _get_middle(self, head):
        # Find the middle node for merge sort
        slow, fast = head, head
        while fast != self.head and fast.next != self.head:
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
        # Merge two sorted halves
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
    cll = CircularLinkedList()
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
            cll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert at end: "))
            cll.insert_at_end(data)
        elif choice == 3:
            target_value = int(input("Enter target value to insert after: "))
            data = int(input("Enter data to insert: "))
            try:
                cll.insert_after_value(target_value, data)
            except ValueError as e:
                print(e)
        elif choice == 4:
            try:
                cll.delete_at_beginning()
            except ValueError as e:
                print(e)
        elif choice == 5:
            try:
                cll.delete_at_end()
            except ValueError as e:
                print(e)
        elif choice == 6:
            value = int(input("Enter value to delete: "))
            try:
                cll.delete_value(value)
            except ValueError as e:
                print(e)
        elif choice == 7:
            cll.display()
        elif choice == 8:
            cll.traverse()
        elif choice == 9:
            cll.recursive_traverse()
        elif choice == 10:
            value = int(input("Enter value to search: "))
            index = cll.linear_search(value)
            print(f"Linear Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 11:
            value = int(input("Enter value to search: "))
            index = cll.recursive_linear_search(cll.head, value)
            print(f"Recursive Linear Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 12:
            value = int(input("Enter value to search: "))
            index = cll.binary_search(value)
            print(f"Binary Search - Index: {index}" if index != -1 else "Value not found.")
        elif choice == 13:
            cll.bubble_sort()
            cll.display()
        elif choice == 14:
            cll.selection_sort()
            cll.display()
        elif choice == 15:
            cll.insertion_sort()
            cll.display()
        elif choice == 16:
            cll.quick_sort()
            cll.display()
        elif choice == 17:
            cll.merge_sort()
            cll.display()
        elif choice == 18:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
