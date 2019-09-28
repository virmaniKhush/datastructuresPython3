class Node():
    def __init__(self, data= None, next=None):
        self.data =  data
        self.next = next

class SinglyLinkedList():
    def __init__(self, head):
        self.head = head
        self.current = head

    def insertAtEend(self, inp_data):
        tmp_node = Node(inp_data)
        if self.head.next is None:
            self.head.next = tmp_node
            self.current = tmp_node

        else:
            self.current.next = tmp_node
            self.current = tmp_node


    def insertAtBegin(self, inp_data):
        tmp_node = Node(inp_data)
        tmp_node.next = self.head
        self.head = tmp_node


    def llPrinter(self):   # also the traversal
        ll_node = self.head
        while ll_node.next is not None:
            print("Current Node : ", ll_node, "\nData in node : ", ll_node.data, "\nNext Node : ", ll_node.next, "\n\n")
            ll_node = ll_node.next
        print("Current Node : ", ll_node, "\nData in node : ", ll_node.data, "\nNext Node : ", ll_node.next, "\n\n")


    def llDeletion(self, to_delete):
        ll_node = self.head
        while ll_node.next is not None:
            if ll_node.data == to_delete:
                if ll_node == self.head:
                    self.head=None
                else:
                    prev.next = ll_node.next
                break
            prev = ll_node
            ll_node = ll_node.next


head1 = Node(2)
ll1 = SinglyLinkedList(head1)
ll1.insertAtEend(3)
ll1.insertAtEend("Anything")
ll1.insertAtEend(5)
ll1.insertAtEend("You SUCK !")
ll1.insertAtEend("I'm the last node.")
ll1.llPrinter()
a = ll1.insertAtBegin("Now i'm the first node !")
ll1_updated  = ll1.llDeletion(5)
ll1.llPrinter()
