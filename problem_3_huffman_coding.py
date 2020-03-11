import sys
from collections import Counter

class HuffManTreeNode(object):
    # define a Tree without value and store data by leaf node
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        
    def set_left_child(self,left):
        self.left = left
    
    def get_left_child(self):
        return self.left
    
    def set_right_child(self,right):
        self.right = right
    
    def get_right_child(self):
        return self.right
    
class HuffManTree(object):
    def __init__(self, data=None):
        self.frequencies = sorted(Counter(data).most_common(), key=lambda x: x[1])
        
    def get_tree_root(self):
        while len(self.frequencies) > 1:
            # create subtree from the lowest frequencies node to the highest frequencies node 
            (key1, freq1) = self.frequencies[0]
            (key2, freq2) = self.frequencies[1]
            self.frequencies = self.frequencies[2:]
            
            # The keys are string type in leaf node, otherwise are node type
            left_node = key1
            right_node = key2
            node = HuffManTreeNode(left_node, right_node)

            self.frequencies.append((node, freq1+freq2))
            self.frequencies = sorted(self.frequencies, key=lambda x: x[1])

        return self.frequencies[0][0]

def huffman_encoding_recursion(node, code=''):
    """
    Encoding characters using recursion
    Args:
      node(HuffManTreeNode):  leaf to save data and non-leaf node assign 0 and 1 to edges
      code(str): Assign 0 to the left edge and 1 to the right edge 

    Returns:
      encode_map(dict) : huffman coding map table
    """
    if type(node) is str:
        return {node: code}
    
    encode_map = dict()
    
    left_node = node.get_left_child()
    right_node = node.get_right_child()
    
    encode_map.update(huffman_encoding_recursion(left_node, code + '0'))
    encode_map.update(huffman_encoding_recursion(right_node, code + '1'))
    return encode_map

def huffman_encoding(data):
    if not data:
        return
    
    huffman_tree = HuffManTree(data)
    root_node = huffman_tree.get_tree_root()
    encode_map = huffman_encoding_recursion(root_node)
    
    encoded_list = [encode_map[c] for c in data]
    encoded_string = ''.join(encoded_list)
 
    return(encoded_string, root_node)

def huffman_decoding(data,root):
    node = root
    decoded_data = ''

    for b in data:   
        if b == '0' and type(node) is HuffManTreeNode:
            node = node.get_left_child()

        elif b == '1' and type(node) is HuffManTreeNode:
            node = node.get_right_child()
        
        if type(node) is str:
            decoded_data += node
            node = root

    return decoded_data
