import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)

    courses = list(reader)

print("All Course Records:")
for c in courses:
    print(c)

cid = input("\nEnter Course ID to search: ")

found = False

for c in courses:
    if c["Course_ID"] == cid:
        print("Course Found:")
        print(c)
        found = True
        break

if not found:
    print("Course not found")
