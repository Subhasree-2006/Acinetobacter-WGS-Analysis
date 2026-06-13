from Bio.Seq import Seq

with open("OXA23_gene.txt") as f:
    seq = f.read().strip()

variants = [
(1888032,"A","G"),
(1888128,"T","C"),
(1888230,"A","C"),
(1888242,"T","C"),
(1888278,"C","T"),
(1888299,"A","G"),
(1888319,"T","C"),
(1888340,"G","A"),
(1888349,"G","T"),
(1888350,"C","A"),
(1888353,"G","A"),
(1888374,"A","G"),
(1888561,"T","A"),
(1888578,"A","G"),
(1888598,"A","T")
]

gene_start = 1887843

for pos, ref, alt in variants:

    rel = pos - gene_start
    codon_start = (rel // 3) * 3

    codon = seq[codon_start:codon_start+3]

    mut = list(codon)
    mut[rel % 3] = alt
    mut = "".join(mut)

    aa1 = str(Seq(codon).translate())
    aa2 = str(Seq(mut).translate())

    codon_no = codon_start // 3 + 1

    print(f"Codon {codon_no}: {codon} -> {mut} | {aa1} -> {aa2}")




