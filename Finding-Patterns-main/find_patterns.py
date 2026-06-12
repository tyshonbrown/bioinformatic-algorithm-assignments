def find_pattern():
    with open("input", "r") as infile:
        lines = infile.readlines()
    
    pattern = lines[0].strip()
    text = lines[1].strip()
    
    matches = []
    
    for i in range(len(text) - len(pattern) + 1):
    
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break 
        
        if match:
            matches.append(str(i))
       
    result = " ".join(matches)
    
    with open("output", "w") as outfile:
        outfile.write(result)

if __name__ == "__main__":
    find_pattern()