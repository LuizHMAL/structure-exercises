 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def insert(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def return_kth_to_last(head, k):
    if head is None or k< 1:
        return None
    current = head
    runner = head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner is not None:
        current = current.next
        runner = runner.next
    return current  
 
