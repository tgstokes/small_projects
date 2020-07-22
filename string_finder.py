# string finder/sorter.py
file_to_open = "random_text.txt"

def read_file(filename):
    output_text = []
    with open(filename) as fo:
        for line in fo:
            text = line.strip():
            output_text.append(text)
    return output_text

read_file(file_to_open)