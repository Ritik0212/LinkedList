class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

  
    def isEmpty(func):
        def inner(self, *args, **kwargs):
            flag = self.head is None
            if flag:
                print('Empty')
                return 0
            x = func(self, *args, **kwargs)
            return x
        return inner

  
    def checkEmptyForOperation(func):
        def inner(self, *args, **kwargs):
            flag = self.head is None
            if flag:
                print('This operation is not allowed on Empty LL')
                return 0
            x = func(self, *args, **kwargs)
            return x
        return inner

      
    def printBeforeAfterLL(func):
        def wrap(self, *args, **kwargs):
            print("==========================================")
            print('Linked List before operation:', end=' ')
            self.printLL()
            x = func(self, *args, **kwargs)
            print('Linked List after operation:', end=' ')
            self.printLL()
            print("==========================================")
            return x
        return wrap

  
    @printBeforeAfterLL
    def insertAtBegin(self, data):
        head_node = Node(data)
        
        if self.head is not None:
            head_node.next = self.head
            self.head = head_node
        else:
            self.head = head_node
        print(f'Inserted at Beginning: {data}')

  
    @printBeforeAfterLL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        print(f'Inserted at End: {data}')

  
    @printBeforeAfterLL
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        new_node = Node(data)
        i = 0
        current_node = self.head

          
        while i != index - 1 and current_node:
            current_node = current_node.next
            i += 1
          
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
            print(f'Inserted data {data} at Index: {index}')
        else:
            print('Given index is out of range for this linked list')
    
  
    @printBeforeAfterLL
    @checkEmptyForOperation
    def updateNode(self, data, index):
        i = 0
        current_node = self.head

        if index == 0:
            current_node.data = data
            print(f'Updated Node at index {index} with data {data}')
            return
          
        while i != index and current_node:
            current_node = current_node.next
            i += 1
        if current_node:
            print(f'Updated Node at index {index} with data {data}')
            current_node.data = data
        else:
            print('Given index is out of range for this linked list')

  
    @printBeforeAfterLL
    @checkEmptyForOperation
    def removeFirstNode(self):
        # if self.head:
        self.head = self.head.next
        print('Removed first Node')
        return

    @printBeforeAfterLL
    @checkEmptyForOperation
    def removeLastNode(self):        
        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None
        print('Removing Last Node')
        return

  
    @printBeforeAfterLL
    @checkEmptyForOperation
    def removeNodeFromIndex(self, index):
        if index == 0:
            self.removeFirstNode()
            return
          
        current_node = self.head
        i = 0
          
        while i != index - 1 and current_node:
            current_node = current_node.next
            i += 1
        if current_node:
            if current_node.next:
                current_node.next = current_node.next.next
                print(f'Removed node from index: {index}')
            else:
                self.removeLastNode()
            return
        print('Given index is out of range for this linked list')
            

    @printBeforeAfterLL
    @checkEmptyForOperation
    def removeNodeWithGivenData(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            print(f'Removed node with data: {data}')
            return
        if current_node.next is None:
            if current_node.data == data:
                print(f'Removed node with data: {data}')
                self.head = None
            else:
                print('Node was not found with given data')
            return
            
        while current_node.next.data != data:
            current_node = current_node.next
            if current_node.next is None:
                print('Node was not found with given data')
                return
        if current_node.next.next:
            current_node.next = current_node.next.next
        else:
            current_node.next = None
        print(f'Removed node with data: {data}')

  
    @isEmpty
    def sizeOfLL(self):
        current_node = self.head
        i = 0
        while current_node:
            current_node = current_node.next
            i += 1
        print(f'Size of Linked List is {i}')
        return i

  
    @isEmpty
    def printLL(self):
        current_node = self.head
        print('##', end=' ')
        while current_node:
            print(current_node.data, end=' ')
            if current_node.next:
                print('->', end=' ')
            current_node = current_node.next
        print("##")


llist = LinkedList()


llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

llist.removeFirstNode()
llist.removeLastNode()
llist.removeNodeFromIndex(1)

llist.updateNode('z', 0)

llist.sizeOfLL()