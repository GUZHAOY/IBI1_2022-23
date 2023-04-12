# 1. Gets the stop codon entered by the user and uses it to create a new file name.
stop_codon = input("Please enter one of the three stop codons (TAA, TAG or TGA): ")
output_file = f"{stop_codon}_stop_genes.fa"

# 2. The original fasta file is read and the gene sequence ending in the given stop codon is screened.
with open('/cygdrive/c/Users/17733/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    lines = f.readlines()

tga_genes = {}
for line in lines:
    if line.startswith('>'):
        seq_name = line.strip().lstrip('>')
        tga_genes[seq_name] = ''
    else:
        tga_genes[seq_name] += line.strip()

tga_genes = {k: v for k, v in tga_genes.items() if v.endswith(stop_codon)}

# 3. Write the selected sequence to a new file and modify the sequence name.
with open(output_file, 'w') as f:
    for i, (k, v) in enumerate(tga_genes.items()):
        gene_name = k.split()[0]
        cds_count = int(len(v) / 3)
        seq_header = f">{gene_name}_CDS{cds_count}"
        f.write(f"{seq_header}\n{v}\n")
