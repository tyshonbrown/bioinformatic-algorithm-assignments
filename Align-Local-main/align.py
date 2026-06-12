def trace(s1, s2, traceback, max_pos):
    align1 = [] # s1 alignment
    align2 = [] # s2 alignment
    i, j = max_pos
    
    while traceback[i][j] is not None:
        prev_i, prev_j = traceback[i][j]
        
        # NO GAP
        if prev_i == i - 1 and prev_j == j - 1:
            align1.append(s1[i-1])
            align2.append(s2[j-1])
            
        # GAP in s2
        elif prev_i == i - 1:
            align1.append(s1[i-1])
            align2.append('-')
            
        # GAP in s1
        else:
            align1.append('-')
            align2.append(s2[j-1])
            
        i, j = prev_i, prev_j
    
    return align1, align2


def construct(s1, s2, pam250_matrix, gap_penalty):
    len1 = len(s1)
    len2 = len(s2)
    
    # initializing the matrix and the traceback matrix
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    traceback = [[None] * (len2 + 1) for _ in range(len1 + 1)]
    
    max_score = 0
    max_position = (0, 0)
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            
            # DIAGONAL match/mismatch calculation, using the values found in the PAM250 matrix
            match = matrix[i-1][j-1] + pam250_matrix[s1[i-1]][s2[j-1]]
            
            # TOP delete Calculation using the gap penalty
            delete = matrix[i-1][j] - gap_penalty
            
            # LEFT Calculation using the gap penalty
            insert = matrix[i][j-1] - gap_penalty
            
            # Get and store the maximum of three values in the score matrix
            matrix[i][j] = max(0, match, delete, insert)

            # storing the values of i and j based on the calculations
            if matrix[i][j] == match:
                traceback[i][j] = (i-1, j-1)
                
            elif matrix[i][j] == delete:
                traceback[i][j] = (i-1, j)
                
            elif matrix[i][j] == insert:
                traceback[i][j] = (i, j-1)
                
            else:
                traceback[i][j] = None

            # update maximum score and position
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_position = (i, j)

    # call to traceback function to construct the alignment of s1 and s2
    align1, align2 = trace(s1, s2, traceback, max_position)

    return max_score, ''.join(reversed(align1)), ''.join(reversed(align2))
    

if __name__ == "__main__":
    
    # Read the two sequences from the input file
    with open('input', 'r') as f:
        sequences = [line.strip() for line in f.readlines()]

    # Read the PAM250 matrix and store it as a dictionary
    pam250 = {}
    with open('PAM250.txt', 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]
        pam250_sequence = lines[0]

        for i, row in enumerate(lines[1:]):
            pam250[pam250_sequence[i]] = {pam250_sequence[j]: int(row[j + 1]) for j in range(len(pam250_sequence))}

    s1 = sequences[0]
    s2 = sequences[1]
    gap_penalty = 5
    
    # algorithm call
    score, align1, align2 = construct(s1, s2, pam250, gap_penalty)
    
    with open('output', 'w') as f:
        f.write(f"{score}\n{align1}\n{align2}")
    
    