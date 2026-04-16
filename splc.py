from prot import translate
from rna import transcribe

def remove_substring(s: str, pattern: str) -> str:
    """
    Return a copy of s with all non-overlapping occurrences of pattern removed.

    Args:
        s: The string to search within.
        pattern: The substring to remove.

    Returns:
        The string with all occurrences of pattern removed.
    """
    n = len(s)
    p = len(pattern)
    i = 0
    result = []
    
    while i < n:
            if i+p <= n and s[i:i+p]==pattern:
                i += p
            else:
                result.append(s[i])
                i += 1     

    return "".join(result)  
        

def splice(dna: str, introns: list[str]) -> str:
    """
    Remove all intron sequences from a DNA string, leaving only the exons.

    In real cells, pre-mRNA is processed by the spliceosome, which removes
    introns and joins exons before translation.

    Args:
        dna: The full pre-mRNA DNA sequence.
        introns: A list of intron sequences to remove.

    Returns:
        The spliced DNA string with all introns removed.
    """
    for pattern in introns:
        dna = remove_substring(dna, pattern)
    return dna

def splice_and_translate(dna: str, introns: list[str]) -> str:
    """
    Remove introns from a DNA string, transcribe to RNA, and translate to protein.

    Args:
        dna: The pre-mRNA DNA sequence.
        introns: A list of intron sequences to remove.

    Returns:
        The protein string encoded by the spliced mRNA.
    """
    
    exon_dna = splice(dna, introns)
    rna = transcribe(exon_dna)
    return translate(rna)
    


def main() -> None:
    # Rosalind sample dataset
    # dna = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
    # introns = [
    #     "ATCGGTCGAA",
    #     "ATCGGTCGAGCGTGT",
    # ]

    # protein = splice_and_translate(dna, introns)
    # print(protein)

    # Expected: MVYIADKQHVASSPCNLS (approximately — depends on exact dataset)


    from custom_io import parse_fasta, write_result
    sequences = parse_fasta(__file__)
    dna = sequences[0][1]
    introns = []
    for _, seq in sequences[1:]:
        introns.append(seq)
    protein = splice_and_translate(dna, introns)
    print(protein)
    write_result(__file__, protein)


if __name__ == "__main__":
    main()
