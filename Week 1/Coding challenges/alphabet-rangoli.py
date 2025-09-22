def print_rangoli(size):
    char = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g',
        8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
        14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
        20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
    }

    finalArr, arr = [], []

    for i in range(n):
        left = '-'.join(char[x] for x in range(n, n - i - 1, -1))
        right = '-'.join(char[x] for x in range(n - i + 1, n + 1))
        if(i != 0):
            arr.append(f"{left}-{right}")
        else:
            arr.append(f"{left}")

    for i in arr:
        finalArr.append(i.center(n * 4 - 3, '-'))

    print('\n'.join(finalArr + finalArr[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)