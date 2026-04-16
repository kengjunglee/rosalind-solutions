
from revc import reverse_complement
from rna import transcribe
from prot import translate
from prot import CODON_TABLE


def proteins_from_rna(rna: str) -> list[str]:
    """
    Find all proteins encoded by ORFs in an RNA string.

    An open reading frame (ORF) begins at an AUG start codon and ends at the
    first stop codon encountered in the same reading frame. Every AUG in the
    string is a candidate start — they may overlap.

    Args:
        rna: An RNA string.

    Returns:
        A list of protein strings, one per ORF that terminates with a stop codon.
        May contain duplicates if two ORFs encode the same protein.
    """
    result: list = []
    for i in range(len(rna)-2):
        if rna[i:i+3] == 'AUG':
            protein = translate(rna[i:])
            if len(protein) * 3 <= len(rna)-i-3:
                result.append(protein)
    return result

def find_all_orf_proteins(dna: str) -> set[str]:
    """
    Find all distinct proteins encoded by ORFs in both strands of a DNA string.

    Considers ORFs on both the given strand and its reverse complement.

    Args:
        dna: A DNA string.

    Returns:
        A set of distinct protein strings from all valid ORFs.
    """
    result: set[str] = set()
    rcdna = reverse_complement(dna)
  
    for protein in proteins_from_rna(transcribe(dna)):
        result.add(protein)
    for protein in proteins_from_rna(transcribe(rcdna)):
        result.add(protein)
    return result
def main() -> None:
    # dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

    # proteins = find_all_orf_proteins(dna)
    # for protein in sorted(proteins):
    #     print(protein)

    # Expected (in any order):
    # M
    # MGMTPRLGLESLLE
    # MLLGSFRLIPKETLIQVAGSSPCNLS
    # MTPRLGLESLLE


    from custom_io import parse_fasta, write_result
    sequences = parse_fasta(__file__)
    dna = sequences[0][1]
    proteins = find_all_orf_proteins(dna)
    output = "\n".join(sorted(proteins))
    print(output)
    write_result(__file__, output)


if __name__ == "__main__":
    main()
