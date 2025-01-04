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

# Decompress the text using Huffman Coding
def decompress(compressed_text, huffman_codes):
    # Reverse the huffman_codes dictionary to map code to character
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    
    # Decode the compressed text
    current_code = ""
    decompressed_text = ""
    
    for bit in compressed_text:
        current_code += bit
        
        # If the current code matches a character in the reversed codes, append that character
        if current_code in reverse_codes:
            decompressed_text += reverse_codes[current_code]
            current_code = ""  # Reset current code after matching

    return decompressed_text

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

# Function to handle user input for decompression
def user_input_decompression():
    # Step 1: Get the file paths for compressed data and Huffman codes
    compressed_file_path = input("Enter the path to the compressed file (e.g., compressed.txt): ")
    huffman_codes_file_path = input("Enter the path to the file containing Huffman codes (e.g., huffman_codes.json): ")

    # Step 2: Read the compressed data (assuming the compressed file contains only the binary string)
    try:
        with open(compressed_file_path, 'r') as file:
            compressed_text = file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {compressed_file_path} was not found.")
        return

    # Step 3: Load the Huffman codes (assuming it's saved as a JSON file)
    try:
        import json
        with open(huffman_codes_file_path, 'r') as file:
            huffman_codes = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {huffman_codes_file_path} was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The Huffman codes file is not a valid JSON file.")
        return

    # Step 4: Perform decompression
    decompressed_text = decompress(compressed_text, huffman_codes)

    # Step 5: Print or save the decompressed text
    print("Decompressed text:")
    print(decompressed_text[:500])  # Show first 500 characters for preview
    save_decompressed = input("Would you like to save the decompressed text to a file? (y/n): ")
    if save_decompressed.lower() == 'y':
        save_path = input("Enter the file path to save the decompressed text: ")
        with open(save_path, 'w') as file:
            file.write(decompressed_text)
        print(f"Decompressed text saved to {save_path}")

# Run the decompression example with user input
user_input_decompression()
