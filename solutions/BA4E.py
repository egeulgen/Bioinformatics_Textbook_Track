import sys
MASSES = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def cyclospectrum_mass_peptide(peptide):
    spec = [0, sum(peptide)]
    temp = peptide + peptide
    for k in range(1, len(peptide)):
        for i in range(len(peptide)):
            subpeptide = temp[i:i + k]
            spec.append(sum(subpeptide))
    spec.sort()
    return spec


def LinearSpectrum(Peptide):
    PrefixMass = [0]
    for i in range(len(Peptide)):
        temp = PrefixMass[i] + Peptide[i]
        PrefixMass.append(temp)
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum


def expand(peptides):
    new_peptides = []
    for pep in peptides:
        for mass in MASSES:
            new_peptides.append(pep + [mass])
    return new_peptides


def Consistent(Peptide, Spectrum):
    if sum(Peptide) > Spectrum[-1] - MASSES[0]:
        return False
    spec = LinearSpectrum(Peptide)
    for mass in spec:
        if mass not in Spectrum:
            return False
    return True


def cyclopeptide_sequencing(spectrum):
    result = set()
    peptides = [[]]
    while peptides:
        peptides = expand(peptides)
        for peptide in peptides:
            if sum(peptide) == spectrum[-1]:
                if cyclospectrum_mass_peptide(peptide) == spectrum:
                    result.add("-".join(map(str, peptide)))
                peptides = [pep for pep in peptides if pep != peptide]
            elif not Consistent(peptide, spectrum):
                peptides = [pep for pep in peptides if pep != peptide]
    return result


if __name__ == "__main__":
    '''
    Given: A collection of (possibly repeated) integers Spectrum corresponding to an ideal experimental spectrum.
    Return: Every amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).
    '''
    spectrum = [int(x) for x in sys.stdin.readline().strip().split()]

    print(" ".join(cyclopeptide_sequencing(spectrum)))
