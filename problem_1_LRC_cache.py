class DLinkedNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.previous = self.head

    def _add_node(self, node):
        # add new node into DLinkedNode
        node.next = self.head.next
        self.head.next.previous = node

        node.previous = self.head
        self.head.next = node

    def _remove_node(self, node):
        # remove node from DLinkedNode
        node.next.previous = node.previous
        node.previous.next = node.next

    def _move_to_head(self, node):
        # move node to DLinkedNode's head
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # pop the tial node that removes the least recently used entry
        node = self.tail.previous
        self._remove_node(node)
        return node

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = self.cache.get(key)

        if not node:
            new_node = DLinkedNode(key, value)
            if self.size >= self.capacity:
                # delete the last node of DLinkedList
                del_node = self._pop_tail()
                del self.cache[del_node.key]
                self.size -= 1

            # add the new node
            self._add_node(new_node)
            self.cache[key] = new_node
            self.size += 1

        else:
            # update value by key
            node.value = value
            self._move_to_head(node)
