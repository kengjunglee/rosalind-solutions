from revc import reverse_complement

def find_reverse_palindromes(dna: str, min_length: int, max_length: int) -> list[tuple[int, int]]:
    """
    Find all reverse palindromes within a given length range in a DNA string.

    A reverse palindrome is a sequence that equals its own reverse complement.
    These are the sequences recognized by restriction enzymes — a strand reads
    the same as its complementary strand in the opposite direction.

    Args:
        dna: A DNA string.
        min_length: The minimum palindrome length to search for.
        max_length: The maximum palindrome length to search for.

    Returns:
        A list of (position, length) pairs (1-based positions) for every
        reverse palindrome within the length range.
    """
    result: list[tuple[int, int]] = []
    n = len(dna)
    for i in range(n):
        for l in range(min_length, max_length+1):
            if i+l <= n:
                substring = dna[i:i+l]
                if substring == reverse_complement(substring):
                    result.append((i, l))
    return result
    


def main() -> None:
    # dna = "TCAATGCATGCGGGTCTATATGCAT"

    # results = find_reverse_palindromes(dna, 4, 12)
    # for pos, length in results:
    #     print(pos+1, length)

    # Expected output:
    # 4 6    (ATGCAT — NcoI site)
    # 5 4    (TGCA)
    # 6 6    (GCATGC — SphI site)
    # 7 4    (CATG)
    # 17 4   (TATA)
    # 18 4   (ATAT)
    # 20 6   (ATGCAT)
    # 21 4   (TGCA)


    from custom_io import parse_fasta, write_result
    sequences = parse_fasta(__file__)
    dna = sequences[0][1]
    results = find_reverse_palindromes(dna, 4, 12)
    output = "\n".join(f"{pos+1} {length}" for pos, length in results)
    print(output)
    write_result(__file__, output)


if __name__ == "__main__":
    main()
