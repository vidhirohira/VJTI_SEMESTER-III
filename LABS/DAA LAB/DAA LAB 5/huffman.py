import heapq
from collections import defaultdict, Counter
import readbooks as rb

# Define a class for Huffman Tree nodes
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes based on frequency for heapq
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
def build_huffman_tree(text):
    freq = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman Codes
def generate_codes(node, code, codes):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = code
    
    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

# Compress the text using Huffman Coding
def compress(text):
    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)
    compressed = ''.join([codes[char] for char in text])
    return compressed, codes

# Calculate the compression ratio
def calculate_compression_ratio(original_text, compressed_text):
    original_size = len(original_text) * 8  # Original text size in bits (1 char = 8 bits)
    compressed_size = len(compressed_text)  # Compressed text size (already in bits)
    return original_size, compressed_size

def process_file(file_type, file_path_or_url):
    # Extract text based on the file type
    if file_type == 'html':
        text = rb.extract_text_from_html(file_path_or_url)  # URL for HTML files
    elif file_type == 'docx':
        text = rb.extract_text_from_doc(file_path_or_url)  # DOCX file path
    elif file_type == 'pdf':
        text = rb.extract_text_from_pdf_plumber(file_path_or_url)  # PDF file path
    elif file_type == 'txt':
        text = rb.extract_text_from_txt(file_path_or_url)  # TXT file path
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
    
    # Compress the extracted text
    compressed_text, huffman_codes = compress(text)
    original_size, compressed_size = calculate_compression_ratio(text, compressed_text)
    
    # Output the results
    print(f"Original text size (in bits): {original_size}")
    print(f"Compressed text size (in bits): {compressed_size}")
    print(f"Compression ratio: {compressed_size / original_size}")
    return compressed_text, huffman_codes

# Example usage:
# For HTML file (provide the URL):
html_url = 'file:///F:/VIDHI%20ROHIRA%20SY%20BTECH%20CE/SEMESTER%203/DAA_LAB5/book.html'
process_file('html', html_url)

# For DOCX file (provide the file path):
process_file('docx', 'book.docx')

# For PDF file (provide the file path):
process_file('pdf', 'book.pdf')

# For TXT file (provide the file path):
# process_file('txt', 'book.txt')

