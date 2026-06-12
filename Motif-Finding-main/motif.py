def score(motifs):
    
    if not motifs:
        return 0
    
    score = 0
    for i in range(len(motifs[0])):  
        column = [motifs[j][i] for j in range(len(motifs))]  
        score += min(sum(nuc != base for nuc in column) for base in "ACGT")  

    return score

def matrix_prob(matrix, n):
    m = [[num / n for num in row] for row in matrix]
    return m
    
# finding the most probable kmer of a sequence given the profile
def probable_kmer(seq, prof, k):
    
    # nucleotide and its corresponding index
    nuc_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    best_kmer, max_prob = None, -1 
    
    # look at each kmer in the given sequence
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        prob = 1
        
        # calculating the probability
        for j, nucleotide in enumerate(kmer):
            prob *= prof[j][nuc_index[nucleotide]]

        # updating highest prob and most probable kmer
        if prob > max_prob:
            max_prob, best_kmer = prob, kmer
            
    return best_kmer
    
# the profile of a motif
def profile(motifs):
    
    num_motifs = len(motifs)

    return [
        # calculate the probabilities
        [(col.count(nuc) + 1) / (num_motifs + 4) for nuc in 'ACGT']
        for col in zip(*motifs)
    ]

def algorithm(sequences, k, t):
    
    # hold score and motifs of most probable kmers
    result = [t*k, None]
    
    # look at each kmer in first string
    for i in range(len(sequences[0])-k+1):
        
        # motifs as each kmer in first dna sequence and profile
        motifs = [sequences[0][i:i+k]]
        prof = profile(motifs)
        
        for j in range(1, t):
            motifs.append(probable_kmer(sequences[j], prof, k))
            prof = profile(motifs)
            
        # update score and motifs
        curr_score = score(motifs)
        if curr_score < result[0]:
            result = [curr_score, motifs] 

    return result[1]

def extract():
    
    first_line = False
    sequences = [] # list of the DNA sequences
    
    with open("input", "r") as infile:
        first_line = infile.readline().strip()
        # get k and t from input file
        k, t = map(int, first_line.split())

        # extracting each full DNA sequence
        for line in infile:
            line = line.strip()
            seq = []
            for char in line:
                seq.append(char)
            sequences.append(seq)
    
    # running the algorithm
    result = algorithm(sequences, k, t)    
    motifs = [''.join(s) for s in result]
    
    with open("output", "w") as file:
        file.write("\n".join(motifs) + "\n")
        
    return
            
if __name__ == "__main__":
    extract()