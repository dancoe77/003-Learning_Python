zz = "####################################################################################"
print(zz)
import csv
data = open("example.csv")
csv_data = csv.reader(data)
data_lines = list(csv_data)
# print(data_lines)
print(data_lines[0])
print(zz)
print(len(data_lines))
print(zz)
for line in data_lines[:5]:
    print(line)
print(zz)
print(data_lines[10])
print(zz)
print(data_lines[10][3])
print(zz)
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print(all_emails)
print(zz)
print(data_lines[10])
print(zz)
full_name = []
for line in data_lines[1:]:
    full_name.append(line[1]+' '+line[2])
print(full_name)
print(zz)
file_to_output = open("output.csv", "w", newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(["a","b","c"])
csv_writer.writerows([["1","2","3"],["4","5","6"]])
file_to_output.close()
f = open("output.csv", "a", newline='')
csv_writer = csv.writer(f, delimiter=',')
csv_writer.writerows([["1","2","3"],["4","5","6"]])
f.close()