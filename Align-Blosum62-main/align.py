def traceback(s1, s2, traceback_matrix):
    a1 = []
    a2 = []
    i, j = len(s1), len(s2)

    while i > 0 or j > 0:
        
        # D in traceback matrix means move Diagonal
        if i > 0 and j > 0 and traceback_matrix[i][j] == 'D':
            a1.append(s1[i - 1])
            a2.append(s2[j - 1])
            i -= 1
            j -= 1
            
        # U in traceback matrix means move Up, sequence 2 has gap (-)
        elif i > 0 and traceback_matrix[i][j] == 'U':
            a1.append(s1[i - 1])
            a2.append('-')
            i -= 1
        
        # Move left, sequence 1 has gap (-)
        else:
            a1.append('-')
            a2.append(s2[j - 1])
            j -= 1

    return ''.join(reversed(a1)), ''.join(reversed(a2))

def construct_matrix(s1, s2, blosum62, score_matrix, traceback_matrix, gap_penalty):
   
    len1, len2 = len(s1), len(s2)
        
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            
            # DIAGONAL Calculation, using the values found in the BLOSUM62 matrix
            match = score_matrix[i - 1][j - 1] + blosum62[s1[i - 1]][s2[j - 1]]
            
            # TOP Calculation using the gap penalty
            delete = score_matrix[i - 1][j] - gap_penalty 
            
            # LEFT Calculation using the gap penalty
            insert = score_matrix[i][j - 1] - gap_penalty

            # Get and store the maximum of three values in the score matrix
            max_score = max(match, delete, insert)
            score_matrix[i][j] = max_score

            # Storing the chosen value in the traceback matrix
            if max_score == match:
                # D = Diagonal
                traceback_matrix[i][j] = 'D'
                
            elif max_score == delete:
                # U = Up
                traceback_matrix[i][j] = 'U'
            else:
                # L = Left
                traceback_matrix[i][j] = 'L'
    
    return

def initialize_matrix(s1, s2, gap_penalty):

    len1, len2 = len(s1), len(s2)

    # Initializing empty score and traceback matrices
    score_matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    traceback_matrix = [[''] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Initialize first row and column with gap penalties
    for i in range(1, len1 + 1):
        
        # Score matrix first column initialization using gap penalty
        score_matrix[i][0] = score_matrix[i - 1][0] - gap_penalty
        
        # Traceback matrix first column of "U" for Up, meaning gap in S2
        traceback_matrix[i][0] = 'U'  # Up (gap in seq2)

    for j in range(1, len2 + 1):
        
        # Score matrix first row initialization using gap penalty
        score_matrix[0][j] = score_matrix[0][j - 1] - gap_penalty
        
        # Traceback matrix first row of "L" for Left, meaning gap in S1
        traceback_matrix[0][j] = 'L'  

    traceback_matrix[0][0] = '0'
    
    return score_matrix, traceback_matrix
    

if __name__ == "__main__":
    
    # Read the two sequences from the input file
    with open('input', 'r') as f:
        sequences = [line.strip() for line in f.readlines()]

    # Read the BLOSUM62 matrix and store it as a dictionary
    blosum62 = {}
    with open('BLOSUM62.txt', 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]
        blosum62_sequence = lines[0]

        for i, row in enumerate(lines[1:]):
            blosum62[blosum62_sequence[i]] = {blosum62_sequence[j]: int(row[j + 1]) for j in range(len(blosum62_sequence))}

    s1 = sequences[0]
    s2 = sequences[1]
    gap_penalty = 5

    # initializing the score matrix and traceback matrix
    score_matrix, traceback_matrix = initialize_matrix(s1, s2, gap_penalty)
    
    # using the blosum62 matrix and gap penalty to construct the score and traceback matrices
    construct_matrix(s1, s2, blosum62, score_matrix, traceback_matrix, gap_penalty)
    
    # Getting the aligned sequences using the traceback matrix
    a1, a2 = traceback(s1, s2, traceback_matrix)
    
    with open("output", "w") as f:
        f.write(str(score_matrix[-1][-1]) + "\n")  # Final alignment score
        f.write(a1 + "\n")
        f.write(a2)
    