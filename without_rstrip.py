# Sample text
text = "Hello World    "

# Remove spaces at the end without using rstrip()
result = text[:len(text) - len(text) + len(text.rstrip())]

print(result)