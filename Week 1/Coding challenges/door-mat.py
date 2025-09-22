n, m = map(int, input().split())
base = ".|."
baseCharacters = "-"
centreText = "welcome"

def halfOfMat(n, m, base, baseCharacters):
    arr = []
    half = int((n-1) / 2)

    for i in range(1, half*2, 2):
        arr.append(f"{((m - len(base*i)) // 2) * baseCharacters}{base*i}{((m - len(base*i)) // 2) * baseCharacters}")
    return arr

def reverthalfOfMat(arr):
    revertArr = []
    for i in range(len(arr)):
        revertArr.append(arr.pop())
    return revertArr

def middleOfMat(m, centreText):
    padding = (m - len(centreText))// 2
    return f"{baseCharacters * padding}{centreText.upper()}{baseCharacters * padding}"


print("\n".join(halfOfMat(n, m, base, baseCharacters)))
print(middleOfMat(m, centreText))
print("\n".join(reverthalfOfMat(halfOfMat(n, m, base, baseCharacters))))