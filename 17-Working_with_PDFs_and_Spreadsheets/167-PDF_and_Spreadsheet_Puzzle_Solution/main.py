import csv
data = open("find_the_link.csv")
csv_data = csv.reader(data)
data_lines = list(csv_data)
# print(data_lines)
link_str = ""
for row_num,data in enumerate(data_lines):
    link_str += data[row_num]
print(link_str)
import pypdf
f = open("Find_the_Phone_Number.pdf", "rb")
pdf = pypdf.PdfReader(f)
print(pdf.get_num_pages())
import re
pattern = r"\d{3}.\d{3}.\d{4}"
all_text = ""
for n in range(pdf.get_num_pages()):
    page = pdf.get_page(n)
    page_text = page.extract_text()
    all_text = all_text+ " " +page_text
# print(all_text)
for match in re.finditer(pattern, all_text):
    print(match)
# print(all_text[42624:42624+20])