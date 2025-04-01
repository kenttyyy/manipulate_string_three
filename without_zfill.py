# Sample text
text = "42"

# Add zeroes at the beginning to make the total length 5 without using zfill()
result = '0' * (5 - len(text)) + text

print(result)