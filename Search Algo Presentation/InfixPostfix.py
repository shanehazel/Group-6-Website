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
    steps = []

    for char in infix:
        if char.isalnum():
            output.append(char)
            steps.append(''.join(output))
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(' and not stack.is_empty():
                output.append(stack.pop())
                steps.append(''.join(output))
            stack.pop()
        else:
            while (not stack.is_empty() and
                   precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                output.append(stack.pop())
                steps.append(''.join(output))
            stack.push(char)

    while not stack.is_empty():
        output.append(stack.pop())
        steps.append(''.join(output))

    return ''.join(output), steps
