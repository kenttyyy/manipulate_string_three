# Sample text
text = "hello world"

# Return the first location of "world" in the string without using index()
result = text.find("world") if "world" in text else -1

print(result)