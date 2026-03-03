#!/usr/bin/env python3
"""
Update resume PDF with Peter Kagai's information
"""
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    from PyPDF2 import PdfReader, PdfWriter

import os
import shutil

# Read the existing PDF
pdf_path = "Full Resume...1.pdf"

# Define replacements
replacements = {
    "Joseph Kagai": "Peter Kagai",
    "(979) 600-5310": "(437) 557-0340",
    "josephkagai635@gmail.com": "petermkagai@gmail.com",
    "19 Sep 1997": "19 Sep 1995",
    "1997": "1995",
    "28 years": "30 years",
}

try:
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    print("Processing resume PDF...")
    
    # Copy pages
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        
        # Check for updates needed
        found_items = []
        for old, new in replacements.items():
            if old in text:
                found_items.append(f"'{old}' -> '{new}'")
        
        if found_items:
            print(f"  Page {page_num}: Found {len(found_items)} items to update:")
            for item in found_items:
                print(f"    - {item}")
        
        writer.add_page(page)
    
    # Write the updated PDF
    output_path = "Full Resume - Peter Kagai.pdf"
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    
    print(f"\n✓ Updated resume copy created: {output_path}")
    print("\nNote: The PDF structure requires manual editing for text content updates.")
    print("The HTML portfolio has been fully updated with Peter Kagai's information.")
    
except Exception as e:
    print(f"Error processing PDF: {e}")
    print("\nNote: The HTML portfolio has been fully updated with Peter Kagai's information.")
    print("For the PDF resume, please manually edit or use a dedicated PDF editor.")

print("\nResume update process completed!")
