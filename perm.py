def permutations(elements: list[int]) -> list[list[int]]:
    """
    Generate all permutations of a list of integers in lexicographic order.

    Args:
        elements: A sorted list of distinct integers.

    Returns:
        A list of all len(elements)! permutations in lexicographic order.
    Take one element away then recursively compute the premutation of remaining elements until base case.
    """
    if len(elements) == 1:
        return [elements]
    results: list[list[int]] = []
    for i in range(len(elements)):
        fs = elements[i]
        remain = elements[:i] + elements[i+1:]
        subperm = permutations(remain)
        for rest in subperm:
            results.append([fs]+rest)

    return results
def main() -> None:
    #n = 3

    #perms = permutations(list(range(1, n + 1)))
    #print(len(perms))
    #for perm in perms:
    #    print(" ".join(map(str, perm)))

    from custom_io import parse_int, write_result
    n = parse_int(__file__)
    perms = permutations(list(range(1, n + 1)))
    lines = [str(len(perms))] + [" ".join(map(str, perm)) for perm in perms]
    result = "\n".join(lines)
    print(result)
    write_result(__file__, result)


if __name__ == "__main__":
    main()
