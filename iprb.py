def mendel_probability(k: int, m: int, n: int) -> float:
    """
    Compute the probability that two randomly selected organisms from a population
    of k (AA), m (Aa), and n (aa) individuals produce a dominant-phenotype offspring.

    Computes P(dominant) directly by summing over pairings that produce a dominant
    offspring: AA×anyone (certainty), Aa×Aa (3/4 chance), Aa×aa (1/2 chance).
    The denominator T*(T-1) reflects sampling without replacement — the two parents
    are distinct.

    Args:
        k: Number of homozygous dominant (AA) individuals.
        m: Number of heterozygous (Aa) individuals.
        n: Number of homozygous recessive (aa) individuals.

    Returns:
        The probability of a dominant-phenotype offspring from a random mating.
    """
    # TODO: implement
    pass


def main() -> None:
    k, m, n = 2, 2, 2

    prob = mendel_probability(k, m, n)
    print(round(prob, 5))

    # Expected: 0.78333


    """ from custom_io import parse_ints, write_result
    values = parse_ints(__file__)
    k, m, n = values[0], values[1], values[2]
    prob = mendel_probability(k, m, n)
    print(round(prob, 5))
    write_result(__file__, str(round(prob, 5))) """


if __name__ == "__main__":
    main()
