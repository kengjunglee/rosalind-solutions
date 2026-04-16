# Monoisotopic masses of the 20 standard amino acid residues.
# A residue mass is the mass of the amino acid minus water (lost during peptide bond formation).
MONOISOTOPIC_MASS: dict[str, float] = {
    "A": 71.03711,  "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146,  "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276,  "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841,  "W": 186.07931, "Y": 163.06333,
}


def protein_mass(protein: str) -> float:
    """
    Calculate the monoisotopic mass of a protein string.

    The mass is the sum of residue masses of all amino acids. Residue masses
    account for the water molecule lost when each amino acid forms a peptide bond,
    so no additional correction is needed.

    Args:
        protein: A protein string using single-letter amino acid codes.

    Returns:
        The monoisotopic mass of the protein, rounded to 3 decimal places.
    """
    result = 0.0
    for amino_acid in protein:
        result += MONOISOTOPIC_MASS[amino_acid]
        
    return result


def main() -> None:
    # protein = "SKADYEK"

    # mass = protein_mass(protein)
    # print(round(mass, 3))

    # Expected: 821.392


    from custom_io import read_dataset, write_result
    protein = read_dataset(__file__)
    mass = round(protein_mass(protein), 3)
    print(mass)
    write_result(__file__, str(mass))


if __name__ == "__main__":
    main()
