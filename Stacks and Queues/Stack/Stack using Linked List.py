class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Element {data} pushed to stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped element: {popped_node.data}")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        print("Stack elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def menu():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter element to push: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            result = stack.peek()
            if result is not None:
                print(f"Top element is: {result}")
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
