import requests
from bs4 import BeautifulSoup
from docx import Document
import PyPDF2
import pdfplumber

# Function to download and extract text from HTML pages
def extract_text_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text

# Function to extract text from DOC files
def extract_text_from_doc(doc_file):
    doc = Document(doc_file)
    text = ' '.join([para.text for para in doc.paragraphs])
    return text

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Alternative PDF extraction using pdfplumber (more accurate for complex layouts)
def extract_text_from_pdf_plumber(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to read text from a simple TXT file
def extract_text_from_txt(txt_file):
    with open(txt_file, 'r') as file:
        text = file.read()
    return text
