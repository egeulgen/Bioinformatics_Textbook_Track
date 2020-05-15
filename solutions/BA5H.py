import sys


def fitting_alignment(str1, str2, indel_penalty=1):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    backtrack_mat = [[None for _ in range(len(str2))] for _ in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] == str2[j] else - 1)
            score2 = score_mat[i - 1][j] - indel_penalty
            score3 = score_mat[i][j - 1] - indel_penalty
            score_mat[i][j] = max(score1, score2, score3)
            if score_mat[i][j] == score1:
                backtrack_mat[i][j] = "d"
            elif score_mat[i][j] == score2:
                backtrack_mat[i][j] = "u"
            elif score_mat[i][j] == score3:
                backtrack_mat[i][j] = "l"

    j = len(str2) - 1
    i = max(enumerate([score_mat[row][j] for row in range(len(str2) - 1, len(str1) - 1)]), key=lambda x: x[1])[0] + len(str2) - 1
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
    Given: Two DNA strings v and w, where v has length at most 10000 and w has length at most 1000.
    Return: The maximum score of a fitting alignment of v and w, followed by a fitting alignment achieving this maximum 
    score. Use the simple scoring method in which matches count +1 and both the mismatch and indel penalties are equal 
    to 1. (If multiple fitting alignments achieving the maximum score exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    string1 = input_lines[0]
    string2 = input_lines[1]

    score, alignment1, alignment2 = fitting_alignment(string1, string2)
    print(score)
    print(alignment1)
    print(alignment2)
