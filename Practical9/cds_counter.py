import re
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
if re.match('ATG',seq):
    list_number=re.findall(r'TAA|TAG|TGA',seq)
    print(len(list_number))
else:
    print(0)
