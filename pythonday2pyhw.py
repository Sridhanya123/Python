
paragraph = """
Python is a popular programming language.
This Python course helps beginners learn coding easily.
Python is used in many applications.
"""
paragraph = paragraph.strip()

print("Length of paragraph:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("First 50 characters:")
print(paragraph[:50])

paragraph_upper = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':")
print(paragraph_upper)

paragraph_lower = paragraph.lower()
print("\nParagraph in lowercase:")
print(paragraph_lower)

words = paragraph.split()
print("\nList of words:")
print(words)

if "course" in paragraph.lower():
    print("\nThe word 'course' is found in the paragraph.")

print(
    "\nThe course description is {} characters long and has {} words."
    .format(len(paragraph), len(words))
)
