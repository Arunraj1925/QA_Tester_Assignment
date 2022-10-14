class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedlList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def add_node(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current

def cyclic_check(llist):
    slow = llist.head
    fast = llist.head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


cllist = CircularLinkedlList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    cllist.add_node(int(data))
 
length = len(data_list)

if length == 0:
    print('The linked list is cyclic: True')
    
else:
    pos = input('Enter the index of element between [0-'+str(length - 1)+'] to point POS=  ').strip()
    if int(pos) >= length:
        print('Entered position ['+pos+'] is not available in linked list')
               
    elif pos == '' or int(pos) < 0 :
        pos = None
        if cyclic_check(cllist):
            print('The linked list is cyclic: True')
        else:
            print('The linked list is not cyclic: False')
        
    else:
        pos = cllist.get_node(int(pos))
        cllist.last_node.next = pos
        if cyclic_check(cllist):
            print('The linked list is cyclic: True')
        else:
            print('The linked list is not cyclic: False')




