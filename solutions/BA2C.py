import sys


def probability(pattern, profile):
    indices = {"A": 0, "C": 1, "G": 2, "T": 3}
    prob = 1
    for i, nuc in enumerate(pattern):
        prob *= profile[indices[nuc]][i]
    return prob


def profile_most_probable_kmer(text, profile, k):
    max_prob = 0
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = probability(kmer, profile)
        if prob > max_prob:
            max_prob = prob
            result = kmer
    return result


if __name__ == "__main__":
    '''
    Given: A string Text, an integer k, and a 4 × k matrix Profile.
    Return: A Profile-most probable k-mer in Text. (If multiple answers exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    k = int(input_lines[1])
    profile = [[float(x) for x in line.split()] for line in input_lines[2:]]

    print(profile_most_probable_kmer(Text, profile, k))
