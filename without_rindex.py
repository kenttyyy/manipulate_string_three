# Sample text
text = "hello world, hello universe"

# Return the first location of "hello" starting from the last character without using rindex()
result = len(text) - text[::-1].index("hello") - len("hello")

print(result)