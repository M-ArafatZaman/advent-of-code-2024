import sys
from functools import cache
import tqdm

def get_input():
    data = open(sys.argv[1]).read().splitlines()
    return [(int(entry.split(":")[0]), list(map(int, entry.split(":")[1].strip().split(" ")))) for entry in data]

@cache
def permutate(n, N = ("+", "*")):
    if n == 1:
        return [[x] for x in N]
    else:
        prev = permutate(n-1, N)
        result = []
        for x in prev:
            for y in N:
                result.append(x + [y])
        return result

def evaluate(vals, ops):
    total = vals[0]
    for op in range(len(ops)):
        if ops[op] == "+":
            total += vals[op+1]
        elif ops[op] == "*":
            total *= vals[op+1]
        elif ops[op] == "||":
            total = int(str(total) + str(vals[op+1]))
    return total

def calibrate(data, operators = ("+", "*")):
    calibration = 0
    for entry in tqdm.tqdm(data):
        total, vals = entry
        possibilities = permutate(len(vals)-1, operators)
        for possibility in possibilities:
            ops = list(possibility)
            if evaluate(vals, ops) == total:
                calibration += total
                break
    return calibration

def main():
    data = get_input()
    print(calibrate(data))
    print(calibrate(data, ("+", "*", "||")))


if __name__ == '__main__':
    main()