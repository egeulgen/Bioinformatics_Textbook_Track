import sys
from BA1C import rev_comp
from BA4A import translate_rna


def substrings_encoding_peptide(dna, peptide):
    k = len(peptide) * 3
    result = []
    for i in range(len(dna) - k + 1):
        substring = dna[i:i + k]
        revc_substring = rev_comp(substring)

        substring = substring.replace("T", "U")
        revc_substring = revc_substring.replace("T", "U")

        if translate_rna(substring) == peptide or translate_rna(revc_substring) == peptide:
            result.append(substring.replace("U", "T"))
    return result


if __name__ == "__main__":
    '''
    Given: A DNA string Text and an amino acid string Peptide.
    Return: All substrings of Text encoding Peptide (if any such substrings exist).
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    Peptide = input_lines[1]

    print("\n".join(substrings_encoding_peptide(Text, Peptide)))
