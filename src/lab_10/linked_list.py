class Node:
    def __init__(self, value, next=None):
        # Node of a singly linked list:
        # value — stored element
        # next — reference to the next node, or None if this is the last node
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        # Head of the list (first node), or None if the list is empty
        self.head = None
        # Number of elements in the list
        self._size = 0

    def append(self, value):
        """Add an element to the end of the list."""
        new_node = Node(value)

        # If the list is empty — new node becomes the head
        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        # Traverse to the end of the list (O(n))
        current = self.head
        while current.next is not None:
            current = current.next

        # Append the new node
        current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Add an element to the beginning of the list (O(1))."""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Insert an element at index idx."""
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        # Insertion at the beginning
        if idx == 0:
            self.prepend(value)
            return

        new_node = Node(value)

        # Traverse to the node BEFORE the insertion position
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # safe because idx <= size

        # Insert the node
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        """Remove node at index idx."""
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        # Removing the head
        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return

        # Traverse to node BEFORE the one we remove
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        # Skip the node being removed
        current.next = current.next.next
        self._size -= 1

    def __iter__(self):
        """Iterate over values from head to tail."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        """Return number of elements in the list."""
        return self._size

    def __repr__(self):
        """Formal string representation."""
        values = list(self)
        return f"SinglyLinkedList({values})"

    def plotter(self):
        """Return a readable linked-list-like representation."""
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)