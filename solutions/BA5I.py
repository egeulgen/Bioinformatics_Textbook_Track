import sys


def overlap_alignment(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for j in range(len(str2))] for i in range(len(str1))]
    backtrack_mat = [[None for j in range(len(str2))] for i in range(len(str1))]

    for j in range(1, len(str2)):
        score_mat[0][j] = score_mat[0][j - 1] - 2
        backtrack_mat[0][j] = "l"

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):

            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] == str2[j] else -2)
            score2 = score_mat[i - 1][j] - 2
            score3 = score_mat[i][j - 1] - 2
            score_mat[i][j] = max(score1, score2, score3)
            if score_mat[i][j] == score1:
                backtrack_mat[i][j] = "d"
            elif score_mat[i][j] == score2:
                backtrack_mat[i][j] = "u"
            elif score_mat[i][j] == score3:
                backtrack_mat[i][j] = "l"

    i = len(str1) - 1
    j = max(range(len(str2)), key=lambda x: score_mat[i][x])
    max_score = score_mat[i][j]

    aligned_1 = aligned_2 = ""
    while backtrack_mat[i][j] is not None:
        direction = backtrack_mat[i][j]
        if direction == "d":
            aligned_1 = str1[i] + aligned_1
            aligned_2 = str2[j] + aligned_2
            i -= 1
            j -= 1
        elif direction == "u":
            aligned_1 = str1[i] + aligned_1
            aligned_2 = "-" + aligned_2
            i -= 1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = str2[j] + aligned_2
            j -= 1

    return max_score, aligned_1, aligned_2


if __name__ == "__main__":
    '''
    Given: Two protein strings v and w, each of length at most 1000.
    Return: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v’ of v and a 
    prefix w’ of w achieving this maximum score. Use an alignment score in which matches count +1 and both the mismatch 
    and indel penalties are 2. (If multiple overlap alignments achieving the maximum score exist, you may return any 
    one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    string1 = input_lines[0]
    string2 = input_lines[1]

    score, alignment1, alignment2 = overlap_alignment(string1, string2)
    print(score)
    print(alignment1)
    print(alignment2)
