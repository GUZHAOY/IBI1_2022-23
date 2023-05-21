import pandas as pd
import re

def align_sequences(seq1, seq2, matrix):
    score = 0
    identity = 0
    for i in range(len(seq1)):
        amino_acid1 = seq1[i]
        amino_acid2 = seq2[i]
        score += matrix.loc[amino_acid1, amino_acid2]
        if amino_acid1 == amino_acid2:
            identity += 1
    return score, identity

def read_sequence_from_file(filename):
    with open(filename) as file:
        content = file.read()
        sequence = re.sub("^.+?\n", "", content)
        sequence = re.sub("\n", "", sequence)
    return sequence

# Read BLOSUM matrix
matrix = pd.read_excel("BLOSUM.xlsx", index_col="First")

# Read sequences from files
human_sequence = read_sequence_from_file('ACE2_human.fa')
mouse_sequence = read_sequence_from_file('ACE2_mouse.fa')
cat_sequence = read_sequence_from_file('ACE2_cat.fa')

# Perform sequence alignments
alignment1 = align_sequences(mouse_sequence, cat_sequence, matrix)
alignment2 = align_sequences(mouse_sequence, human_sequence, matrix)
alignment3 = align_sequences(cat_sequence, human_sequence, matrix)

# Print results
print("Alignment between mouse and cat:", alignment1)
print("Alignment between mouse and human:", alignment2)
print("Alignment between cat and human:", alignment3)
