import re

with open(0) as f:
    s = f.read().strip()
    regex = r'mul\(\d+,\d+\)'
    pat = re.findall(regex, s)
    t = 0
    # Part a
    for p in pat:
        a = list(map(int, p[4:-1].split(",")))
        t += a[0] * a[1]
    print(t)

    # Part b
    regex = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
    pat = re.findall(regex, s)
    include = True
    t2 = 0
    for p in pat:
        if p == "do()":
            include = True
        elif p == "don't()":
            include = False
        elif include:
            a = list(map(int, p[4:-1].split(",")))
            t2 += a[0] * a[1]
    print(t2)