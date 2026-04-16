def profile_matrix(sequences: list[str]) -> dict[str, list[int]]:
    """
    Build a profile matrix from a list of aligned DNA sequences.

    Each column of the matrix counts how many sequences have A, C, G, or T
    at that position.

    Args:
        sequences: A list of DNA strings, all of equal length.

    Returns:
        A dict mapping each base ('A', 'C', 'G', 'T') to a list of per-column
        counts.
    """
    # TODO: implement
    pass


def consensus_string(profile: dict[str, list[int]]) -> str:
    """
    Derive the consensus string from a profile matrix.

    At each position, choose the base with the highest count. Ties are broken
    in alphabetical order (A before C before G before T).

    Args:
        profile: A dict mapping each base to a list of per-column counts.

    Returns:
        The consensus string.
    """
    # TODO: implement
    pass


def main() -> None:
    sequences = [
        "ATCCAGCT",
        "GGGCAACT",
        "ATGGATCT",
        "AAGCAACC",
        "TTGGAACT",
        "ATGCCATT",
        "ATGGCACT",
    ]

    profile = profile_matrix(sequences)
    consensus = consensus_string(profile)
    print(consensus)
    for base in "ACGT":
        counts = []
        for count in profile[base]:
            counts.append(str(count))
        print(f"{base}: {' '.join(counts)}")

    # Expected:
    # ATGCAACT
    # A: 5 1 0 0 5 5 0 0
    # C: 0 0 1 4 2 0 6 1
    # G: 1 1 6 3 0 1 0 0
    # T: 1 5 0 0 0 1 1 6


    """ from custom_io import parse_fasta, write_result
    records = parse_fasta(__file__)
    sequences = []
    for _, seq in records:
        sequences.append(seq)
    profile = profile_matrix(sequences)
    consensus = consensus_string(profile)
    output_lines = [consensus]
    for base in "ACGT":
        counts = []
        for count in profile[base]:
            counts.append(str(count))
        output_lines.append(f"{base}: {' '.join(counts)}")
    output = "\n".join(output_lines)
    print(output)
    write_result(__file__, output) """


if __name__ == "__main__":
    main()
