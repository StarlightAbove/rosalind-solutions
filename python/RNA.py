def solve(path):
    with open(path, "r", encoding="utf-8") as file:
        dna = file.read()
    rna = dna.replace("T", "U")
    return rna

print(solve("data/rosalind_rna.txt"))