import sys
import heapq
import tqdm

def diff(t):
    return abs(t[1] - t[0])

def part1(data):
    # (-starting index, ending index)
    # - because we want a max heap
    file_ranges = {}
    empty_ranges = []
    curr = 0
    max_heap = []
    for i in range(len(data)):
        if i % 2 == 0 and data[i] != '0':
            # File range
            file_ranges[i//2] = [(-curr, curr + int(data[i]) - 1)]
            heapq.heappush(max_heap, -i//2)
        elif i % 2 == 1 and data[i] != '0':
            # Empty range
            heapq.heappush(empty_ranges, (curr, curr + int(data[i]) - 1))
        curr += int(data[i])

    while len(empty_ranges) > 0:
        file = -heapq.heappop(max_heap)
        empty_range = heapq.heappop(empty_ranges)
        (file_start, file_end) = heapq.heappop(file_ranges[file])
        file_range = (-file_start, file_end)

        if empty_range[0] > file_range[0]: 
            # Push the file back in
            heapq.heappush(file_ranges[file], (file_start, file_end))
            break

        if diff(empty_range) == diff(file_range):
            heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[1]))
        elif diff(empty_range) < diff(file_range):
            heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[1]))
            heapq.heappush(file_ranges[file], (file_start, file_end - (diff(empty_range) + 1)))
            heapq.heappush(max_heap, -file)
        elif diff(empty_range) > diff(file_range):
            heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[0] + diff(file_range)))
            heapq.heappush(empty_ranges, (empty_range[0] + (diff(file_range) + 1), empty_range[1]))

    # Checksum
    checksum = 0
    for id in tqdm.tqdm(file_ranges.keys()):
        for file_range in file_ranges[id]:
            for index in range(-file_range[0], file_range[1]+1):
                checksum += id * index
    return checksum
            

def main():
    data = open(sys.argv[1]).read()
    print(part1(data))

if __name__ == "__main__":
    main()