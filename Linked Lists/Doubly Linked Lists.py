class Node:
    
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)

class DoublyLL():
    
    def __init__(self):
        self.head = None
        
    def TraverseForward(self):
        curr = self.head
        
        if curr == None:
            print("Linked List is empty")
            return
        while curr:
            print(curr, end=" ")
            curr = curr.next
        print()
    
    def TraverseBack(self):
        curr = self.head
        
        if curr == None:
            print("Linked list is empty")
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr, end=" ")
            curr = curr.prev
        print()
    
    def Display(self):
        curr = self.head
        elements = []
        if curr == None:
            return "Linked List is empty"
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(elements)
    
    def Search(self, val):
        curr = self.head
        if curr == None:
            return "Linked List is empty"
        while curr:
            if val == curr.data:
                return f"Value, {val} Found"
            curr = curr.next
        return f"Value, {val} not found"
        
    
    def InsertStart(self, val):
        curr = self.head
        value = Node(val)
        if curr == None:
            self.head = value
            return
        value.next = self.head
        self.head = value
        curr.prev = value
    
    def InsertEnd(self, val):
        curr = self.head
        value = Node(val)
        if curr == None:
            print("Linked List is empty")
            return
        if curr.next == None:
            curr.next = value
            value.prev = curr
            return
        
        while curr.next:
            curr = curr.next
        value.prev = curr
        curr.next = value
        
    
    def Insert(self, val, pos):
        value = Node(val)
        curr = self.head
        nextval = curr.next
        if curr == None:
            print("Linked List is empty")
            return
        if nextval == None:
            print("Linked list only has one node")
            return
        
        
        index = 0
        while nextval:
            if index == pos - 1:
                curr.next = value
                value.prev = curr
                value.next = nextval
                return
            elif index == pos:
                value.next = self.head
                curr.prev = value
                self.head = value
            nextval = nextval.next
            curr = curr.next
            index += 1
            
        if pos > index or pos < 0:
            print("Invalid position")
            return
        
        
                        
    
    def DeleteHead(self):
        curr = self.head
        if curr == None:
            print("Linked List is empty")
            return
        self.head = curr.next
        
          
    def DeleteTail(self):
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
        
    
    def Delete(self, pos):
        curr = self.head
        nextval = curr.next
        
        if curr == None:
            print("Linked List is empty")
            return
        if nextval == None:
            print("Linked list only has one node")
            return
        if pos == 0:
            nextval.prev = None
            self.head = nextval
            return
        
        index = 0
        while nextval:
            if index == pos - 1:
                curr.next = None
                return
            nextval = nextval.next
            curr = curr.next
            index += 1
        
        if pos > index or pos < 0:
            print("Invalid position")
            return
        
        
    
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.next = B
B.prev = A
B.next = C
C.prev = B
C.next = D
D.prev = C
D.next = E
E.prev = D
E.next = F
F.prev = E

Dll = DoublyLL()
Dll.head = A
print(Dll.Display())
# Dll.TraverseBack()
# Dll.Delete(0)
# Dll.DeleteHead()
# Dll.DeleteTail()
# print(Dll.Search(3))
# Dll.InsertStart(8)
# Dll.Insert(7, 0)
print(Dll.Display())