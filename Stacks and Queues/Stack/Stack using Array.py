class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        
    def push(self, data):
        if len(self.stack) >= self.capacity:
            print("Stack overflow! Cannot push.")
            return
        self.stack.append(data)
        print(f"Element {data} pushed to stack.")
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        popped_element = self.stack.pop()
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        print("Stack elements:")
        for element in reversed(self.stack):
            print(element, end=" -> ")
        print("None")

def menu():
    capacity = int(input("Enter the capacity of the stack: "))
    stack = Stack(capacity)
    
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
