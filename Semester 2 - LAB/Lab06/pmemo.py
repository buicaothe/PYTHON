# LAB6B - COMMANDLINE (MAIN function as pmemo.py)
# Import read_write.py:
import read_write as rw


def main():
    print("Enter your text (type 'END' on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    # Join the lines into a single string 's' separated by newlines
    s = "\n".join(lines)

    filename = input("Enter the file name to save to: ")

    # Calling write function from read_write module
    write_result = rw.write(s, filename)
    print(f"Number of characters: {write_result}")

    # Calling read function from read_write module
    read_result = rw.read(filename)
    print("Content: ")
    print(read_result)


# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
