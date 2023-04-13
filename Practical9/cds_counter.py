import re
#Defining DNA sequence
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
if re.match('ATG',seq): #Find the start codon
    list_number=re.findall(r'TAA|TAG|TGA',seq) #Find the stop codon
    print("The number of possible encoding sequences is",len(list_number)) #Output the number of encoding sequences found
else:
    print(0)
