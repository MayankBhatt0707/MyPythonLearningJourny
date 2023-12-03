def remove_strip(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()

print(remove_strip("                 Mayank is a good boy        ", "Mayank"))