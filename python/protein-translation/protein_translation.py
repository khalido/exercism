# %%
from typing import List, Dict

info: Dict[str, str] = {
    "AUG": "Methionine",
    **dict.fromkeys(("UUU", "UUC"), "Phenylalanine"),
    **dict.fromkeys(("UUA", "UUG"), "Leucine"),
    **dict.fromkeys(("UCU", "UCC", "UCA", "UCG"), "Serine"),
    **dict.fromkeys(("UAU", "UAC"), "Tyrosine"),
    **dict.fromkeys(("UGU", "UGC"), "Cysteine"),
    "UGG": "Tryptophan",
    **dict.fromkeys(("UAA", "UAG", "UGA"), "STOP"),
}


def proteins(strand: str) -> List[str]:
    protein_sequence: List[str] = []

    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]

        try:
            protein = info[codon]
        except:
            raise Exception(f"{codon} not present in info table")

        if protein == "STOP":
            break
        else:
            protein_sequence.append(protein)

    return protein_sequence