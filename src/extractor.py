import argparse
import json
from pathlib import Path
from pdfminer.high_level import extract_text
from datetime import datetime

def extract_text_from_pdf(path):
    return extract_text(path)

def parse_tasks(text):
    # Very simple parser: lines containing keywords
    tasks = []
    for line in text.splitlines():
        line_strip = line.strip()
        if not line_strip:
            continue
        if any(k in line_strip.lower() for k in ['due', 'deadline', 'task', 'action', 'please']):
            tasks.append({'text': line_strip})
    return tasks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to PDF file')
    parser.add_argument('--output', default='tasks.json', help='Output JSON file')
    args = parser.parse_args()
    text = extract_text_from_pdf(args.input)
    tasks = parse_tasks(text)
    out = {'extracted_at': datetime.utcnow().isoformat() + 'Z', 'tasks': tasks}
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2)
    print('Tasks written to', args.output)

if __name__ == '__main__':
    main()
