from functools import cache

@cache
def blink(val, num = 1):
    if num == 0: return [val]

    if val == 0:
        return blink(1, num-1)
    elif len(str(val)) % 2 == 0:
        return blink(int(str(val)[:len(str(val))//2]), num - 1) + blink(int(str(val)[len(str(val))//2:]), num - 1)
    else:
        return blink(val * 2024, num - 1)

def solve(data):
    print(sum([len(blink(i, 25)) for i in data]))

def main():
    data = list(map(int, open(0).read().strip().split(" ")))
    print(solve(data))

if __name__ == "__main__":
    main()