# head = {
#     "value":1,
#     "next":{
#         "value":2,
#         "next": None
#     }
# }

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        return f"Node({self.value})"
    
class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def prepend(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
            
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    
    def pop(self) -> Node:
        if self.head is None:
            return None
        
        #If we have one element
        if self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
            
        temp = self.head
        pre = self.head
        
        while(temp.next):
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        return temp
    
    def pop_first(self) -> Node:
        if self.head is None:
            return None
        
        temp = self.head
        
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        self.head = self.head.next
        self.length -= 1
        temp.next = None
        
        return temp
    
    def get_by_index(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
        return temp
    
    def set_value(self, index: int, value: int) -> bool:
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        return False    
    
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get_by_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        
        return True
    
    def remove(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_by_index(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        
        return temp
    
    def reverse(self) -> None:
        temp = self.head
        self.head = self.tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    

ll = LinkedList(4)
ll.append(5)
ll.append(6)

print(ll.get_by_index(1))
ll.set_value(1, 9)
print(ll.get_by_index(1))

ll.insert(1, 10)
ll.print()
print("****")
ll.reverse()
ll.print()




