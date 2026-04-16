import math


def log_random_string_prob(dna: str, gc_content: float) -> float:
    """
    Compute the log base-10 probability that a DNA string was generated randomly
    with a given GC content.

    Under the model, each G and C base is drawn with probability gc_content/2,
    and each A and T base is drawn with probability (1 - gc_content)/2.
    The log probability is the sum of log probabilities of each base.

    Args:
        dna: A DNA string.
        gc_content: The GC-content probability (between 0 and 1).

    Returns:
        The log base-10 probability of generating the string under this model.
    """
    # TODO: implement
    pass


def log_random_string_probs(dna: str, gc_values: list[float]) -> list[float]:
    """
    Compute log base-10 probabilities for a DNA string over a list of GC contents.

    Args:
        dna: A DNA string.
        gc_values: A list of GC-content probabilities (each between 0 and 1).

    Returns:
        A list of log base-10 probabilities, rounded to 3 decimal places.
    """
    # TODO: implement
    pass


def main() -> None:
    dna = "ACGATACAA"
    gc_values = [0.129, 0.287, 0.423, 0.476, 0.641, 0.793, 0.837]

    results = log_random_string_probs(dna, gc_values)
    print(" ".join(str(r) for r in results))

    # Expected: -5.737 -5.217 -5.263 -5.36 -5.958 -7.116 -7.668


    """ from custom_io import parse_string_and_floats, write_result
    dna, gc_values = parse_string_and_floats(__file__)
    results = log_random_string_probs(dna, gc_values)
    output = " ".join(str(r) for r in results)
    print(output)
    write_result(__file__, output) """


if __name__ == "__main__":
    main()
