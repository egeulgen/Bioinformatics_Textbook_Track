import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
            'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}


def printScoreMat(Score, prefixMasses, spectral_vector, k):
    for t in range(-2, k + 1):
        if t == -2:
            tmp = [str(x) for x in spectral_vector]
            for idx in range(len(tmp)):
                s = tmp[idx]
                if len(s) == 1:
                    s = ' ' + s
                    tmp[idx] = s
            tmp = ['   '] + tmp
            print(' '.join(tmp))
            print(' ')
            print(' ')
        elif t == -1:
            tmp = [str(i) for i in range(len(spectral_vector))]
            for idx in range(len(tmp)):
                s = tmp[idx]
                if len(s) == 1:
                    s = ' ' + s
                    tmp[idx] = s
            tmp = ['   '] + tmp
            print(' '.join(tmp))
        else:
            for i in prefixMasses:
                row = []
                for j in range(-1, len(spectral_vector)):
                    if j == -1:
                        row.append((str(i) if i >= 10 else ' ' + str(i)) + ' ')
                    else:
                        score = Score[i][j][t]
                        if score < -1e5:
                            score = 'XX'
                        elif len(str(score)) == 1:
                            score = ' ' + str(score)
                        row.append(str(score))
                print(' '.join(row))
            print(' ')
    return None


def SpectralAlignment(peptide, spectral_vector, k):
    spectral_vector.insert(0, 0)

    ## Calculate prefix masses
    prefixMasses = [0]
    for i in range(len(peptide)):
        prefix = peptide[:i + 1]
        mass = 0
        for aa in prefix:
            mass += aa_table[aa]
        prefixMasses.append(mass)

    ## Create diff array
    diff = {}
    for i in range(1, len(prefixMasses)):
        diff[prefixMasses[i]] = prefixMasses[i] - prefixMasses[i - 1]

    ## Initiliaze scores
    Score = {}
    for i in prefixMasses:
        Score[i] = {}
        for j in range(len(spectral_vector)):
            Score[i][j] = {}
            for t in range(k + 1):
                Score[i][j][t] = -float("inf")
    Score[0][0][0] = 0

    ## Calculate scores
    for i in prefixMasses[1:]:
        for j in range(len(spectral_vector)):
            for t in range(k + 1):
                if (t == 0) and (i - diff[i] >= 0) and (j - diff[i] >= 0):
                    Score[i][j][t] = spectral_vector[j] + Score[i - diff[i]][j - diff[i]][t]
                elif (t > 0) and (i - diff[i] >= 0) and (j - diff[i] >= 0):
                    Score[i][j][t] = spectral_vector[j] + max(Score[i - diff[i]][j - diff[i]][t], max(
                        [Score[i - diff[i]][j_star][t - 1] for j_star in range(j)]))
                elif (t > 0) and (i - diff[i] >= 0) and (j > 0):
                    Score[i][j][t] = spectral_vector[j] + max(
                        [Score[i - diff[i]][j_star][t - 1] for j_star in range(j)])

    # printScoreMat(Score, prefixMasses, spectral_vector, k)

    ## Find max score layer
    max_score = -float("inf")
    for t in range(k + 1):
        current = Score[prefixMasses[-1]][len(spectral_vector) - 1][t]
        if current > max_score:
            max_score = current
            max_layer = t

    ## Backtrace
    layer = max_layer
    column = len(spectral_vector) - 1

    result = ''
    for i in range(len(peptide), 0, -1):
        pre = prefixMasses[i]
        if (column - diff[pre] >= 0) and (
                Score[pre][column][layer] == spectral_vector[column] + Score[pre - diff[pre]][column - diff[pre]][
            layer]):
            column -= diff[pre]
            result = peptide[i - 1] + result
        else:
            tmp = [Score[pre - diff[pre]][j_star][layer - 1] for j_star in range(column)]
            idx = tmp.index((max(tmp)))
            modif = column - idx - diff[pre]
            if modif > 0:
                result = peptide[i - 1] + '(+' + str(modif) + ')' + result
            else:
                result = peptide[i - 1] + '(' + str(modif) + ')' + result
            column = idx
            layer -= 1

    return result


if __name__ == "__main__":
    '''
    Given: A peptide Peptide, a spectral vector Spectrum', and an integer k.
    Return: A peptide Peptide' related to Peptide by up to k modifications with maximal score against Spectrum' out of 
    all possibilities.
    '''
    tmp = sys.stdin.read().splitlines()
    peptide = tmp[0]
    spectral_vector = [int(x) for x in tmp[1].rstrip().split(' ')]
    k = int(tmp[2])

    print(SpectralAlignment(peptide, spectral_vector, k))
