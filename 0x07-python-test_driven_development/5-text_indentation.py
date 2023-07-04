#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        for char in line:
            print(char, end="")
            if char in punctuation_marks:
                print("\n\n", end="")
        print()
