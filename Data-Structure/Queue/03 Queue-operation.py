"""
    Program: 03
    Program Name: 'Queue Operation'
    Author: M. Praveen Kumar
"""

class Queue:
    # Class variable "queue_data" that holds elements of the queue.
    queue_data = []

    def enQueue(self, value):
        # Adding elements to the queue.
        self.queue_data.append(value)
    
    def deQueue(self):
        if not self.isEmpty():
            # Deleting the elements in the queue.
            return self.queue_data.pop(0)
        else:
            # if .isEmpty() -> TRUE; value unavailable to be deleted.
            print("Queue is empty. Cannot delete element")

    def peek(self):
        if not self.isEmpty():
            # Checking on the latest element added to the queue.
            return self.queue_data[0]
        else:
             # if .isEmpty() -> TRUE; no value found.
            print("Queue is empty. Nothing to display")
    
    def size(self):
        # Returning the length of the stack.
        return len(self.queue_data)

    def isEmpty(self):
        # Returns bool TRUE/FALSE if stack is empty/stack is non-empty repectively.
        return len(self.queue_data) == 0
    
    def display_queue(self):
        if not self.isEmpty():
            for data in self.queue_data:
                # Displaying stack contents as inserted/deleted.
                print(data, end=" ")
        else:
            # if .isEmpty() -> TRUE; no value found in the queue.
            print("Queue is empty.")

def main():
    """
    main() holds the body content performing the stack operations with function calls and positional arguments
    that are passed onto the respective function decleration and parameters being assigned.
    """
    queue_obj = Queue()
    queue_obj.display_queue() 
    
    queue_obj.enQueue(10)
    queue_obj.enQueue(1)
    queue_obj.enQueue(34)
    queue_obj.enQueue(56)
    
    print("After adding elements to queue:")
    queue_obj.display_queue() 
    print("\nThe topmost element:",queue_obj.peek())

    queue_obj.deQueue() # Poping a value from the queue.
    queue_obj.deQueue() # Poping a value from the queue.

    print("After deleting elements from the queue:")
    queue_obj.display_queue()
    print("\nThe topmost element: ",queue_obj.peek())

    print("Is the queue empty?:",queue_obj.isEmpty())
    print("Size of the queue:", queue_obj.size())
    return None

if __name__ == "__main__":
    main()