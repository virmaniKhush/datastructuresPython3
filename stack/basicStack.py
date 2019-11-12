MAX_SIZE = 100
class Stack():
    def __init__(self, top=-1, stack=[0 for kx in range(MAX_SIZE)]):
        self.top = top
        self.stack = stack

    def push(self, val):
        self.top +=1
        self.stack[self.top] = val

    def pop(self):
        pop_elem=self.stack[self.top]
        self.top-=1
        return pop_elem

    def stackPrinter(self):
        counter = self.top
        while counter >= 0:
            print(self.stack[counter])
            counter-=1

    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return self.top==MAX_SIZE-1


stack1 = Stack()
print("stack1 empty: ", stack1.isEmpty())
print("Input 5 numbers into stack:")
for kx in range(5):
    inp = int(input())
    stack1.push(inp)
print("stack1:")
stack1.stackPrinter()
val = stack1.pop()
print("stack1 after 1 pop:")
stack1.stackPrinter()
print("stack1 full:", stack1.isFull())
print("stack1 empty:", stack1.isEmpty())



