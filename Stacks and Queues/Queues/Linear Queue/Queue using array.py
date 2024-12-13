class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        print(f"Element {data} enqueued.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        dequeued_data = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        print(f"Dequeued element: {dequeued_data}")
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        print("Queue elements:")
        while i != self.rear:
            print(self.queue[i], end=" -> ")
            i = (i + 1) % self.capacity
        print("None")

def menu():
    capacity = int(input("Enter the capacity of the queue: "))
    queue = Queue(capacity)
    
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
