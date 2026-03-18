# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class LinkedList:

    def __init__(self, head):
        self.head = head
            
    def append(self, data):
        new_node = Node(data)
        prev_node = self.head
        if self.head == None:
            self.head = new_node
        while prev_node.next != None:
            prev_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

    def insert(self, data, cursor):
        new_node = Node(data)
        prev_node = self.head
        if cursor == 0:
            new_node.next = prev_node
            prev_node.prev = new_node
            self.head = new_node
        else:
            for _ in range(cursor - 1):
                prev_node = prev_node.next
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node

    def delete(self,cursor):
        pprev_node = self.head
        current_node = self.head
        for _ in range(cursor - 2):
            pprev_node = pprev_node.next
        for _ in range(cursor):
            current_node = current_node.next
        pprev_node.next = current_node
    

def L(cursor):
    if cursor > 0:
        cursor -= 1
    return cursor
def D(cursor):
    if cursor < n:
        cursor += 1
    return cursor
def B(cursor, command):
    if cursor > 0:
        command.delete(cursor)
        cursor -= 1
def P(cursor, str):
    command.insert(str, cursor)

command_list = {
    "L" : L,
    "D" : D,
    "B" : B,
    "P" : P
}

command = LinkedList()
