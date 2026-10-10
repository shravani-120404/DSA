class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

# 1. Create linked list
    def create(self,values):
        for x in values:
            self.insert(x,999)

# 2. Traverse and print
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")

 # 3. Insert at specific position 
    def insert(self,data,pos):
        new=Node(data)
        if pos==1 or self.head is None:
            new.next=self.head
            self.head=new
            return
        temp=self.head
        for _ in range(pos-2):
            if temp.next is None:
                break
            temp=temp.next
        new.next=temp.next
        temp.next=new

# 4. Find middle node
    def middle(self):
        slow=fast=self.head
        if not slow:
            print("List is empty")
            return
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("Middle:",slow.data)

 # 5. Delete node 
    def delete(self,value):
        temp=self.head
        if temp and temp.data==value:
            self.head=temp.next
            return
        while temp and temp.next:
            if temp.next.data==value:
                temp.next=temp.next.next
                return
            temp=temp.next
        print("Value not found")

 # 6. Reverse list
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

 # 7. Sum of every two consecutive nodes
    def pair_sum(self):
        temp=self.head
        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp=temp.next
        print()



ll=LinkedList()
ll.create(list(map(int,input("Enter values: ").split())))
print("List:")
ll.display()

ll.insert(int(input("Value to insert: ")),int(input("Position: ")))
ll.display()

ll.middle()

ll.delete(int(input("Value to delete: ")))
ll.display()

ll.reverse()
print("Reversed:")
ll.display()

print("Consecutive pair sums:")
ll.pair_sum()