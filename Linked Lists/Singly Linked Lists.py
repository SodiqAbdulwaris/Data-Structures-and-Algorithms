
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
        curr = self.head
        nextval = curr.next
        value = Node(val)
        
        # If linked list is empty
        if curr == None:
            print("List is empty")
            return
        # If linked list has only one value
        if nextval == None:
            curr.next = value
            return
        
        while nextval:
            curr.next = nextval
            nextval = nextval.next
            curr = curr.next
        curr.next = value
        
                    

    # Insert element at position
    def Insert(self, val, pos):
        curr = self.head
        nextval = curr.next
        value = Node(val)
        
        if curr == None:
            print("List is empty")
            return
        if nextval == None:
            print("Linked list only has one node")
            return
        if pos == 0:
            value.next = curr
            self.head = value
            return
        
        index = 0
        while nextval:
            if index == pos - 1:
                curr.next = value
                value.next = nextval
                return
            nextval = nextval.next
            curr = curr.next
            index += 1
        if nextval == None:
            curr.next = value
            index += 1
            
        if pos > index or pos < 0:
            print("Invalid position")
            return
            
        
    
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
        nextval = curr.next
        
        if curr == None:
            print("Linked list is empty")
            return
        if nextval == None:
            print("Linked list only has one node")
            return
        
        while nextval.next:
            nextval = nextval.next
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
# Sll.DeleteLast()
# Sll.Delete(6)
print(Sll.Display())
Sll.InsertEnd(7)
Sll.InsertStart(7)
Sll.Insert(0, 8)
print(Sll.Display())    
        
