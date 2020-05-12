import sys
from collections import defaultdict
from BA3G import Eulerian_path


def deBruijn_graph_paired_reads(paired_reads):
    adj_list = defaultdict(list)
    for pair in paired_reads:
        adj_list[(pair[0][:-1], pair[1][:-1])].append((pair[0][1:], pair[1][1:]))
    return adj_list


def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    prefix_string = ''
    suffix_string = ''
    for i, pattern_pair in enumerate(GappedPatterns):
        if i != len(GappedPatterns) - 1:
            prefix_string += pattern_pair[0][0]
            suffix_string += pattern_pair[1][0]
        else:
            prefix_string += pattern_pair[0]
            suffix_string += pattern_pair[1]
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d - 1]:
            return -1
    return prefix_string + suffix_string[len(suffix_string) - k - d - 1:]


def string_reconstruction_read_pairs(k, d, paired_reads):
    adj_list = deBruijn_graph_paired_reads(paired_reads)
    path = Eulerian_path(adj_list)
    return StringSpelledByGappedPatterns(path, k - 1, d)


if __name__ == "__main__":
    '''
    Given: Integers k and d followed by a collection of paired k-mers PairedReads.
    Return: A string Text with (k, d)-mer composition equal to PairedReads. (If multiple answers exist, you may return 
    any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k, d = [int(x) for x in input_lines[0].split()]
    PairedReads = []
    for line in input_lines[1:]:
        PairedReads.append(line.split("|"))

    print(string_reconstruction_read_pairs(k, d, PairedReads))
