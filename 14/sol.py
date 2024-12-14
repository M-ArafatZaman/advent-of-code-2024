WIDE = 101
TALL = 103

def main():
    data = [ [list(map(int, j.split("=")[1].split(","))) for j in i.split(" ")] for i in open(0).read().splitlines() ]
    p, v = list(map(list, list(zip(*data))))
        
    sec = 100
    for i in range(len(p)):
        x, y = p[i]
        p[i] = ( (x + sec * v[i][0]) % WIDE , (y + sec * v[i][1]) % TALL )
    
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y in p:
        if x < WIDE // 2 and y < TALL // 2: q1 += 1
        if x > WIDE // 2 and y < TALL // 2: q2 += 1
        if x < WIDE // 2 and y > TALL // 2: q3 += 1
        if x > WIDE // 2 and y > TALL // 2: q4 += 1

    print(q1*q2*q3*q4)

if __name__ == "__main__":
    main()