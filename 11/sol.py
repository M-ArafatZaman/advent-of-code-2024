import tqdm

def part1(data):
    arr = list(data)
    BLINK = 25
    for _ in tqdm.tqdm(range(BLINK)):
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[i] = 1
            elif len(str(arr[i])) % 2 == 0:
                num = str(arr[i])
                arr[i] = int(str(num)[:len(num)//2])
                arr.insert(i+1, int(str(num)[len(num)//2:]))
                i += 1
            else:
                arr[i] = arr[i] * 2024
            i += 1
    return len(arr)

def main():
    data = list(map(int, open(0).read().strip().split(" ")))
    print(part1(data))

if __name__ == "__main__":
    main()