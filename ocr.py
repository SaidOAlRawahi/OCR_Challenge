import re
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe' #file path to tesseract program
from PIL import Image

#read the image
image = Image.open("image.png")
text = tess.image_to_string(image)
print(text)

pattern = r"(\d{1,2}\/\d{1,2}\/\d{4})|(\d{1,2}\s+[A-Za-z]+\s+\d{4})" #pattern of dates under the format of dd/mm/yyyy and dd Month yyyy
matches = re.findall(pattern, text)
print("\nDates: ")
print(matches)

pattern = r"Room:\s+(\w+)" #pattern for single worlds after Room: 
matches = re.findall(pattern, text)
print("\nRooms: ")
print(matches)

pattern = r"\$\d+" #pattern for numbers leaded by a dollar sign
matches = re.findall(pattern, text)
print("\nRates: ")
print(matches)

pattern = r"(?:Al\s+)?[A-Z][a-z]+\s*,\s(?!,\n)*[A-Z][a-z]+" #pattern for names that follow the format optional(Al) Name, Name
matches = re.findall(pattern, text)
print("\nNames: ")
print(matches)

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"#pattern for emails
matches = re.findall(pattern, text)
print("\nEmails: ")
print(matches)