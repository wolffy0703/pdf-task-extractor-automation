# PDF Task Extractor Automation

Extracts action items and tasks from PDFs and exports them to JSON or Notion.

## Features
- Parse PDF content using PyPDF2
- Extract bullets and deadlines
- Export tasks to JSON or Notion (optional)

## Tech Stack
- Python 3.x
- PyPDF2 / pdfminer
- Notion API (optional)

## Quick Start
1. `pip install -r requirements.txt`
2. `python src/extractor.py --input pdf/sample.pdf --output tasks.json`
