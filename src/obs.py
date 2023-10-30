import ast
import random
import re


# Define the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

# Create a substitution cipher with random binary values
cipher = {
    letter: "".join(
        random.choice(
            "Exx_xx__x___XEexeE_x_x_ "
        )
        for _ in range(8)
    )
    for letter in alphabet
}

    

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

# Define the Python code
with open("combined_scriptV3.py", "r") as pfile:
    python_code = pfile.read()

# Define a flag to track whether the next word is a variable, function, or class name
next_name_type = None

# Split the code into lines
code_lines = python_code.split('\n')

# Parse the code using the ast module
parsed_code = ast.parse(python_code)


# Use regular expressions to find and replace variable, function, and class names
def replace(match):
    matched_name = match.group()
    if matched_name in cipher:
        return cipher[matched_name]
    return matched_name

python_code = re.sub(r'(?<=def )\w+|(?<=class )\w+|(\w+)(?=\s*=\s*)', replace, python_code)

print(python_code)