class Converter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operators = set(['+', '-', '*', '/', '^'])

    def is_operator(self, ch):
        return ch in self.operators

    def precedence_of(self, op):
        return self.precedence.get(op, 0)

    def infix_to_postfix(self, expression):
        stack = []
        output = []
        for char in expression:
            if char.isalnum():  # If the character is an operand, add it to the output
                output.append(char)
            elif char == '(':  # If the character is '(', push it onto the stack
                stack.append(char)
            elif char == ')':  # If the character is ')', pop from the stack until '(' is encountered
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif self.is_operator(char):
                while stack and self.precedence_of(stack[-1]) >= self.precedence_of(char):
                    output.append(stack.pop())
                stack.append(char)
        
        while stack:
            output.append(stack.pop())

        return ''.join(output)

    def infix_to_prefix(self, expression):
        expression = expression[::-1]  # Reverse the expression
        expression = expression.replace('(', ')').replace(')', '(')  # Swap parentheses

        postfix = self.infix_to_postfix(expression)
        return postfix[::-1]  # Reverse the postfix result to get prefix

    def postfix_to_infix(self, expression):
        stack = []
        for char in expression:
            if char.isalnum():  # If the character is an operand, push it onto the stack
                stack.append(char)
            elif self.is_operator(char):  # If the character is an operator, pop two operands from the stack and form an infix expression
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(f'({operand1}{char}{operand2})')

        return stack[-1]

    def prefix_to_infix(self, expression):
        stack = []
        expression = expression[::-1]  # Reverse the prefix expression
        for char in expression:
            if char.isalnum():  # If the character is an operand, push it onto the stack
                stack.append(char)
            elif self.is_operator(char):  # If the character is an operator, pop two operands from the stack and form an infix expression
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(f'({operand1}{char}{operand2})')

        return stack[-1]

    def postfix_to_prefix(self, expression):
        infix = self.postfix_to_infix(expression)
        return self.infix_to_prefix(infix)


def menu():
    converter = Converter()
    while True:
        print("\nMenu:")
        print("1. Infix to Postfix")
        print("2. Infix to Prefix")
        print("3. Postfix to Infix")
        print("4. Prefix to Infix")
        print("5. Postfix to Prefix")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            expression = input("Enter infix expression: ")
            print("Postfix expression:", converter.infix_to_postfix(expression))
        elif choice == 2:
            expression = input("Enter infix expression: ")
            print("Prefix expression:", converter.infix_to_prefix(expression))
        elif choice == 3:
            expression = input("Enter postfix expression: ")
            print("Infix expression:", converter.postfix_to_infix(expression))
        elif choice == 4:
            expression = input("Enter prefix expression: ")
            print("Infix expression:", converter.prefix_to_infix(expression))
        elif choice == 5:
            expression = input("Enter postfix expression: ")
            print("Prefix expression:", converter.postfix_to_prefix(expression))
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

menu()
