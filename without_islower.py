# Sample text
text = "hello world"

# Check if all characters are lowercase without using islower()
result = all('a' <= c <= 'z' for c in text)

print(result)