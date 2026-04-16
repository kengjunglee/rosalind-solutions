import math


def at_least_n_aabb(k: int, n: int) -> float:
    """
    Compute the probability that at least n of the 2^k organisms in generation k
    of Mendel's experiment have the AaBb genotype.

    Starting from an AaBb individual, each generation consists of AaBb parents
    crossed together. From any AaBb × AaBb cross, P(offspring is Aa) = 1/2 and
    P(offspring is Bb) = 1/2 independently, so P(AaBb) = 1/4. The 2^k organisms
    in generation k are independent, giving a binomial distribution.

    Args:
        k: The number of generations (generation k has 2^k organisms).
        n: The minimum number of AaBb organisms required.

    Returns:
        The probability that at least n of the 2^k organisms are AaBb.
    """
    # TODO: implement
    pass


def main() -> None:
    k, n = 2, 1

    prob = at_least_n_aabb(k, n)
    print(round(prob, 3))

    # Expected: 0.684


    """ from custom_io import parse_two_ints, write_result
    k, n = parse_two_ints(__file__)
    prob = at_least_n_aabb(k, n)
    print(round(prob, 3))
    write_result(__file__, str(round(prob, 3))) """


if __name__ == "__main__":
    main()
