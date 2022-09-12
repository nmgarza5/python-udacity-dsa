"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

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

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # 1) set current as the head
        # 2) set my current position as 0 if there is no head or 1 otherwise
        # 3) while our current position is not our target position and while we have a current (list is not empty)
        # 4) and if there is a next position, move current to current.next and increment position. if this is target position, return
        # 5) if there is no next position, we are at the end of the list
        current = self.head
        current_position = 1

        while current_position <= position:
            if current_position == position:
                return current
            elif current.next:
                current = current.next
                current_position += 1
            else:
                break
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        current_position = 1

        while current_position < position:
            if current_position == position-1:
                temp = current.next
                new_element.next = temp
                current.next  = new_element
                return
            else:
                current = current.next
                current_position += 1


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        current_position = 1

        while current:
            if current.value == value and current_position == 1:
                self.head = current.next
                return
            elif current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


    def print(self):
        current = self.head
        ll = []
        while current:
            ll.append(current.value)
            if current.next == None:
                break
            current = current.next
        print(ll, '-- list')

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
ll = LinkedList(e1)
test = LinkedList(a1)
ll.append(e2)
ll.append(e3)


test.append(a2)
test.append(a3)
test.append(a4)
test.append(a5)
test.append(a7)
test.append(a8)


test.print()
test.insert(a6,6)
test.print()

test.delete(2)
test.print()

# Test get_position
# Should print 3
# print(ll.head.next.next.value)
# Should also print 3
# print(ll.get_position(3).value)

# Test insert
# ll.insert(e4,3)
# # Should print 4 now
# # print(ll.get_position(3).value)
# # print(ll.get_position(2).value)

# # should print 1, 2, 4, 3
# # ll.print()

# # # Test delete
# ll.print()
# ll.delete(1)
# print("-----")
# ll.print()
# print("-----")
# # # Should print 2 now
# print(ll.get_position(1).value, '-- position 1')
# # # Should print 4 now
# print(ll.get_position(2).value, '-- position 2')
# # Should print 3 now
# print(ll.get_position(3).value, '-- position 3')
