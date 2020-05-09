import sys


def skew(dna_seq):
    return dna_seq.count("G") - dna_seq.count("C")


def minimal_skew(dna_seq):
    all_skew = []
    min_skew = 1e6
    for i in range(len(dna_seq) + 1):
        skw = skew(dna_seq[:i])
        all_skew.append(skw)
        if skw < min_skew:
            min_skew = skw

    idx_list = []
    for i, skw in enumerate(all_skew):
        if skw == min_skew:
            idx_list.append(i)
    return idx_list


if __name__ == "__main__":
    '''
    Given: A DNA string Genome.
    Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
    '''
    input_lines = sys.stdin.read().splitlines()
    Genome = input_lines[0]

    print(" ".join(map(str, minimal_skew(Genome))))
