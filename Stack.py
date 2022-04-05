from collections import deque

class Stack:
    #Initializing the stack
    def __init__(self, data=None):
        self.items = deque([data])
    #Checking if the stack is empty
    def check_empty(self):
        return self.items == deque()
    #Pushing an element to the stack
    def push(self, data):
        self.items.append(data)
        print("Pushed:", data)
    #Popping an element from the stack
    def pop(self):
        if self.check_empty() == True:
            print("Stack is empty")
             

        self.items.pop()

    #Printing the stack
    def __repr__(self):
        return str(self.items)
    #Checking the length of the stack
    def __len__(self):
        return len(self.items)
    #Returning the top element of the stack
    def top_element(self):
        return self.items[-1]

def main():
    s1 = Stack(45)
    print(s1.check_empty())
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.pop()
    print(s1)
    print(len(s1))
    print(s1.top_element())

if __name__ == "__main__":
    main()

    