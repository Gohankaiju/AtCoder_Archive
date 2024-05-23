def solution(island, trip):

    ans = 0
    before = 0

    for c in trip:
        #print(island.find(c))
        ans += abs(island.find(c) - before)
        before = island.find(c)

    #print(f"ans={ans}")
    return ans