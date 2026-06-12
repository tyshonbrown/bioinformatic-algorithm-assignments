class Node:
    
    def __init__(self, label=None, index=None):
        # The label on the edge leading into this node
        # label of edge leading into node from parent (can be either a string or coordinates within the string provided in the input)
        self.label = label
        self.index = index
        self.children = {}
        
class SuffixTree:
    
    def __init__(self, sequence):
        self.sequence = sequence
        # Root node of the suffix tree
        self.root = Node()
        self.build_tree()
        
    def build_tree(self):
        
        # Insert suffixes one by one
        for i in range(len(self.sequence)):
            suffix = self.sequence[i:]
            #print(suffix)
            self.insert(suffix, i)
            
    
    def insert(self, suffix, index):
        
        current_node = self.root
        
        if suffix[0] not in current_node.children:
            new_node = Node(suffix[0:], index)
            current_node.children[suffix[0]] = new_node
            #self.edges[suffix[0]] = []
        
        else:
            
            child_node = current_node.children[suffix[0]]
            lab = child_node.label
            length = len(suffix)
            
            # find where mismatch occurs
            i = 0
            while i < length:
                if lab[i] != suffix[i]:
                    break
                i += 1
            
            #self.edges[suffix[0]].append(suffix[:i])
         
            split_node = Node(suffix[i:], index)
            child_node.children[index] = split_node
            #current_node.children[index] = split_node
            
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.label:
            print("  " * level + f"Label: {node.label}, Index: {node.index}")
        for child in node.children.values():
            self.print_tree(child, level + 1)
        
    def get_edges(self, node=None, level=0, lst=[]):
        if node is None:
            node = self.root
        if lst is None:
            lst = []
        
        if node.label:
            lst.append(node.label)

        for child in node.children.values():
            self.get_edges(child, level + 1, lst) 

        return lst
        
     
if __name__ == "__main__":
    
    sequence = [] # list of the DNA sequence
    suffixes = []
    
    with open("input", "r") as infile:

        # extracting each full DNA sequence
        for line in infile:
            line = line.strip()
            for char in line:
                sequence.append(char)
    
    tree = SuffixTree(sequence)
    
    
    edges = tree.get_edges()
    #print(edges)
    
    with open("output", 'w') as f:
        for lst in edges:
            f.write(''.join(lst) + '\n')
    