import sys
from random import randint

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


def RandomizedMotifSearch(DNA_list, k, t):
    Motifs = []
    for dna in DNA_list:
        idx = randint(0, len(dna) - k)
        Motifs.append(dna[idx:idx + k])
    BestMotifs = Motifs
    while True:
        profile = FormProfile(Motifs)
        Motifs = []
        for dna in DNA_list:
            Motifs.append(profile_most_probable_kmer(dna, profile, k))
        if CalculateScore(Motifs) < CalculateScore(BestMotifs):
            BestMotifs = Motifs
        else:
            return BestMotifs


if __name__ == "__main__":
    '''
    Given: Positive integers k and t, followed by a collection of strings Dna.
    Return: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1000 times. Remember to use 
    pseudocounts!
    '''
    input_lines = sys.stdin.read().splitlines()
    k, t = [int(x) for x in input_lines[0].split()]
    DNA_list = input_lines[1:]

    best_score = float("Inf")
    for _ in range(1000):
        result = RandomizedMotifSearch(DNA_list, k, t)
        current_score = CalculateScore(result)
        if current_score <= best_score:
            best_score = current_score
            best_result = result

    print("\n".join(best_result))
