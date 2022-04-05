from collections import deque
class Queue:
    #Initializing the queue
    def __init__(self, data) -> None:
        self.items = deque([data])

    #Returning the length of the queue
    def __len__(self):
        return len(self.items)
    
    #Printing the queue
    def __str__(self) -> str:
        return str(self.items)

    #Adding element to the queue
    def enqueue(self, data) -> None:
        self.items.append(data)
        print("Enqueued:", data)

    #Removing element from the queue
    def dequeue(self) -> None:
        if self.items == deque():
            print("Queue is empty")
        else:
            self.items.popleft()
            print("Dequeued:", self.items)

    # #Printing the queue
    # def print_queue(self) -> None:
    #     print(self.items)

if __name__ == "__main__":
    q1 = Queue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.enqueue(40)
    q1.dequeue()
    print(q1)
    print(len(q1))
    q1.dequeue()
    print(q1)