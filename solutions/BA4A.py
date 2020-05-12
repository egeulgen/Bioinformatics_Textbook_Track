import sys

bases = "UCAG"
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
CODON_TABLE = dict(zip(codons, amino_acids))


def translate_rna(rna):
    protein = ""
    idx = 0
    codon = rna[idx:idx + 3]
    while CODON_TABLE[codon] != "*":
        protein += CODON_TABLE[codon]
        idx += 3
        codon = rna[idx:idx + 3]
    return protein


if __name__ == "__main__":
    '''
    Given: An RNA string Pattern.
    Return: The translation of Pattern into an amino acid string Peptide.
    '''
    Pattern = sys.stdin.read().splitlines()[0]

    print(translate_rna(Pattern))
