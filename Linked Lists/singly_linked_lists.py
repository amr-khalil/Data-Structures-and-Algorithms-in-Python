class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Insertion at the end
    def append(self, data):
        new_node = Node(data)

        # Empty Linked List Case
        if self.head is None:
            self.head = new_node
            return
        
        # Non-empty Linked List Case
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    # Insertion at the beginning
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node

    # Insertion after a node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous Node dosn't exist")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deletion by Value
    def delete_node(self, key):
        cur_node = self.head

        # Case of Deleting Head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case of Deleting Node Other Than the Head
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    # Deletion by Position
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

        prev.next = cur_node.next
        cur_node = None

    # Length
    def length_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    # Recursive Implementation
    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    # Swap Nodess   
    def swap_nodes(self, key_1, key_2):

            if key_1 == key_2:
                return 

            prev_1 = None 
            curr_1 = self.head 
            while curr_1 and curr_1.data != key_1:
                prev_1 = curr_1 
                curr_1 = curr_1.next

            prev_2 = None 
            curr_2 = self.head 
            while curr_2 and curr_2.data != key_2:
                prev_2 = curr_2 
                curr_2 = curr_2.next

            if not curr_1 or not curr_2:
                return 

            if prev_1:
                prev_1.next = curr_2
            else:
                self.head = curr_2

            if prev_2:
                prev_2.next = curr_1
            else:
                self.head = curr_1

            curr_1.next, curr_2.next = curr_2.next, curr_1.next
            
            
if __name__ == '__main__':
    myList = LinkedList()
    myList.append('A')
    myList.append('B')
    myList.append('C')
    myList.append('D')

    # myList.prepend('#')
    # myList.insert_after_node(myList.head, '#')

    # myList.delete_node("A")
    # myList.delete_node("D")
    # myList.delete_node_at_pos(0)

    myList.print_list()
    myList.length_recursive(myList.head.next)
    
