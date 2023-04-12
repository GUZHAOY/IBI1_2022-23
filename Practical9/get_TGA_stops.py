with open('/cygdrive/c/Users/17733/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as f:
    lines = f.readlines()
#Filter for sequences ending in TGA
tga_genes = {}
for line in lines:
    if line.startswith('>'):
        seq_name = line.strip().lstrip('>')
        tga_genes[seq_name] = ''
    else:
        tga_genes[seq_name] += line.strip()

tga_genes = {k: v for k, v in tga_genes.items() if v.endswith('TGA')}
#Write the results to a new file
output_file = 'TGA_genes.fa'
with open(output_file, 'w') as f:
    for k, v in tga_genes.items():
        f.write(f'>{k}\n{v}\n')
