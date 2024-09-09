class LinearQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f"Inserted {item}")
            self.display_front_rear()

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
        else:
            item = self.queue[self.front]
            print(f"Deleted {item}")
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            self.display_front_rear()

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue contents:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
            self.display_front_rear()

    def display_front_rear(self):
        print(f"Front: {self.front}, Rear: {self.rear}")


def main():
    queue_size = int(input("Enter the size of the queue: "))
    queue = LinearQueue(queue_size)
    
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = int(input("Enter the item to insert: "))
            queue.enqueue(item)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
