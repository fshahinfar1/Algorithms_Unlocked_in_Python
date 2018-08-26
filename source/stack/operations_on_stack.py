import stack

def insert_at_bottom(stack, value):
    if stack.is_empty():
        stack.push(value)
        return
    tmp = stack.top()
    stack.pop()
    insert_at_bottom(stack, value)
    stack.push(tmp)

def reverse(stack):
    if not stack.is_empty():
        tmp = stack.top()
        stack.pop()
        reverse(stack)
        insert_at_bottom(stack, tmp)

def insert_sorted(stack, value):
    if stack.is_empty() or stack.top() < value:
        stack.push(value)
    else:
        tmp = stack.top()
        stack.pop()
        insert_sorted(stack, value)
        stack.push(tmp)

def sort(stack):
    pass
