import sys
MASSES=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]


def CountPeptides(Mass):
    NumPeptides={}
    for i in range(57):
        NumPeptides[i] = 0

    for mass in range(57, Mass + 1):
        NumPeptides[mass] = MASSES.count(mass)
        for int_mass in MASSES:
            if mass >= int_mass:
                if NumPeptides[mass - int_mass] > 0:
                    NumPeptides[mass] += NumPeptides[mass - int_mass]

    return NumPeptides[Mass]


if __name__ == "__main__":
    '''
    Given: An integer m.
    Return: The number of linear peptides having integer mass m.
    '''
    m = int(sys.stdin.readline().strip())

    print(CountPeptides(m))
