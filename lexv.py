def extend_strings(alphabet: list[str], n: int, current: str) -> list[str]:
    """
    Generate all extensions of current up to length n.

    Args:
        alphabet: An ordered list of symbols.
        n: The maximum string length.
        current: The string to extend.

    Returns:
        A list of current and all its extensions up to length n, in lex order.
    """
    pass


def enumerate_strings(alphabet: list[str], n: int) -> list[str]:
    """
    Generate all strings of length 1 through n formed from the given alphabet,
    in lexicographic order defined by the alphabet's ordering.

    The ordering treats shorter strings as coming before their own extensions:
    e.g. with alphabet [A, C], n=2: A, AA, AC, C, CA, CC.
    This corresponds to a preorder (depth-first) traversal of the k-mer trie.

    Args:
        alphabet: An ordered list of symbols defining the lexicographic order.
        n: The maximum string length.

    Returns:
        A list of all strings of length 1 to n in the defined lex order.
    """
    pass


def main() -> None:
    alphabet = ["D", "N", "A"]
    n = 3

    for s in enumerate_strings(alphabet, n):
        print(s)

    """ from custom_io import parse_alphabet_and_int, write_result
    alphabet, n = parse_alphabet_and_int(__file__)
    result = "\n".join(enumerate_strings(alphabet, n))
    print(result)
    write_result(__file__, result) """


if __name__ == "__main__":
    main()
