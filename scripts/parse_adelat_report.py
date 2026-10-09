import pypdf
import json
import os

def extract_pdf_data(pdf_path, output_json):
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        return
    reader = pypdf.PdfReader(pdf_path)
    pages_text = [page.extract_text() for page in reader.pages]
    print(f"Extracted {len(pages_text)} pages.")

if __name__ == "__main__":
    pdf = r"../data/raw/ADELAT_BM_Canales_Atencion_INFORME_REGIONAL.pdf"
    out = r"../data/processed/adelat_report_raw_text.json"
    extract_pdf_data(pdf, out)
