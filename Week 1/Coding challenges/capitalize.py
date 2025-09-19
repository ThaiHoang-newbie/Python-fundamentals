import os

def solve(s):
    s = s.split(" ")
    num = 0
    for i in s:
        s[num] = i.capitalize()
        num += 1
    return ' '.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
