import re

def find_emails(text):
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    emails = re.findall(pattern, text)
    return emails

text = input("Enter text: ")

result = find_emails(text)

print("Email addresses:", result)
