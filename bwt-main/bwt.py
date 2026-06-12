def decode(last_col):
    
    # sorting the last column to get the first column
    first_col = sorted(last_col, key=lambda x: (x[0] != '$', x[0], x[1]))
    
    current_row = 0
    result = []
    
    while True:
        
        if last_col[current_row][0] == '$':
            break
        
        result.insert(0, last_col[current_row][0])
        current_row = first_col.index(last_col[current_row])
    
    
    # adding $ to the end of the result
    result.append('$')
    
    # writing to result
    with open("output", "w") as file:
        file.write("".join(result))
    
    return
    

if __name__ == "__main__":
    
    # extracting fron the input file
    bwt = []
    with open("input", "r") as infile:
        line = infile.read().strip()
        for char in line:
            bwt.append(char)
      
    
    # Keeping track of the occurrence of characters 
    occurrence_count = {}
    result = [] # an array of (char, occurrence) tuples
    for char in bwt:
        occurrence_count[char] = occurrence_count.get(char, 0) + 1
        result.append((char, occurrence_count[char]))
    
    # call to The Algorithm    
    decode(result)