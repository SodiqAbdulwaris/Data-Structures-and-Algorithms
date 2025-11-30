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
        value = Node(val)
        curr = self.head
        curr.prev = value
        value.next = curr
        self.head = value
    
    def InsertEnd(self, val):
        curr = self.head
        value = Node(val)
        while curr.next:
            curr = curr.next
        curr.next = value
        value.prev = curr
        
    
    def Insert(self, val, pos):
        curr = self.head
        value = Node(val)
        
        if pos == 0:
            if self.head:           
                self.head.prev = value
            value.next = self.head
            self.head = value
            return
        
        for _ in range(pos - 2):
            if curr is None:
                print("Invalid position")
                return
            curr = curr.next
        nextcurr = curr.next
        curr.next = value
        value.prev = curr
        value.next = nextcurr
        if nextcurr is not None:
            nextcurr.prev = value
        

    def DeleteHead(self):
        curr = self.head
        
        if self.head is None:
            print("Linked List is empty")
            return
        if curr.next is not None:
            curr.next.prev = None 
            self.head = curr.next
        else:
            self.head = None
        
          
    def DeleteTail(self):
        curr = self.head
        
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        
    
    def Delete(self, pos):
        curr = self.head
        
        if self.head is None:
            print("Linked List is empty")
            return
        if pos == 0:
            if curr.next is not None:
                curr.next.prev = None 
            self.head = curr.next
            return
        
        index = 1
        while curr and index < pos:
            if curr.next is None:
                print("Invalid position")
                return
            curr = curr.next
            index += 1
            
        if curr.next is not None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            curr.prev.next = curr.next
            
   
   
       
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
# Dll.Traverse(3)
# Dll.TraverseBack()
Dll.Delete(6)
# Dll.DeleteHead()
# Dll.DeleteTail()
# print(Dll.Search(3))
# Dll.InsertStart(8)
# Dll.InsertEnd(9)
# Dll.Insert(7, 7)
print(Dll.Display())