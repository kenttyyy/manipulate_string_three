# Sample text
text = "hello world"

# Convert all characters to uppercase without using upper()
result = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in text])

print(result)