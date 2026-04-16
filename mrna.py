from prot import CODON_TABLE

codon_count: dict[str, int]={}
for codon, amino_acid in CODON_TABLE.items():
    if amino_acid not in codon_count:
        codon_count[amino_acid] = 0
    codon_count[amino_acid] += 1

def count_mrna_sources(protein: str) -> int:
    """
    Count the number of distinct mRNA strings that could encode a given protein.

    For each amino acid in the protein, multiply by the number of codons that
    encode it. Then multiply by the number of stop codons, since the mRNA must
    end with one. Return the result modulo 1,000,000.

    Args:
        protein: A protein string using single-letter amino acid codes.

    Returns:
        The number of mRNA strings that could encode the protein, modulo 1,000,000.
    """
    result = codon_count[""]
    for amino_acid in protein:
        result *= codon_count[amino_acid]
    
    return result % 1000000


def main() -> None:
    # protein = "MA"

    # count = count_mrna_sources(protein)
    # print(count)

    # M is encoded by 1 codon (AUG)
    # A is encoded by 4 codons (GCU, GCC, GCA, GCG)
    # There are 3 stop codons (UAA, UAG, UGA)
    # Total: 1 * 4 * 3 = 12


    from custom_io import read_dataset, write_result
    protein = read_dataset(__file__)
    count = count_mrna_sources(protein)
    print(count)
    write_result(__file__, str(count))


if __name__ == "__main__":
    main()
