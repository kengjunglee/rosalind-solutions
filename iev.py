def expected_dominant_offspring(couples: list[int]) -> float:
    """
    Calculate the expected number of dominant-phenotype offspring across all couples.

    Each couple produces exactly 2 offspring. By linearity of expectation, the
    total expected dominant offspring is the sum over all couple types of
    (count × 2 × P(dominant for that pairing)).

    Args:
        couples: A list of 6 non-negative integers representing the number of
                 couples for each genotype pairing (AA-AA through aa-aa).

    Returns:
        The expected total number of offspring displaying the dominant phenotype.
    """
    # TODO: implement
    pass


def main() -> None:
    couples = [1, 0, 0, 1, 0, 1]

    expected = expected_dominant_offspring(couples)
    print(round(expected, 1))

    # Expected: 3.5


    """ from custom_io import parse_ints, write_result
    couples = parse_ints(__file__)
    expected = expected_dominant_offspring(couples)
    print(round(expected, 1))
    write_result(__file__, str(round(expected, 1))) """


if __name__ == "__main__":
    main()
