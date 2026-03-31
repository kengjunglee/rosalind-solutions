from perm import permutations


def sign_combos(n: int) -> list[list[int]]:
    """
    Generate all combinations of +1 and -1 of length n.

    Args:
        n: A positive integer.

    Returns:
        A list of all 2^n sign combinations, each a list of +1 and -1 values.
    """
    pass


def signed_permutations(n: int) -> list[list[int]]:
    """
    Generate all signed permutations of [1, 2, ..., n].

    A signed permutation assigns a positive or negative sign to each element
    of a permutation, yielding 2^n * n! total orderings.

    Args:
        n: A positive integer.

    Returns:
        A list of all 2^n * n! signed permutations of [1, ..., n].
    """
    pass


def main() -> None:
    n = 2

    signed_perms = signed_permutations(n)
    print(len(signed_perms))
    for perm in signed_perms:
        print(" ".join(map(str, perm)))

    """ from custom_io import parse_int, write_result
    n = parse_int(__file__)
    signed_perms = signed_permutations(n)
    lines = [str(len(signed_perms))] + [" ".join(map(str, perm)) for perm in signed_perms]
    result = "\n".join(lines)
    print(result)
    write_result(__file__, result) """


if __name__ == "__main__":
    main()
