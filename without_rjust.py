# Sample text
text = "Hello"

# Add spaces at the beginning to make the total length 10 without using rjust()
result = ' ' * (10 - len(text)) + text

print(result)