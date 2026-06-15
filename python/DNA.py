def solve(path):
    with open(path, "r", encoding="utf-8") as file:
        dna = file.read()
    a = dna.lower().count("a")
    c = dna.lower().count("c")
    g = dna.lower().count("g")
    t = dna.lower().count("t")
    output = f"{a} {c} {g} {t}"
    return output

print(solve("~/Work/rosalind-solutions/data/rosalind_dna.txt"))