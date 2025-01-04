import heapq
from collections import Counter
from docx import Document
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import os

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
    heap = [HuffmanNode(char, freq[char]) for char in freq]
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
    
    # Print Huffman codes for each character
    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(f"Character: '{char}' -> Code: {code}")
    
    compressed = ''.join([codes[char] for char in text])
    return compressed, codes, root

# Calculate the compression ratio
def calculate_compression_ratio(original_text, compressed_text):
    original_size = len(original_text) * 8  # Original text size in bits (1 char = 8 bits)
    compressed_size = len(compressed_text)  # Compressed text size (already in bits)
    return original_size, compressed_size

# Decompress the text using Huffman Codes and the Huffman Tree
def decompress(compressed_text, root):
    current_node = root
    original_text = []
    
    for bit in compressed_text:
        # Traverse the Huffman tree
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # When we reach a leaf node, we've decoded a character
        if current_node.char is not None:
            original_text.append(current_node.char)
            current_node = root  # Reset to root for next character

    return ''.join(original_text)

# Read DOCX file
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

# Read PDF file
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Read HTML file
def extract_text_from_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup.get_text()

# Read TXT file
def extract_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Get file size in bytes
def get_file_size(text):
    return len(text.encode('utf-8'))  # File size in bytes (assuming UTF-8 encoding)

# Process file depending on its type
def process_file(file_type, file_path):
    # Extract text based on the file type
    if file_type == 'html':
        text = extract_text_from_html(file_path)  # Local HTML file
    elif file_type == 'docx':
        text = extract_text_from_docx(file_path)  # DOCX file path
    elif file_type == 'pdf':
        text = extract_text_from_pdf(file_path)  # PDF file path
    elif file_type == 'txt':
        text = extract_text_from_txt(file_path)  # TXT file path
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    # Print the original text (before compression)
    print("\nOriginal Text (Before Compression):")
    print(text[:500])  # Show a portion (first 500 characters) of the original text for brevity
    
    # Compress the extracted text
    compressed_text, huffman_codes, root = compress(text)
    original_size, compressed_size = calculate_compression_ratio(text, compressed_text)

    # Print the compressed text (first 500 characters of the binary string for brevity)
    print("\nCompressed Text (After Compression):")
    print(compressed_text[:500])

    # Decompress the text to verify correctness
    decompressed_text = decompress(compressed_text, root)

    # Output the results
    print(f"\nOriginal text size (in bits): {original_size}")
    print(f"Compressed text size (in bits): {compressed_size}")
    print(f"Compression ratio: {compressed_size / original_size}")
    print(f"Decompression successful: {text == decompressed_text}")

    # Print the decompressed text (first 500 characters for brevity)
    print("\nDecompressed Text (After Decompression):")
    print(decompressed_text[:500])

    # Print the character codes of the decompressed text
    print("\nCharacter Codes in Decompressed Text:")
    for char in decompressed_text[:500]:  # Displaying a portion for brevity
        print(f"Character: '{char}' -> Code: {huffman_codes.get(char)}")

    # Print the size of the decompressed text (file size in bytes)
    decompressed_size = get_file_size(decompressed_text)
    print(f"\nDecompressed File Size (in bytes): {decompressed_size}")

    return compressed_text, huffman_codes

# Example usage with the files you generated:

# For DOCX file:
# process_file('docx', 'book.docx')

# For HTML file:
process_file('html', 'book.html')

# For PDF file:
# process_file('pdf', 'book2.pdf')

# For TXT file:
# process_file('txt', 'book2.txt')
