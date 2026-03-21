title = "String Reflection"

def to_camel_case(s: str) -> str:
    words = s.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

result = to_camel_case(title)
print(f"{result}.py")