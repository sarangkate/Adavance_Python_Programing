import csv
import json

file = open("Student.csv","w")

writer = csv.writer(file)
writer.writerow(["Roll_No","Name", "Marks"])
writer.writerow([1,"Sarang", "90"])
writer.writerow([2,"Saish", "95"])
writer.writerow([3,"Sarang", "90"])

file.close()

file = open("Student.csv", "r")
reader = csv.DictReader(file)
data = list(reader)

file.close()

file1 = open("output.json", "w")
json.dump(data, file1, indent=4)

file1.close()

print("CSV data converted to JSON successfully.")
