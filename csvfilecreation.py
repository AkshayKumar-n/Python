import pandas
import csv
Header = ["Name", "Rollno"]
studentData = [{"Name": "Akshay", "Rollno": "101"},

               {"Name": "Abhi", "Rollno": "102"},
               {"Name": "Akhil", "Rollno": "103"},
               {"Name": "Pavan", "Rollno": "104"}
               ]

with open("students.csv", 'w+', encoding='UTF8', newline="") as s:
    writer = csv.DictWriter(s, fieldnames=Header)
    writer.writeheader()
    writer.writerows(studentData)

# d = pandas.read_csv("students.csv")
# print(d.tail(n=2))
