"""
    Program: 02
    Program Name: 'Stack Operation'
    Author: M. Praveen Kumar
"""


class Stack:
    """
    Class "Stack" is a blueprint of the object "value" stored into stack_items,
    the stack operations are methods push(), pop(), peek(), size(), isEmpty(),
    """

    def __init__(self):
        # Instance variable "stack_items" to hold the values in the stack.
        self.stack_items = []

    def push(self, value: object):
        # Adding element to the end of the stack.
        self.stack_items.append(value)

    def pop(self):
        if not self.isEmpty():
            # Deleting the last elements that is inserted into stack.
            return self.stack_items.pop()
        else:
            # if .isEmpty() -> TRUE; value unavailable to pop.
            print("Stack is empty. Cannot pop element.")

    def peek(self):
        if not self.isEmpty():
            # Checking the latest element inserted into stack.
            return self.stack_items[-1]
        else:
            # if .isEmpty() -> TRUE; no value found.
            print("Stack is empty. Nothing to peek.")

    def size(self):
        # Returning the length of the stack.
        return len(self.stack_items)

    def isEmpty(self):
        # Returns bool TRUE/FALSE if stack is empty/stack is non-empty repectively.
        return len(self.stack_items) == 0

    def display_stack(self):

        if not self.isEmpty():
            for value in self.stack_items:
                # Displaying stack contents as inserted/deleted.
                print(value, end=" ")
        else:
            # if .isEmpty() -> TRUE; no value found in the stack.
            print("Stack is empty.")


def main():
    """
    main() holds the body content performing the stack operations with function calls and positional arguments
    that are passed onto the respective function decleration and parameters being assigned.
    """
    stack_obj = Stack()
    stack_obj.push(2)
    stack_obj.push(4)
    stack_obj.push(6)
    stack_obj.push(8)

    print("Displaying stack elements:")
    stack_obj.display_stack()

    print("\nIs stack empty?:", stack_obj.isEmpty())

    print("Top element:", stack_obj.peek())

    print("Popped element:", stack_obj.pop())
    stack_obj.display_stack()

    print("\nSize of the stack:", stack_obj.size())


if __name__ == "__main__":
    main()
