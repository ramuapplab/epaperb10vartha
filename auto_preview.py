from pdf2image import convert_from_path
from PIL import Image
import json
from datetime import datetime

# Read latest date from JSON
with open('archive-index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    latest_date = data['editions'][0]['date']

# Convert PDF Page 1 to image
pdf_path = f'pages/{latest_date}/page1.pdf'
images = convert_from_path(pdf_path, dpi=150, poppler_path=r'C:\poppler\Library\bin')
pdf_image = images[0]

# Create preview canvas (1200x630 - Facebook/WhatsApp size)
preview = Image.new('RGB', (1200, 630), 'white')

# Calculate scaling to fit ENTIRE page width
scale = 1200 / pdf_image.width
new_height = int(pdf_image.height * scale)
pdf_resized = pdf_image.resize((1200, new_height), Image.Resampling.LANCZOS)

# Paste from TOP (shows logo, date, headline)
preview.paste(pdf_resized, (0, 0))

# Save
preview.save('preview-small.png', 'PNG', optimize=True, quality=90)
print(f"✅ Preview created: Shows full width, starting from TOP")
print(f"   Date: {latest_date}")
print(f"   Original size: {pdf_image.width}x{pdf_image.height}")
print(f"   Preview size: 1200x630 (fits width, crops bottom)")
