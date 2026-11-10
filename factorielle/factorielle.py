def factorielle(n: int) -> int:
    """Calcule n! de façon itérative."""
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


def factorielle_rec(n: int) -> int:
    """Calcule n! de façon récursive."""
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")
    return 1 if n <= 1 else n * factorielle_rec(n - 1)


if __name__ == "__main__":
    n = int(input("Entrez n : "))
    print(f"{n}! = {factorielle(n)}")
