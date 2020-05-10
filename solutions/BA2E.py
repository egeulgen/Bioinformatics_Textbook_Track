import sys
from BA1G import hamming_dist


def probability(pattern, profile):
    prob = 1
    for i, nuc in enumerate(pattern):
        prob *= profile[nuc][i]
    return prob


def profile_most_probable_kmer(text, profile, k):
    max_prob = -1
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prob = probability(kmer, profile)
        if prob > max_prob:
            max_prob = prob
            result = kmer
    return result

def GreedyMotifSearch(DNA_list, k, t):
    BestMotifs = [dna[0:k] for dna in DNA_list]
    LowestScore = CalculateScore(BestMotifs)
    DNA = DNA_list[0]
    for i in range(len(DNA) - k + 1):
        Motifs = [DNA[i:i + k]]
        for j in range(1, t):
            profile = FormProfile(Motifs)
            Motifs.append(profile_most_probable_kmer(DNA_list[j], profile, k))
        CurrentScore = CalculateScore(Motifs)
        if CurrentScore < LowestScore:
            BestMotifs = Motifs
            LowestScore = CurrentScore
    return BestMotifs


def FormProfile(TextList, pseudocount=1):
    if type(TextList) != list:
        TextList = [TextList]
    t = len(TextList)
    k = len(TextList[0])
    profile = {'A': [pseudocount] * k, 'C': [pseudocount] * k, 'G': [pseudocount] * k, 'T': [pseudocount] * k}
    for i in range(k):
        for j in range(t):
            profile[TextList[j][i]][i] += 1
    return profile


def CalculateScore(Motifs):
    k = len(Motifs[0])
    profile = FormProfile(Motifs)
    consensus = ''
    for i in range(k):
        most_freq = 0
        for nuc in ['A', 'C', 'G', 'T']:
            if profile[nuc][i] > most_freq:
                most_freq = profile[nuc][i]
                to_add = nuc
        consensus += to_add
    score = 0
    for motif in Motifs:
        score += hamming_dist(consensus, motif)
    return score


if __name__ == "__main__":
    '''
    Given: Integers k and t, followed by a collection of strings Dna.
    Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t) with pseudocounts. 
    If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, t = [int(x) for x in input_lines[0].split()]
    DNA_list = input_lines[1:]
    print("\n".join(GreedyMotifSearch(DNA_list, k, t)))
