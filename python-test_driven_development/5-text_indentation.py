#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to process and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".:?":
            result += "\n\n"
            i += 1
            # Skip all spaces after the punctuation mark
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    
    # Print the final processed text
    print(result, end="")
