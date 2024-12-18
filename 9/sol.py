import sys
import heapq

def diff(t):
    return abs(t[1] - t[0])

def get_file_metadata(data):
    # (-starting index, ending index)
    # - because we want a max heap
    file_ranges = {}
    empty_ranges = []
    curr = 0
    file_heap = []
    for i in range(len(data)):
        if i % 2 == 0 and data[i] != '0':
            # File range
            file_ranges[i//2] = [(-curr, curr + int(data[i]) - 1)]
            heapq.heappush(file_heap, -i//2)
        elif i % 2 == 1 and data[i] != '0':
            # Empty range
            heapq.heappush(empty_ranges, (curr, curr + int(data[i]) - 1))
        curr += int(data[i])

    return file_ranges, empty_ranges, file_heap

def get_checksum(file_ranges):
    checksum = 0
    for id in file_ranges.keys():
        for file_range in file_ranges[id]:
            for index in range(-file_range[0], file_range[1]+1):
                checksum += id * index
    return checksum

def compress(file_ranges, empty_ranges, file_heap, fragment=True):
    skip_empty_spaces = []
    while len(file_heap) > 0 and (len(skip_empty_spaces) > 0 or len(empty_ranges) > 0):
        moved = False
        if len(empty_ranges) == 0 and len(skip_empty_spaces) > 0:
            # We can't move the file.
            heapq.heappop(file_heap)
            for er in skip_empty_spaces:
                heapq.heappush(empty_ranges, er)
            skip_empty_spaces = []
            continue
        file = -heapq.heappop(file_heap)
        empty_range = heapq.heappop(empty_ranges)
        (file_start, file_end) = heapq.heappop(file_ranges[file])
        file_range = (-file_start, file_end)

        if empty_range[0] > file_range[0]: 
            # Push the file back in
            heapq.heappush(file_ranges[file], (file_start, file_end))
            heapq.heappush(file_heap, -file)
            continue
        
        if diff(empty_range) == diff(file_range):
            heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[1]))
            moved = True
        elif diff(empty_range) < diff(file_range):
            if fragment:
                # Part 1
                heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[1]))
                heapq.heappush(file_ranges[file], (file_start, file_end - (diff(empty_range) + 1)))
                heapq.heappush(file_heap, -file)
                moved = True
            else:
                # Part 2
                skip_empty_spaces.append(empty_range)
                heapq.heappush(file_ranges[file], (file_start, file_end))
        elif diff(empty_range) > diff(file_range):
            heapq.heappush(file_ranges[file], (-empty_range[0], empty_range[0] + diff(file_range)))
            heapq.heappush(empty_ranges, (empty_range[0] + (diff(file_range) + 1), empty_range[1]))
            moved = True

        if moved and len(skip_empty_spaces) > 0:
            for er in skip_empty_spaces:
                heapq.heappush(empty_ranges, er)
            skip_empty_spaces = []
        
        if not moved:
            heapq.heappush(file_heap, -file)

    return get_checksum(file_ranges)

def main():
    data = open(sys.argv[1]).read()
    print(compress(*get_file_metadata(data)))
    print(compress(*get_file_metadata(data), fragment=False))

if __name__ == "__main__":
    main()