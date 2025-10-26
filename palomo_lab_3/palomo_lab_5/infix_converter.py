def infix_to_postfix(values):
    # Dictionary and initialize empty stacks.
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []

    # Validate the variables.
    for value in values.split():
        if value.isalnum():
            output.append(value)
        elif value == '(':
            stack.append(value)
        elif value == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[value]:
                output.append(stack.pop())
            stack.append(value)
    
    while stack:
        output.append(stack.pop())
    
    # Return the answer.
    return ' '.join(output)

# Direct Program in the terminal.
if __name__ == "__main__":
    while True:
        print("Note: ALWAYS add one space after a character.")
        try:
            infix = input("Enter infix expression (space-separated): ")
            print("Postfix expression:", infix_to_postfix(infix))
            break
        except:
            print("Invalid input.\n")