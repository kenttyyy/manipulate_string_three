# Sample text
text = "Hello World!"

# Remove "!" at the end without using removesuffix()
result = text[:-1] if text.endswith("!") else text

print(result)