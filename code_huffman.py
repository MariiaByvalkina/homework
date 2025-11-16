import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def encode(msg: str) -> tuple[str, dict[str, str]]:

    freq_table = Counter(msg)

    if len(freq_table) == 1:
        char = list(freq_table.keys())[0]
        return '0' * len(msg), {char: '0'}

    heap = []
    for char, freq in freq_table.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    encoding_table = {}

    def build_codes(node, code):
        if node is None:
            return
        if node.char is not None:
            encoding_table[node.char] = code
            return
        build_codes(node.left, code + '0')
        build_codes(node.right, code + '1')

    if heap:
        build_codes(heap[0], '')

    codes = []
    for char in msg:
        codes.append(encoding_table[char])
        encoded_msg = ''.join(codes)

    return encoded_msg, encoding_table

def decode(encoded: str, table: dict[str, str]) -> str:
    if not encoded:
        return ""

    decoding_table = {}
    for char, code in table.items():
        decoding_table[code] = char

    decoded_chars = []
    current_code = ""

    for bit in encoded:
        current_code += bit
        if current_code in decoding_table:
            decoded_chars.append(decoding_table[current_code])
            current_code = ""

    return ''.join(decoded_chars)

