def perform_operation(num1, num2, operation):
    print(operation)
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print('error to divide by zero')
        else:
            return num1 / num2
    else:
        print('Invalid operation')
