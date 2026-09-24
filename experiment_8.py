file = open("input.txt", "r")
lines = file.readlines()
count = len(lines)

first_two_lines = lines[:2]
file.close()

print("Total number of lines:", count)
file1 = open("output.txt", "w")
for line in first_two_lines:
    file1.write(line)

file1.close()

print("First two lines have been written to output.txt")