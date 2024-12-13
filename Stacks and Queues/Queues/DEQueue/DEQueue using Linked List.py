class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Element {data} inserted at front.")

    def insert_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Element {data} inserted at rear.")

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty! Cannot delete from front.")
            return None
        deleted_data = self.front.data
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        print(f"Element {deleted_data} deleted from front.")
        return deleted_data

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty! Cannot delete from rear.")
            return None
        deleted_data = self.rear.data
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        print(f"Element {deleted_data} deleted from rear.")
        return deleted_data

    def peek_front(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        return self.rear.data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Deque is empty!")
            return
        current = self.front
        print("Deque elements:")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def menu():
    deque = Deque()
    
    while True:
        print("\nMenu:")
        print("1. Insert at Front")
        print("2. Insert at Rear")
        print("3. Delete from Front")
        print("4. Delete from Rear")
        print("5. Peek Front")
        print("6. Peek Rear")
        print("7. Display Deque")
        print("8. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to insert at front: "))
            deque.insert_front(data)
        elif choice == 2:
            data = int(input("Enter element to insert at rear: "))
            deque.insert_rear(data)
        elif choice == 3:
            deque.delete_front()
        elif choice == 4:
            deque.delete_rear()
        elif choice == 5:
            result = deque.peek_front()
            if result is not None:
                print(f"Front element is: {result}")
        elif choice == 6:
            result = deque.peek_rear()
            if result is not None:
                print(f"Rear element is: {result}")
        elif choice == 7:
            deque.display()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
