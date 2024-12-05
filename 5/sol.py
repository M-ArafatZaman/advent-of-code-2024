from collections import defaultdict

with open(0) as f:
    data = f.read().splitlines()
    rules = set([r for r in data if "|" in r])
    pages = [p.split(",") for p in data if len(p) > 0 and p not in rules]

    ans_1 = 0
    for p in pages:
        # Check p
        count = defaultdict(int)
        for pp in p:
            count[pp] += 1
        rules_post = defaultdict(list)
        rules_pre = defaultdict(list)
        rules_to_check = []
        for rule in rules:
            if count[rule.split("|")[0]] > 0 and count[rule.split("|")[1]] > 0:
                rules_to_check.append(rule)
                # I am expecting this
                rules_pre[rule.split("|")[0]].append(rule.split("|")[1])
                # I should have seen this
                rules_post[rule.split("|")[1]].append(rule.split("|")[0])

        expecting_count = defaultdict(int)
        seen_count = defaultdict(int)
        invalid = False
        for pp in p:
            seen_count[pp] += 1
            for should_see in rules_post[pp]:
                if seen_count[should_see] == 0:
                    invalid = True
                    break
                else:
                    expecting_count[should_see] -= 1

            for expecting in rules_pre[pp]:
                expecting_count[expecting] += 1
        # I should've met my expecations 
        # So they should be 0
        
        if not (invalid or sum(expecting_count.values()) > 0):
            ans_1 += int(p[len(p)//2])
    print(ans_1)




