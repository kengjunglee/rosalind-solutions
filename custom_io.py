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


def parse_fasta(caller_file: str) -> list[tuple[str, str]]:
    """Parse a FASTA-formatted dataset.txt from the same directory as the calling script.

    Args:
        caller_file: The __file__ variable of the calling script.

    Returns:
        A list of (label, sequence) tuples, one per FASTA record.
    """
    text = read_dataset(caller_file)
    sequences: list[tuple[str, str]] = []
    label: str | None = None
    seq_parts: list[str] = []

    for line in text.split("\n"):
        if line.startswith(">"):
            if label is not None:
                sequences.append((label, "".join(seq_parts)))
            label = line[1:]
            seq_parts = []
        else:
            seq_parts.append(line)

    if label is not None:
        sequences.append((label, "".join(seq_parts)))

    return sequences


def parse_strings(caller_file: str) -> list[str]:
    """Parse a list of strings, one per line, from dataset.txt.

    Args:
        caller_file: The __file__ variable of the calling script.

    Returns:
        A list of strings, one per line.
    """
    text = read_dataset(caller_file)
    return text.split("\n")


def parse_ints(caller_file: str) -> list[int]:
    """Parse a single line of space-separated integers from dataset.txt.

    Args:
        caller_file: The __file__ variable of the calling script.

    Returns:
        A list of integers.
    """
    text = read_dataset(caller_file)
    result = []
    for token in text.split():
        result.append(int(token))
    return result


def parse_string_and_floats(caller_file: str) -> tuple[str, list[float]]:
    """Parse a DNA string (line 1) and space-separated floats (line 2) from dataset.txt.

    Args:
        caller_file: The __file__ variable of the calling script.

    Returns:
        A tuple of (dna_string, list_of_floats).
    """
    text = read_dataset(caller_file)
    lines = text.split("\n")
    dna = lines[0]
    floats = []
    for token in lines[1].split():
        floats.append(float(token))
    return dna, floats
