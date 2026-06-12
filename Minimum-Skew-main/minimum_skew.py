def min_skew():
    
    with open("input", "r") as file:
        dna = file.read().replace("\n", "").strip()

    skew = [0]  # Skew values
    min_skew = 0  # Minimum skew value
    min_positions = []  # positions where skew is minimized

    # Computing the skew values
    for i in range(len(dna)):
        
        # G increases skew by 1
        if dna[i] == 'G':
            skew.append(skew[-1] + 1)
        
        # C decreases skew by 1
        elif dna[i] == 'C':
            skew.append(skew[-1] - 1)
            
        # A or T does nothing to skew
        else:
            skew.append(skew[-1]) 

        # Check if new minimum skew found
        if skew[-1] < min_skew:
            min_skew = skew[-1]
 
    # Get rid of starting value
    skew.pop(0)
    
    # positions of minimal skew value
    for i in range(len(skew)):
        if skew[i] == min_skew:
            min_positions.append(i + 1)
    
    result = " ".join(map(str, min_positions))
    
    with open("output", "w") as outfile:
        outfile.write(result)


if __name__ == "__main__":
    min_skew()