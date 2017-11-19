import stack
import operations_on_stack

def main():
    s = stack.stack()
    for i in range(10):
        s.push(i)
    # while not s.is_empty():
    #     print(s.top(), s.size()-1)
    #     s.pop()
    operations_on_stack.insert_at_bottom(s, 11)
    operations_on_stack.reverse(s)
    print(s)


if __name__ == '__main__':
    main()
