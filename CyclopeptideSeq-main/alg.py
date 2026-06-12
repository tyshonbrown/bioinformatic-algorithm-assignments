from collections import Counter

AMINO_ACID_MASSES = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def linear_spectrum(peptide):
    # computing prefix sums
    prefix = [0]
    for mass in peptide:
        prefix.append(prefix[-1] + mass)
    
    # linear spectrum construction
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix[j] - prefix[i])
    
    return sorted(spectrum)

def theoretical_spectrum(peptide):
    spectrum = [0]
    
    for l in range(1, len(peptide)):
        for s in range(len(peptide)):
            subpeptide = peptide[s:s + l]
            
            # wrap around
            if len(subpeptide) < l:
                subpeptide += peptide[:(s + l) % len(peptide)]
            
            # add total mass of subpeptide to the spectrum
            spectrum.append(sum(subpeptide))
    
    spectrum.append(sum(peptide))
    return sorted(spectrum)
    
    
def is_compatible(linear_spec, experimental_spec):
    
    # get counts of each element in the spectrum
    lin_spec_counts = Counter(linear_spec)
    exp_spec_counts = Counter(experimental_spec)
    
    for mass in lin_spec_counts:
        if lin_spec_counts[mass] > exp_spec_counts.get(mass, 0):
            return False
    return True

def expand(peptides):
    if not peptides:
        return [[mass] for mass in AMINO_ACID_MASSES]
    return [pep + [mass] for pep in peptides for mass in AMINO_ACID_MASSES]

def BBCyclopeptideSequencing(S):
    # largest mass in S
    parent_mass = max(S)
    
    candidate_peptides = [[]]
    final_peptides = []
    
    while candidate_peptides:
        
        candidate_peptides = expand(candidate_peptides)
        next_candidates = []
        
        for cp in candidate_peptides:
            # check total mass of the peptide cp
            total_mass = sum(cp)
            
            # valid peptide found, add it to final peptides
            if total_mass == parent_mass:
                if Counter(theoretical_spectrum(cp)) == Counter(S):
                    final_peptides.append(cp)
                
            # possibility of valid peptide, so added to next candidates    
            elif total_mass < parent_mass and is_compatible(linear_spectrum(cp), S):
                next_candidates.append(cp)
        
        # look at the next possible candidates
        candidate_peptides = next_candidates
    
    return final_peptides

if __name__ == "__main__":
    
    with open("input", "r") as file:
        content = file.read().strip()
        experimental_spectrum = list(map(int, content.split()))
        
    result = BBCyclopeptideSequencing(experimental_spectrum)
    formatted = ["-".join(map(str, pep)) for pep in result]
    
    with open("output", "w") as f:
        f.write(" ".join(formatted))
    