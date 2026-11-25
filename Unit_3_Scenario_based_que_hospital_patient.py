import csv

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)

    patients = list(reader)

print("All Patient Records:")
for p in patients:
    print(p)

pid = input("\nEnter Patient ID to search: ")

found = False

for p in patients:
    if p["Patient_ID"] == pid:
        print("Patient Found:")
        print(p)
        found = True
        break

if not found:
    print("Patient not found")
