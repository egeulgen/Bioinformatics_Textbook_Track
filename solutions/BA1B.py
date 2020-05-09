import sys


def most_freq_kmers(text, k):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        if kmer not in count_dict:
            count_dict[kmer] = 1
        else:
            count_dict[kmer] += 1

    max_freq = max(count_dict.values())
    return [kmer for kmer, count in count_dict.items() if count == max_freq]


if __name__ == "__main__":
    '''
    Given: A DNA string Text and an integer k.
    Return: All most frequent k-mers in Text (in any order).
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    k = int(input_lines[1])
    print(" ".join(most_freq_kmers(Text, k)))
