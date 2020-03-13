import sys
from collections import Counter


class HuffManTreeNode(object):
    # define a Tree without value and store data by leaf node
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def set_left_child(self, left):
        self.left = left

    def get_left_child(self):
        return self.left

    def set_right_child(self, right):
        self.right = right

    def get_right_child(self):
        return self.right


class HuffManTree(object):
    def __init__(self, data=None):
        self.frequencies = data

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

            self.frequencies.append((node, freq1 + freq2))
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


def huffman_encoding(data=None):
    if data is None:
        return (None, None)
    if len(data) == 0:
        return (data, None)

    pro_data = sorted(Counter(data).most_common(), key=lambda x: x[1])
    if len(pro_data) == 1:
        return('0' * pro_data[0][1], pro_data)

    huffman_tree = HuffManTree(pro_data)
    root_node = huffman_tree.get_tree_root()
    encode_map = huffman_encoding_recursion(root_node)

    encoded_list = [encode_map[c] for c in data]
    encoded_string = ''.join(encoded_list)

    return(encoded_string, root_node)


def huffman_decoding(data, decoder):
    if data is None:
        return None

    if len(data) == 0:
        return data

    if type(decoder) is list:
        return(decoder[0][1] * decoder[0][0])

    node = decoder
    decoded_data = ''

    for b in data:
        if b == '0' and type(node) is HuffManTreeNode:
            node = node.get_left_child()

        elif b == '1' and type(node) is HuffManTreeNode:
            node = node.get_right_child()

        if type(node) is str:
            decoded_data += node
            node = decoder

    return decoded_data


def test_huffman_coding(a_great_sentence):

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, decoder = huffman_encoding(a_great_sentence)

    if(encoded_data):
        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    else:
        print("The size of the encoded data is: {}\n".format(encoded_data, base=2))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, decoder)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


print('-------------Test case 1:a_great_sentence = "Data Structures & Algorithms"---------------')
'''
The size of the data is: 77

The content of the data is: Data Structures & Algorithms

The size of the encoded data is: 40

The content of the encoded data is: 1011010000111000001101110110101001110000111001010110011010001110100011101111100111011111001011111011000000011010

The size of the decoded data is: 77

The content of the encoded data is: Data Structures & Algorithms
'''
a_great_sentence = "Data Structures & Algorithms"
test_huffman_coding(a_great_sentence)

print('-----------------------Test case 2 : a_great_sentence = "aaaaaa"--------------------------')
'''
The size of the data is: 55

The content of the data is: aaaaaa

The size of the encoded data is: 24

The content of the encoded data is: 000000

The size of the decoded data is: 55

The content of the encoded data is: aaaaaa
'''
a_great_sentence = "aaaaaa"
test_huffman_coding(a_great_sentence)

print('-------------------------Test case 3 : a_great_sentence = ""-------------------------------')
'''
The size of the data is: 49

The content of the data is: 

The size of the encoded data is: 

The content of the encoded data is: 

The size of the decoded data is: 49

The content of the encoded data is:
'''
a_great_sentence = ""
test_huffman_coding(a_great_sentence)
