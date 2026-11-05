class Node:
    def __init__(self, data):
        self.data  = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def push_front(self, a):
        new_node = Node(a)
        if self.cnt == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.cnt += 1
    
    def push_back(self, a):
        new_node = Node(a)
        if self.cnt == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.cnt += 1

    def pop_front(self):
        if self.head == None:
            print("empty list")
        elif self.cnt == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.cnt -= 1
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.cnt -= 1
            return temp

    def pop_back(self):
        if self.tail == None:
            print("empty list")
        elif self.cnt == 1:
            temp = self.tail.data
            self.head = None
            self.tail = None
            self.cnt -= 1
            return temp
        else:
            temp = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.cnt -= 1
            return temp

    def size(self):
        return self.cnt

    def empty(self):
        if self.cnt == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.cnt == 0:
            return "empty list"
        else:
            return self.head.data
    
    def back(self):
        if self.cnt == 0:
            return "empty list"
        else:
            return self. tail.data

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

link = DoublyLinkedList()

for i in range(N):
    if command[i] == "push_front":
        link.push_front(A[i])
    elif command[i] == "push_back":
        link.push_back(A[i])
    elif command[i] == "pop_front":
        print(link.pop_front())
    elif command[i] == "pop_back":
        print(link.pop_back())
    elif command[i] == "size":
        print(link.size())
    elif command[i] == "empty":
        print(link.empty())
    elif command[i] == "front":
        print(link.front())
    elif command[i] == "back":
        print(link.back())