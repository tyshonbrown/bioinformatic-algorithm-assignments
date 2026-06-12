
 # GETTING THE DNA SEQUENCE
def get_sequence():
    sequence = []
    
    with open("input", "r") as infile:
        
        # reads each line in the file
        for line in infile:
            line = line.strip()
            
            # make sure only sequence between info lines are read
            if line.startswith(">"):
                continue
                
            # adding each DNA letter to list
            else:
                for char in line:
                    sequence.append(char)
    
    # calling function to get sp values
    sp = get_sp(sequence)
    
    # writing sp values to output file
    with open("output", "w") as outfile:
        outfile.write(" ".join(map(str, sp)))
        
    return

# CALCULATING SP VALUES
def get_sp(sequence):
    
    # j keeps track of the prefix to compare it with i
    j = 0
    n = len(sequence)
    
    # fill sp with 0's to start
    sp = [0] * n
    
    # working from index 1 until end
    for i in range(1, n):

        # if  sequence match is broken, reset j to start
        #if j > 0 and sequence[i] != sequence[j]:
        #    j = 0
        
        # if a prefix match is broken, j is repositioned
        while j > 0 and sequence[i] != sequence[j]:
            j = sp[j - 1]

        # checks a pattern is matching the prefix
        if sequence[i] == sequence[j]:
            j += 1
            sp[i] = j
            
        # if no prefix match
        else:
            sp[i] = 0
            
    return sp


if __name__ == "__main__":
    get_sequence()