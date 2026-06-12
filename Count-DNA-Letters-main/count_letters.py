def count_letters():
    with open("input", "r") as infile:
        str = infile.read()
        
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    
    for char in str:
        if char == "A":
            count_a += 1
        elif char == "C":
            count_c += 1
        elif char == "G":
            count_g += 1
        elif char == "T":
            count_t += 1
            
    result = f"{count_a} {count_c} {count_g} {count_t}"
    
    with open("output", "w") as outfile:
        outfile.write(result)
    
            
if __name__ == "__main__":
    count_letters()
            