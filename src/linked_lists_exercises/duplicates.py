class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

def delete(head, key):
    current = head
    previous = None
    while current is not None:
        if current.data == key:
            if previous is None:
                head = current.next
            else:
                previous.next = current.next
            return head
        previous = current
        current = current.next
    return head

def delete_duplicates(head):
    current = head
    seen = set()
    previous = None
    while current is not None:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next
    return head



def delete_duplicates_bufferless(head):
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

list = [1, 2 , 2, 4, 5, 5, 3, 6] 
head = None
for item in list:
    head = insert(head, item)
print_list(head)

head = delete_duplicates(head)
print_list(head)

head = delete_duplicates_bufferless(head)
print_list(head)

print(head)
'''uv run src\linked_lists_exercises\duplicates.py para rodar o programa
'''