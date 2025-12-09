class Node:
    def __init__(self,node,next=None):
        self.node=node
        self.next=next

### A LINKED LIST CLASS TO MANAGE NODES WITH METHODS TO ADD NODE, PRINT LIST AND DELETE nth NODE
class Singly_linkedlist:
    def __init__(self):
        self.head=None

    def add_node (self,node):
        new_node=Node(node)
        if self.head is None:
            self.head=new_node
            return
        
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node

    def print_list(self):
        if self.head is None:
            print("The Linked list is empty.")
            return
 
        print_node=self.head
        while print_node:
            print(print_node.node,end="--> ")
            print_node=print_node.next
        print("end")
    
    def delete_nth_node(self,delete_index):
        ### RAISE EXCEPTIONS
        if self.head is None:
            raise Exception("Can not delete from an empty list")
        if delete_index<=0:
            raise Exception("The Index should be positive integer")
        
        if delete_index==1:
            self.head=self.head.next
            return
        
        current_node=self.head
        count=1
        node_before=None

        while current_node and count < delete_index:
            node_before=current_node
            current_node=current_node.next
            count+=1
        if not current_node:
            raise Exception("The Index is out of range")
        node_before.next=current_node.next

### CREATING A SAMPLE LINKED LIST
my_list=Singly_linkedlist()

my_list.add_node(2)
my_list.add_node(4)
my_list.add_node(8)
my_list.add_node(10)
my_list.add_node(12)
my_list.add_node(14)

print("THE LINKED LIST IS:")
my_list.print_list()

### DELETING THE FIRST NODE
try:
    my_list.delete_nth_node(1)
    print("\nList after deleting the 1st node:")
    my_list.print_list()
except Exception as e:
        print(f"Error: {e}")

### DELETING NODE OUT OF RANGE, EMPTY LIST AND NEGATIVE INDEX
try:
    my_list.delete_nth_node(10)
except Exception as e:
    print(f"\nError while deleting the 10th term: {e}")

try:
    empty_list = Singly_linkedlist()
    empty_list.delete_nth_node(1)
except Exception as e:
    print(f"\nError while deleting from empty list: {e}")

try:
    my_list.delete_nth_node(-2)
except Exception as e:
    print(f"\nError while deleting the -2nd term: {e}")

### DELETION WITH INPUT
while True:
    try:
        index = int(input("\nEnter the index to delete (1-based):"))
        my_list.delete_nth_node(index)
        print("List after deletion:")
        my_list.print_list()
    except Exception as e:
        print(f"Error: {e}")

    continue_deleting = input("Do you want to continue deleting node? (y/n):").strip().lower()
    if continue_deleting != 'y':
        print("Exiting deletion, see you in the next assignment!")
        break
