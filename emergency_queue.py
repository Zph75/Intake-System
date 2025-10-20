class Patient:
    def __init__(self, name, urgency):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(urgency, int):
            raise TypeError("urgency must be an integer")
        if urgency < 1 or urgency > 10:
            raise ValueError("urgency must be in range 1..10 (1 = most urgent)")
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"Patient({self.name!r}, urgency={self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    # index helpers
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2
    
    def heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.data[index].urgency < self.data[parent].urgency:
                # swap child and parent
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index

            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("insert expects a Patient instance")
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        n = len(self.data)
        if n == 0:
            return None
        if n == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root



if __name__ == "__main__":
    # Basic usage
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    # Expected: Taylor (1) at root

    # peek
    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)  # Taylor 1

    served = heap.remove_min()
    print("Served:", served.name)  # Taylor
    heap.print_heap()  # Jordan and Avery remain


    heap.insert(Patient("Casey", 2))
    heap.insert(Patient("Riley", 4))
    heap.print_heap()

    served_order = []
    while True:
        p = heap.remove_min()
        if p is None:
            break
        served_order.append((p.name, p.urgency))
    print("Served order:", served_order)


    empty_heap = MinHeap()
    assert empty_heap.peek() is None, "peek on empty should be None"
    assert empty_heap.remove_min() is None, "remove_min on empty should be None"

    try:
        heap.insert("not a patient")
    except TypeError as e:
        print("Caught expected TypeError for bad insert:", e)

    try:
        Patient("BadUrgency", 0)  # invalid urgency
    except ValueError as e:
        print("Caught expected ValueError for bad urgency:", e)

    print("All tests completed successfully.")