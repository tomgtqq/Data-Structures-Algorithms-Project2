class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if self and other:
            return self.value == other.value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            if cur_head.next:
                arrows = " -> "
            else:
                arrows = ""
            out_string += str(cur_head.value) + arrows
            cur_head = cur_head.next
        return out_string


def union(llist_1, llist_2):
    union_linkedlist = LinkedList()
    union_set = set()

    node1 = llist_1.head
    while node1:
        union_set.add(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        union_set.add(node2.value)
        node2 = node2.next

    for value in union_set:
        union_linkedlist.append(value)

    return union_linkedlist if union_linkedlist.head is not None else "There is no union"


def intersection(llist_1, llist_2):

    intersection_linkedlist = LinkedList()
    llist_1_set = set()
    llist_2_set = set()

    node1 = llist_1.head
    while node1:
        llist_1_set.add(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        llist_2_set.add(node2.value)
        node2 = node2.next

    for value in (llist_1_set & llist_2_set):
        intersection_linkedlist.append(value)
    return intersection_linkedlist if intersection_linkedlist.head is not None else "There is no intersection"


print("--------------------------------Test case 1----------------------------------")

llist_1 = LinkedList()
llist_2 = LinkedList()

element_1 = [4, 1, 8, 4, 5]
element_2 = [5, 0, 1, 8, 4, 5]

for i in element_1:
    llist_1.append(i)

for i in element_2:
    llist_2.append(i)

print('------Linked Lists------')
print(element_1)
print(element_2)

result1 = union(llist_1, llist_2)
print('------Union result------')
print(result1)

result2 = intersection(llist_1, llist_2)
print('------Intersection result------')
print(result2)


print("---------------------------------Test case 2------------------------------------")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print('------Linked Lists------')
print(element_1)
print(element_2)

result1 = union(linked_list_1, linked_list_2)
print('------Union result------')
print(result1)

result2 = intersection(linked_list_1, linked_list_2)
print('------Intersection result------')
print(result2)


print("----------------------------------Test case 3-----------------------------------")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_4 = [1, 7, 8, 9, 11, 21, 1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print('------Linked Lists------')
print(element_3)
print(element_4)

result1 = union(linked_list_3, linked_list_4)
print('------Union result------')
print(result1)

result2 = intersection(linked_list_3, linked_list_4)
print('------Intersection result------')
print(result2)
