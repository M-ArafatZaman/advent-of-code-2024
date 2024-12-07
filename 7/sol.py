import sys
from functools import cache

def get_input():
    data = open(sys.argv[1]).read().splitlines()
    return [(int(entry.split(":")[0]), list(map(int, entry.split(":")[1].strip().split(" ")))) for entry in data]

def permutate(n):
    if n == 1:
        return [["+"], ["*"]]
    else:
        prev = permutate(n-1)
        return [x + ["+"] for x in prev] + [x + ["*"] for x in prev]

def evaluate(vals, ops):
    total = vals[0]
    for op in range(len(ops)):
        if ops[op] == "+":
            total += vals[op+1]
        else:
            total *= vals[op+1]
    return total

def part1(data):
    calibration = 0
    for entry in data:
        total, vals = entry
        possibilities = permutate(len(vals)-1)
        for possibility in possibilities:
            ops = list(possibility)
            if evaluate(vals, ops) == total:
                calibration += total
                break
    return calibration
        

def part2(data):
    pass

def main():
    data = get_input()
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()