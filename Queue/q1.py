class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print("Deleted:", temp.data)
        else:
            print("Queue is empty")

    def print(self):
        temp = self.front

        while temp:
            print(temp.data, end="  ")
            temp = temp.next

        print()


q = Queue()

q.enqueue(Node(15))
q.enqueue(Node(25))
q.enqueue(Node(30))
q.enqueue(Node(45))
q.enqueue(Node(40))

print("Queue elements:")
q.print()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

print("Queue after dequeue:")
q.print()