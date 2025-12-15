from collections import deque
from typing import Optional

class Stack: # LIFO data-structure - bigO: O(1) for any class-method
    def __init__(self):
        # internal storage for the stack
        self._data = []

    def push(self, item) -> None:
        """Add an element to the top of the stack."""
        self._data.append(item)

    def pop(self) -> any:
        """
        Remove the top element of the stack and return it.
        If the stack is empty — raise an IndexError with a clear message.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[any]:
        """
        Return the top element without removing it.
        If the stack is empty — return None.
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack is empty, otherwise False."""
        return not self._data

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self._data)


class Queue: # O(1) data structure --> basic principle FIFO
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        """Add an element to the end of the queue."""
        self._data.append(item)

    def dequeue(self) -> any:
        """
        Remove and return the first element of the queue.
        If the queue is empty — raise IndexError with a clear message.
        """
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._data.popleft()

    def peek(self) -> Optional[any]:
        """
        Return the first element without removing it.
        If the queue is empty — return None.
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Return True if the queue is empty, otherwise False."""
        return not self._data
    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)