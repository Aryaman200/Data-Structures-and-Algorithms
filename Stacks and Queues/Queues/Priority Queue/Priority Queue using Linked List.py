class Node:
    def __init__(self, data, priority):
        self.data = data      # Store data of the element
        self.priority = priority  # Store priority of the element
        self.next = None      # Pointer to the next node in the list

class PriorityQueue:
    def __init__(self):
        self.front = None     # Initialize the front pointer to None (empty queue)
    
    def insert(self, data, priority):
        # Create a new node with the data and priority
        new_node = Node(data, priority)
        
        # If the queue is empty or the new element has higher priority than the first element
        if not self.front or self.front.priority < priority:
            new_node.next = self.front
            self.front = new_node
            print(f"Element '{data}' with priority {priority} inserted at the front.")
            return
        
        # Traverse the queue to find the correct position for the new node
        current = self.front
        while current.next and current.next.priority >= priority:
            current = current.next
        
        # Insert the new node after the current node
        new_node.next = current.next
        current.next = new_node
        print(f"Element '{data}' with priority {priority} inserted.")
    
    def remove(self):
        # Remove and return the element with the highest priority
        if self.is_empty():
            print("Priority Queue is empty! Cannot remove element.")
            return None
        # The front node has the highest priority
        removed_node = self.front
        self.front = self.front.next
        print(f"Element '{removed_node.data}' with priority {removed_node.priority} removed.")
        return removed_node.data
    
    def peek(self):
        # Peek at the element with the highest priority
        if self.is_empty():
            print("Priority Queue is empty!")
            return None
        print(f"Element '{self.front.data}' with priority {self.front.priority} is at the front.")
        return self.front.data
    
    def is_empty(self):
        # Check if the queue is empty
        return self.front is None
    
    def display(self):
        # Display all elements in the priority queue
        if self.is_empty():
            print("Priority Queue is empty!")
            return
        current = self.front
        print("Priority Queue elements (priority, data):")
        while current:
            print(f"({current.priority}, '{current.data}')", end=" -> ")
            current = current.next
        print("None")

def menu():
    pq = PriorityQueue()
    
    while True:
        print("\nMenu:")
        print("1. Insert element")
        print("2. Remove element")
        print("3. Peek element")
        print("4. Display Priority Queue")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = input("Enter element to insert: ")
            priority = int(input("Enter priority (higher number means higher priority): "))
            pq.insert(data, priority)
        elif choice == 2:
            pq.remove()
        elif choice == 3:
            pq.peek()
        elif choice == 4:
            pq.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
