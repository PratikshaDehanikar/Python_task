# math_op using func and condition , (val1,val2,op)


def math_op(val1, val2, op):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2
    elif op == '/':
        if val2 != 0:
            return val1 / val2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unsupported operation"


result = math_op(10, 5, '+')
print(result)  # Output: 15

print()

result = math_op(10, 5, '-')
print(result)  # Output: 5

print()

result = math_op(10, 5, '*')
print(result)  # Output: 50

print()

result = math_op(10, 5, '/')
print(result)  # Output: 2.0

print()

result = math_op(10, 0, '/')
print(result)  # Output: Error: Division by zero

print()

result = math_op(10, 5, '^')
print(result)  # Output: Error: Unsupported operation
