"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            newNode = ListNode(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            oldNode = self.head
            self.head = ListNode(value, oldNode, value)
            self.head.next = oldNode
            self.head.prev = ListNode(value, oldNode, value)
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            removedNode = self.head.value
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return removedNode
        else:
            removedNode = self.head.value
            self.head = ListNode(self.head.prev, self.tail, self.head.prev)
            self.length = self.length - 1
            return removedNode
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            self.tail = ListNode(value)
            self.head = ListNode(value)
            self.length +=1
        else:
            self.tail = ListNode(value, self.tail, value)
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            self.tail = None
            self.head = None
            self.length = self.length -1
        else:
            removedTail = self.tail.value
            self.tail = ListNode(self.tail.prev, self.head, self.tail.prev)
            self.length = self.length - 1
            return removedTail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head.value is node:
            return
        else:
            oldValue = ListNode(self.head.value, self.head.prev, self.head.next)
            self.head.value = node.value
            self.head.next = oldValue
            self.head.prev = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail.value is node:
            return
        else:
            oldValue = ListNode(self.tail.value, self.tail.prev, self.tail.next)
            self.tail.value = node.value
            self.tail.prev = oldValue
            self.tail.next = node
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        previous_node = node.prev
        if previous_node is None:
            self.head = node.next
        else:
            previous_node.next = node.next
        next_node = node.next
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = previous_node
        self.length -= 1
        node.prev = None
        node.next = None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        current_max = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_max < current_node.value:
                current_max = current_node.value
            current_node = current_node.next
        return current_max