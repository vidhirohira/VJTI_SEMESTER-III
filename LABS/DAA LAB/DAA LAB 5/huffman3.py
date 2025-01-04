import heapq
from collections import Counter
from docx import Document
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

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
    compressed = ''.join([codes[char] for char in text])
    return compressed, codes

# Calculate the compression ratio
def calculate_compression_ratio(original_text, compressed_text):
    original_size = len(original_text) * 8  # Original text size in bits (1 char = 8 bits)
    compressed_size = len(compressed_text)  # Compressed text size (already in bits)
    return original_size, compressed_size

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

    # Compress the extracted text
    compressed_text, huffman_codes = compress(text)
    original_size, compressed_size = calculate_compression_ratio(text, compressed_text)

    # Output the results
    print(f"Original text size (in bits): {original_size}")
    print(f"Compressed text size (in bits): {compressed_size}")
    print(f"Compression ratio: {compressed_size / original_size}")
    return compressed_text, huffman_codes

# Example usage with the files you generated:

# For HTML file:
# process_file('html', 'book2.html')

# For DOCX file:
process_file('docx', 'book.docx')

# For PDF file:
# process_file('pdf', 'book2.pdf')

# For TXT file:
# process_file('txt', 'book2.txt')
