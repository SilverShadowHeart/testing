def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():  # If the token is an operand, push it to the stack
            stack.append(int(token))
        else:  # Otherwise, it's an operator
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            # Pop the top two operands
            b = stack.pop()
            a = stack.pop()
            # Perform the operation
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero error")
                result = a / b  # Perform float division
            elif token == '//':
                result = a // b  # Integer division
            elif token == '%':
                result = a % b  # Modulus
            elif token == '**':
                result = a ** b  # Exponentiation
            else:
                raise ValueError(f"Unsupported operator: {token}") 
            # Push the result back to the stack
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]  # Final result

# Example usage
postfix_expr = input("Enter a postfix expression (space-separated): ")
try:
    result = evaluate_postfix(postfix_expr)
    print("Result:", result)
except Exception as e:
    print("Error:", e)
