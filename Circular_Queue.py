class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.max_length = max_length
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear and not self.queue

    def is_full(self):
        return (self.rear + 1) % self.max_length == self.front

    def enqueue(self, element):
        if self.is_full():
            # If the queue is full, delete the latest added element
            deleted_element = self.queue[self.front]
            del self.queue[self.front]
            self.front = (self.front + 1) % self.max_length
            print(f"Queue is full. Deleting element: {deleted_element}")

        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.max_length

    def display_queue(self):
        print("Circular Queue:", list(self.queue.values()))


# Example usage:
cq = CircularQueue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display_queue()

cq.enqueue(6)  # This will exceed the maximum length, deleting the oldest element (1)
cq.display_queue()