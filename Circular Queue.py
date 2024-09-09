class CircularQueue:
    def __init__(self, size):  # Corrected __init__ method
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, element):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element
        print("Enqueued:", element)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print("Dequeued:", element)
        return element

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            if self.rear >= self.front:
                print("Queue elements:", self.queue[self.front:self.rear + 1])
            else:
                print("Queue elements:", self.queue[self.front:] + self.queue[:self.rear + 1])

    def display_front_rear(self):
        print("Front position:", self.front)
        print("Rear position:", self.rear)


def menu():
    size = int(input("Enter the size of the circular queue: "))
    cq = CircularQueue(size)

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Display Front and Rear Positions")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            element = int(input("Enter element to enqueue: "))
            cq.enqueue(element)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            cq.display_front_rear()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

menu()
