import sys

BLOSUM62 = {
    ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
    ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
    ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
    ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
    ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
    ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
    ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
    ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
    ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
    ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
    ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
    ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
    ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
    ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
    ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
    ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
    ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
    ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
    ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
    ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
    ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
    ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
    ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
    ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
    ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
    ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
    ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
    ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
    ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
    ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
    ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
    ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
    ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
    ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
    ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
    ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
    ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
    ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
    ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
    ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
    ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
    ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
    ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
    ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
    ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
    ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
    ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
    ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
    ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
    ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
    ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
    ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
    ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
    ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
    ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
    ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
    ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
    ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
    ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
    ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
    ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
    ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
    ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
    ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
    ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
    ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
    ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
    ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
    ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
}


def global_alignment_with_affine_gap(v, w, gap_open=11, gap_extend=1):
    v = "-" + v
    w = "-" + w

    ## Initialize Score Matrices
    Middle = [[0 for _ in range(len(w))] for _ in range(len(v))]
    Lower = [[0 for _ in range(len(w))] for _ in range(len(v))]
    Upper = [[0 for _ in range(len(w))] for _ in range(len(v))]

    Middle[1][0] = -gap_open
    Middle[0][1] = -gap_open
    for i in range(2, len(Middle)):
        Middle[i][0] = Middle[i - 1][0] - gap_extend
    for j in range(2, len(Middle[0])):
        Middle[0][j] = Middle[0][j - 1] - gap_extend

    for j in range(len(Lower[0])):
        Lower[0][j] = -1e6
    for i in range(0, len(Lower)):
        Lower[i][0] = Middle[i][0]
    for i in range(len(Upper)):
        Upper[i][0] = -1e6
    for j in range(0, len(Upper[0])):
        Upper[0][j] = Middle[0][j]

    ## Initialize Backtrack Matrices
    BacktrackM = [["d" for _ in range(len(w))] for _ in range(len(v))]
    BacktrackL = [["u" for _ in range(len(w))] for _ in range(len(v))]
    BacktrackU = [["l" for _ in range(len(w))] for _ in range(len(v))]

    for i in range(len(BacktrackM)):
        BacktrackM[i][0] = "u"
    for j in range(len(BacktrackM[0])):
        BacktrackM[0][j] = "l"

    for j in range(len(BacktrackL[0])):
        BacktrackL[0][j] = "l"
    for i in range(len(BacktrackU)):
        BacktrackU[i][0] = "u"

    BacktrackM[0][0] = None
    BacktrackL[0][0] = None
    BacktrackU[0][0] = None

    for i in range(1, len(v)):
        for j in range(1, len(w)):
            # lower
            Lower[i][j] = max(Lower[i - 1][j] - gap_extend, Middle[i - 1][j] - gap_open)
            if Lower[i][j] == Lower[i - 1][j] - gap_extend:
                BacktrackL[i][j] = "u"
            else:
                BacktrackL[i][j] = "d"
            # upper
            Upper[i][j] = max(Upper[i][j - 1] - gap_extend, Middle[i][j - 1] - gap_open)
            if Upper[i][j] == Upper[i][j - 1] - gap_extend:
                BacktrackU[i][j] = "l"
            else:
                BacktrackU[i][j] = "d"
            # middle
            if (v[i], w[j]) in BLOSUM62:
                key = (v[i], w[j])
            else:
                key = (w[j], v[i])
            diag = Middle[i - 1][j - 1] + BLOSUM62[key]
            Middle[i][j] = max([diag, Upper[i][j], Lower[i][j]])

            if Middle[i][j] == diag:
                BacktrackM[i][j] = "d"
            elif Middle[i][j] == Lower[i][j]:
                BacktrackM[i][j] = "u"
            else:
                BacktrackM[i][j] = "l"

    i = len(BacktrackM) - 1
    j = len(BacktrackM[0]) - 1
    aligned1 = ""
    aligned2 = ""
    current_layer = "M"
    while BacktrackM[i][j] is not None:
        if current_layer == "M":
            if BacktrackM[i][j] == "d":
                aligned1 = v[i] + aligned1
                aligned2 = w[j] + aligned2
                i -= 1
                j -= 1
            elif BacktrackM[i][j] == "u":
                current_layer = "L"
            else:
                current_layer = "U"

        elif current_layer == "L":
            if BacktrackL[i][j] == "u":
                aligned1 = v[i] + aligned1
                aligned2 = "-" + aligned2
                i -= 1
            elif BacktrackL[i][j] == "d":
                aligned1 = v[i] + aligned1
                aligned2 = "-" + aligned2
                i -= 1
                current_layer = "M"
            else:
                current_layer = "M"

        elif current_layer == "U":
            if BacktrackU[i][j] == "l":
                aligned1 = "-" + aligned1
                aligned2 = w[j] + aligned2
                j -= 1
            elif BacktrackL[i][j] == "d":
                aligned1 = "-" + aligned1
                aligned2 = w[j] + aligned2
                j -= 1
                current_layer = "M"
            else:
                current_layer = "M"

    return Middle[len(v) - 1][len(w) - 1], aligned1, aligned2


if __name__ == "__main__":
    '''
    Given: Two amino acid strings v and w (each of length at most 100).
    Return: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum 
    score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.
    '''
    input_lines = sys.stdin.read().splitlines()
    string1 = input_lines[0]
    string2 = input_lines[1]

    score, alignment1, alignment2 = global_alignment_with_affine_gap(string1, string2)
    print(score)
    print(alignment1)
    print(alignment2)

