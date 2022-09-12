"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        temp = self.head
        self.head = new_element
        new_element.next = temp

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        temp = self.head
        next = self.head.next
        self.head = next
        return temp

    def print(self):
        current = self.head
        ll = []
        while current:
            ll.append(current.value)
            if current.next == None:
                break
            current = current.next
        print(ll, '-- list')

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.ll.head:
            return self.ll.delete_first()
        else: return

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

a1 = Element(1)
a2 = Element(2)
a3 = Element(3)
a4 = Element(4)
a5 = Element(5)
a6 = Element(6)
a7 = Element(7)
a8 = Element(8)

# Start setting up a LinkedList
test = LinkedList(a1)

test.append(a2)
test.append(a3)
test.append(a4)
test.print()
test.insert_first(a5)
test.insert_first(a6)
test.print()
test.delete_first()
test.delete_first()
test.print()

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
stack.ll.print()
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
stack.ll.print()
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
