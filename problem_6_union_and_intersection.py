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

    union_llist = LinkedList()

    p1 = llist_1.head
    p2 = llist_2.head

    while p1:
        union_llist.append(p1.value)
        p1 = p1.next

    while p2:
        union_llist.append(p2.value)
        p2 = p2.next

    return union_llist


def intersection(llist_1, llist_2):

    p1 = llist_1.head
    llist_set = set()

    while p1:
        if not p1.value in llist_set:
            p2 = llist_2.head
            while p2:
                if p1 == p2:
                    llist_set.add(p1.value)
                p2 = p2.next
        p1 = p1.next

    inter_llist = LinkedList()
    for i in llist_set:
        inter_llist.append(i)

    return inter_llist
