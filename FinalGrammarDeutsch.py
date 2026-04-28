"""
Name: Santiago Martin del Campo 
Date : April 28 2026
Project: Context-Free Grammar 
"""

# Import NLTK library
from nltk import CFG
from nltk.parse import ChartParser

# Grammar made
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Pron
VP -> V NP Vrest | V Vrest
Vrest -> PP Vrest |
PP -> Prep NP

Det -> 'der' | 'den' | 'dem' | 'die' | 'das'
N -> 'Mann' | 'Hund' | 'Stock' | 'Frau' | 'Wasser' | 'Milch' | 'Apfel' | 'Kekse' | 'Deutsch' 
V -> 'ist' | 'hat' | 'sieht' | 'trifft' | 'isst' | 'trinkt' | 'geht' | 'kommt' | 'läuft' | 'macht' | 'gibt' | 'nimmt' | 'findet' | 'denkt' | 'sagt' | 'bringt' | 'spielt' | 'fragt' | 'hilft' | 'arbeitet' | 'liebt'
Prep -> 'mit' | 'für' | 'in'
Pron -> 'ich' | 'du' | 'er' | 'sie'
""")

# Parser
parser = ChartParser(grammar)

# input sentence for trying parser, it must match with terminal symnbols
sentence = "der Mann sieht die Frau".split()

# Parse the sentence and generate a tree
trees = list(parser.parse(sentence))

# Output results
print("Sentence:", " ".join(sentence))
print("Number of trees:", len(trees))

# Print tree
for tree in trees:
    print(tree)
    tree.pretty_print()