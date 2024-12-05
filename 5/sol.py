from collections import defaultdict

def is_valid(pages, rules_pre, rules_post):
    expecting_count = defaultdict(int)
    seen_count = defaultdict(int)
    invalid = False
    for p in pages:
        seen_count[p] += 1
        for should_see in rules_post[p]:
            if seen_count[should_see] == 0:
                invalid = True
                break
            else:
                expecting_count[should_see] -= 1

        for expecting in rules_pre[p]:
            expecting_count[expecting] += 1
    return not (invalid or sum(expecting_count.values()) > 0)


with open(0) as f:
    data = f.read().splitlines()
    rules = set([r for r in data if "|" in r])
    pageList = [p.split(",") for p in data if len(p) > 0 and p not in rules]

    ans_1 = 0
    ans_2 = 0
    for pages in pageList:
        count = defaultdict(int)
        for p in pages:
            count[p] += 1
        rules_post = defaultdict(list)
        rules_pre = defaultdict(list)
        for rule in rules:
            if count[rule.split("|")[0]] > 0 and count[rule.split("|")[1]] > 0:
                # I am expecting this
                rules_pre[rule.split("|")[0]].append(rule.split("|")[1])
                # I should have seen this
                rules_post[rule.split("|")[1]].append(rule.split("|")[0])

        if is_valid(pages, rules_pre, rules_post):
            ans_1 += int(pages[len(pages)//2])
            continue

        # Part 2
        expecting_count = defaultdict(int)
        seen_count = defaultdict(int)
        corrected_pages = [_ for _ in pages]
        i = 0
        while i < len(corrected_pages):
            recount = False
            seen_count[corrected_pages[i]] += 1
            for should_see in rules_post[corrected_pages[i]]:
                if seen_count[should_see] == 0:
                    recount = True
                    swap_index = len(corrected_pages) - corrected_pages[::-1].index(should_see) - 1
                    corrected_pages[i], corrected_pages[swap_index] = corrected_pages[swap_index], corrected_pages[i]
                    break
                else:
                    expecting_count[should_see] -= 1

            if recount:
                continue

            for expecting in rules_pre[corrected_pages[i]]:
                expecting_count[expecting] += 1
            
            i += 1
            
            if i == len(corrected_pages) and not is_valid(corrected_pages, rules_pre, rules_post):
                expecting_count = defaultdict(int)
                seen_count = defaultdict(int)
                i = 0
        ans_2 += int(corrected_pages[len(corrected_pages)//2])

    print(ans_1)
    print(ans_2)
