import sys
from BA9I import BurrowsWheelerTransform
from BA9N import create_check_point_array, Count_symbol, PartialSuffixArray, MultiplePatternMatching


def pattern_to_seeds(pattern, d):
    minsize = len(pattern) // (d + 1)

    cut_points = list(range(0, len(pattern) - minsize + 1, minsize))
    cut_points.append(len(pattern))

    seeds = []
    offsets = []
    for i in range(1, len(cut_points)):
        seeds.append(pattern[cut_points[i - 1]: cut_points[i]])
        offsets.append(cut_points[i - 1])
    return seeds, offsets


def find_seed_positions(seed, FirstOccurrence, BWT, check_point_array, partial_suffix_array):
    seed_pos_list = []
    top, bottom = MultiplePatternMatching(FirstOccurrence, BWT, seed, check_point_array)
    if top:
        for idx in range(top, bottom + 1):
            to_add = 0
            while idx not in partial_suffix_array.keys():
                idx = FirstOccurrence[BWT[idx]] + Count_symbol(check_point_array, idx, BWT, BWT[idx])
                to_add += 1
            seed_pos_list.append(partial_suffix_array[idx] + to_add)
    return seed_pos_list


def wrapper(Text, pattern_list, d, C):
    BWT = BurrowsWheelerTransform(Text + '$')

    FirstOccurrence = {}
    for idx, symbol in enumerate(sorted(BWT)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = idx

    check_point_array = create_check_point_array(BWT, C)
    partial_suffix_array = PartialSuffixArray(Text + '$', C)

    positions_list = []
    for pattern in pattern_list:
        ## break pattern into seeds
        seeds_list, offsets_list = pattern_to_seeds(pattern, d)

        # find exact matches and try to extend each seed
        pattern_pos_list = set()
        for candidate_seed, offset in zip(seeds_list, offsets_list):
            seed_pos_list = find_seed_positions(candidate_seed, FirstOccurrence, BWT, check_point_array,
                                                partial_suffix_array)

            for candidate_pos in seed_pos_list:
                pattern_position = candidate_pos - offset

                if pattern_position >= 0 and pattern_position + len(pattern) <= len(Text):
                    approximate_match_flag = True
                    num_mismatch = 0
                    for idx, symbol in enumerate(pattern):
                        if symbol != Text[pattern_position + idx]:
                            num_mismatch += 1
                            if num_mismatch > d:
                                approximate_match_flag = False
                                break
                    if approximate_match_flag:
                        pattern_pos_list.add(pattern_position)

        positions_list += list(pattern_pos_list)

    return sorted(positions_list)


if __name__ == "__main__":
    '''
    Given: A string Text, a collection of strings Patterns, and an integer d.
    Return: All positions in Text where a string from Patterns appears as a substring with at most d mismatches.
    '''
    tmp = sys.stdin.read().splitlines()
    Text = tmp[0]
    pattern_list = [pattern for pattern in tmp[1].split(' ')]
    d = int(tmp[2])

    positions_list = wrapper(Text, pattern_list, d, C=100)
    print(' '.join(str(pos) for pos in positions_list))
