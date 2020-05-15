import sys


def edit_distance(str1, str2):
    str1 = "-" + str1
    str2 = "-" + str2

    score_mat = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

    for j in range(len(str2)):
        score_mat[0][j] = j

    for i in range(len(str1)):
        score_mat[i][0] = i

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            score1 = score_mat[i - 1][j - 1] + (1 if str1[i] != str2[j] else 0)
            score2 = score_mat[i - 1][j] + 1
            score3 = score_mat[i][j - 1] + 1
            score_mat[i][j] = min(score1, score2, score3)

    return score_mat[len(str1) - 1][len(str2) - 1]


if __name__ == "__main__":
    '''
    Given: Two amino acid strings.
    Return: The edit distance between these strings.
    '''
    input_lines = sys.stdin.read().splitlines()
    string1 = input_lines[0]
    string2 = input_lines[1]

    print(edit_distance(string1, string2))
