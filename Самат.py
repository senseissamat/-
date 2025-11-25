def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def capitalize_words(text):
    return text.title()

def count_letters(text):
    return len(text.replace(" ", ""))


print("--- Using full module logic (inside one file) ---")
print("Add:", add(10, 5))
print("Capitalize:", capitalize_words("hello world"))

print("\n--- Using specific function logic ---")
print("Multiply:", multiply(4, 6))
print("Divide:", divide(20, 5))
print("Count letters:", count_letters("Hello ChatGPT"))
