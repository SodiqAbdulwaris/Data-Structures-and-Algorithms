class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class SinglyLL:
    
    def __init__(self):
        self.head = None
    
    # Traverse linked link
    def Traverse(self):
        curr = self.head
        
        if curr == None:
            print("Linked List is empty")
        else:
            while curr:
                print(curr, end=" ")
                curr = curr.next
            print()
    
    # Display linked list
    def Display(self):
        curr = self.head
        elements = []
        if curr == None:
            return "Linked List is empty"
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " -> ".join(elements)
    
    # Search for an element
    def Search(self, val):
        curr = self.head
        if curr == None:
            return "Empty"
        while curr:
            if val == curr.data:
                return f"Value,{val} found"
            curr = curr.next
        return f"Value,{val} not found"
    
    # Insert at beginning
    def InsertStart(self, val):
        curr = self.head
        value = Node(val)
        value.next = curr
        self.head = value
    
    # Insert at end
    def InsertEnd(self, val):
        value = Node(val)

        if self.head is None:
            self.head = value
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = value

        
                    

    # Insert element at position
    def Insert(self, val, pos):
        value = Node(val)

        # Insert at head
        if pos == 0:
            value.next = self.head
            self.head = value
            return

        curr = self.head
        index = 0

        while curr and index < pos - 1:
            curr = curr.next
            index += 1

        if curr is None:
            print("Invalid position")
            return

        value.next = curr.next
        curr.next = value

            
        
    
    # Delete at the beginning
    def DeleteHead(self):
        curr = self.head
        if curr == None:
            print("Linked list is empty")
            return
        if curr.next == None:
            print("Linked list only has one node")
        self.head = curr.next
    
    # Delete last element
    def DeleteLast(self):
        curr = self.head
        
        if curr == None:
            print("Linked list is empty")
            return
        if curr.next == None:
            print("Linked list only has one node")
            return
        
        while curr.next.next:
            curr = curr.next
        curr.next = None
    
    # Delete at a location, pos <Starts counting at 0>
    def Delete(self, pos):
        curr = self.head
        nextval = curr.next
        
        if curr == None:
            print("Linked list is empty")
            return
        if nextval == None:
            print("Linked list only has one node")
            return
        
        if pos == 0:
            self.head = nextval
            return
        
        index = 0
        while nextval:
            if index == pos - 1:
                curr.next = nextval.next
                return
            nextval = nextval.next
            curr = curr.next
            index += 1
        
            
        if pos > index or pos < 0:
            print("Invalid position")
            return
            
     

Head = Node(1)
A = Node(3)
B = Node(4)
C = Node(8)
D = Node(9)
E = Node(10)

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = E

Sll = SinglyLL()
Sll.head = Head
# Sll.Traverse()
print(Sll.Display())
# print(Sll.Search(20))
# Sll.DeleteHead()
Sll.DeleteLast()
# Sll.Delete(6)
# print(Sll.Display())
# Sll.InsertEnd(7)
# Sll.InsertStart(7)
# Sll.Insert(0, 8)
print(Sll.Display())    
        
