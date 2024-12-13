class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front  # Point rear to front to make it circular
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Point rear to front to maintain circular structure
        print(f"Element {data} enqueued.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        dequeued_data = self.front.data
        if self.front == self.rear:  # If only one element is present
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain the circular link
        print(f"Dequeued element: {dequeued_data}")
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        print("Queue elements:")
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.front:
                break
        print("None")

def menu():
    queue = CircularQueue()
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to enqueue: "))
            queue.enqueue(data)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            result = queue.peek()
            if result is not None:
                print(f"Front element is: {result}")
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
