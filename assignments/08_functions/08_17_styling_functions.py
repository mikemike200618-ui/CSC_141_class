
def bold_text(text):
    """Return the text formatted in bold."""
    return f"\033[1m{text}\033[0m"
def italic_text(text):
    """Return the text formatted in italics."""
    return f"\033[3m{text}\033[0m"
def underline_text(text):
    """Return the text formatted with underline."""
    return f"\033[4m{text}\033[0m"
# Demonstrate the styling functions
sample_text = "Hello, World!"
print(bold_text(sample_text))
print(italic_text(sample_text))
print(underline_text(sample_text))
# These functions apply different text styles (bold, italics, underline) using ANSI escape codes
# and demonstrate their usage by styling a sample text.
# Note: The styling may not display correctly in all environments, such as some IDEs or text editors. 
# It is best viewed in a terminal that supports ANSI escape codes. 
