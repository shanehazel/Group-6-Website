from colorama import Fore, Style

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

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return None if self.is_empty() else self.top.data

    def is_empty(self):
        return self.top is None


def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = Stack()

    for char in infix:
        if char.isalnum():
            output.append(Fore.YELLOW + char + Style.RESET_ALL)
            print(''.join(output))
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(' and not stack.is_empty():
                output.append(Fore.CYAN + stack.pop() + Style.RESET_ALL)
                print(''.join(output))
            stack.pop()
        else:
            while (not stack.is_empty() and
                   precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                output.append(Fore.CYAN + stack.pop() + Style.RESET_ALL)
                print(''.join(output))
            stack.push(char)

    while not stack.is_empty():
        output.append(Fore.CYAN + stack.pop() + Style.RESET_ALL)
        print(''.join(output))

while True:
    infix_expression = input("\033[95mEnter the infix expression: \033[0m").replace(" ", "")

    print("\nConverting to postfix:")
    infix_to_postfix(infix_expression)

    continue_input = input("\nDo you want to continue? (yes/no): ").lower()
    if continue_input != 'yes':
        break
