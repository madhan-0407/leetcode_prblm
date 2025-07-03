#Node definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Insert at end
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=Node(self,data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last=new_node
#Insert at Beginning
    def insert_begin(self,data):
        new_node=Node(self,data)
        new_node.next=self.head
        self.head=new_node
# Insert at a Specific Position
    def 
