# LAB6B - READ_WRITE FUNCTION (read_write.py)

# 1. write function:
def write(s, filename):
    try:
        # Use the variable filename, not the string 'filename'
        with open(filename, 'w') as f:
            number_of_char = f.write(s)
            return number_of_char
    except Exception as e:
        # Return the error message text as per instructions
        return f"Error writing to file: {e}"

# 2. read function:


def read(filename):
    try:
        # Use the variable filename, not the string 'filename'
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except Exception as e:
        # Return the error message text if anything went wrong
        return f"Error reading file: {e}"
