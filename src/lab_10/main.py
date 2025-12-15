from src.lab_10.linked_list import SinglyLinkedList
from src.lab_10.structures import Stack, Queue

def linked_list_example():
    print("\n--- SinglyLinkedList Example ---")
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("List after appending 10, 20, 30:", ll.plotter())

    ll.prepend(5)
    print("List after prepending 5:", ll.plotter())

    ll.insert(2, 15)
    print("List after inserting 15 at index 2:", ll.plotter())

    ll.remove_at(1)
    print("List after removing element at index 1:", ll.plotter())


def stack_example():
    print("\n--- Stack Example ---")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", [stack._data])

    print("Popped element:", stack.pop())
    print("Stack after popping:", [stack._data])

    print("Top element (peek):", stack.peek())

def queue_example():
    print("\n--- Queue Example ---")
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue after enqueuing A, B, C:", list(queue._data))

    print("Dequeued element:", queue.dequeue())
    print("Queue after dequeuing:", list(queue._data))

    print("Front element (peek):", queue.peek())

if __name__ == "__main__":
    linked_list_example()
    stack_example()
    queue_example()