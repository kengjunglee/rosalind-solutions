import os


def read_dataset(caller_file):
    """Read dataset.txt from the same directory as the calling script."""
    directory = os.path.dirname(os.path.abspath(caller_file))
    filepath = os.path.join(directory, "dataset.txt")
    with open(filepath) as f:
        return f.read().strip()


def write_result(caller_file, result):
    """Write result to output.txt in the same directory as the calling script."""
    directory = os.path.dirname(os.path.abspath(caller_file))
    filepath = os.path.join(directory, "output.txt")
    with open(filepath, "w") as f:
        f.write(str(result) + "\n")


def parse_two_ints(caller_file):
    """Parse two integers from one line (e.g., fib, fibd datasets)."""
    text = read_dataset(caller_file)
    a, b = text.split()
    return int(a), int(b)


def parse_int(caller_file):
    """Parse a single integer (e.g., perm, sign datasets)."""
    text = read_dataset(caller_file)
    return int(text)


def parse_alphabet_and_int(caller_file):
    """Parse an alphabet (line 1) and an integer (line 2) (e.g., lexf, lexv datasets)."""
    text = read_dataset(caller_file)
    lines = text.split("\n")
    alphabet = lines[0].split()
    n = int(lines[1])
    return alphabet, n
