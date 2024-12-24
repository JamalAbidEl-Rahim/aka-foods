import pdfplumber
import pandas as pd

# Specify the file name and the page to extract
pdf_file = "C:/Users/jamal/Desktop/aka foods/AKA.pdf"
specific_page = 26  # Change this to the page number you want to extract
output_file = f"page_26.parquet"

# Open the PDF and extract the specific page
with pdfplumber.open(pdf_file) as pdf:
    if specific_page <= len(pdf.pages):  # Check if the page exists
        page = pdf.pages[specific_page - 1]  # Pages are 0-indexed
        raw_text = page.extract_text()

        if raw_text:  # Ensure the page is not empty
            # Force text to UTF-8
            raw_text = raw_text.encode('utf-8', 'replace').decode('utf-8')

            # Create a DataFrame with the extracted data
            data = {
                "file_name": pdf_file,
                "page_number": specific_page,
                "raw_text": raw_text
            }
            df = pd.DataFrame([data])

            # Save the data to a Parquet file
            df.to_parquet(output_file, engine="pyarrow", index=False)
            print(f"Page {specific_page} saved to {output_file}")
        else:
            print(f"Page {specific_page} is empty.")
    else:
        print(f"The PDF only has {len(pdf.pages)} pages.")
df = pd.read_parquet(output_file, engine="pyarrow")
print(f"\nContents of {output_file}:")
print(df)


