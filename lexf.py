def enumerate_kmers(alphabet: list[str], k: int) -> list[str]:
    """
    Generate all strings of length k formed from the given alphabet,
    listed in lexicographic order defined by the alphabet's ordering.

    Args:
        alphabet: An ordered list of symbols defining the lexicographic order.
        k: The length of each string to generate.

    Returns:
        A list of all len(alphabet)^k strings of length k, in lex order.
    """
    if k == 1: return (list(alphabet)) #base case
    #inductive steps
    result:list[str] = [] 
    #range over the alphabet, and place the s symbol at the begining of all the strings with length k-1
    for s in alphabet:
        substring = enumerate_kmers(alphabet, k-1)
        #concatenate each symbol at the its start for each substring
        for suffix in substring:
            result.append(s+suffix)
    return result


def main() -> None:
    # alphabet = ["A", "C", "G", "T"]
    # k = 2

    # for kmer in enumerate_kmers(alphabet, k):
    #     print(kmer)

    from custom_io import parse_alphabet_and_int, write_result
    alphabet, k = parse_alphabet_and_int(__file__)
    result = "\n".join(enumerate_kmers(alphabet, k))
    print(result)
    write_result(__file__, result)


if __name__ == "__main__":
    main()
