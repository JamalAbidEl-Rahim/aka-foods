import pdfplumber
# Path to the PDF file
pdf_path = "C:/Users/jamal/Desktop/aka foods/AKA.pdf"

# Open the PDF with pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Specify the pages you want to extract (1-based index)
    specific_pages = [75]  # Pages to extract (1 = first page, 2 = second, etc.)

    for page_number in specific_pages:
        page = pdf.pages[page_number - 1]  # Convert to 0-based index
        print(f"Text from page {page_number}:\n")
        print(page.extract_text())
        print("\n" + "-" * 50 + "\n")
