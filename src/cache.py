from collections import OrderedDict, deque
import sys


def fifo(k, reqs):
    cache = deque()   
    cache_set = set()  
    miss_count = 0
    for r in reqs:
        if r not in cache_set:
            miss_count += 1
            if len(cache) == k:
                cache_set.remove(cache.popleft())
            cache.append(r)
            cache_set.add(r)
    return miss_count

def lru(k, reqs):
    cache = OrderedDict()
    miss_count = 0
    for r in reqs:
        if r in cache:
            cache.move_to_end(r)
        else:
            miss_count += 1
            if len(cache) == k:
                cache.popitem(last=False)
            cache[r] = True
    return miss_count


def optff(k, reqs):
    next_req = {}
    last_seen = {}
    for i in range(len(reqs) - 1, -1, -1):
        next_req[i] = last_seen.get(reqs[i], float('inf'))
        last_seen[reqs[i]] = i

    cache = set()
    cache_next = {} 
    miss_count = 0
    for i, r in enumerate(reqs):
        if r in cache:
            cache_next[r] = next_req[i]
        else:
            miss_count += 1
            if len(cache) == k:
                evict = max(cache, key=lambda x: cache_next[x])
                cache.remove(evict)
                del cache_next[evict]
            cache.add(r)
            cache_next[r] = next_req[i]
    return miss_count


def main():
    with open(sys.argv[1]) as f:
        k, m = map(int, f.readline().split())
        reqs = list(map(int, f.readline().split()))

    print(f"FIFO  : {fifo(k, reqs)}")
    print(f"LRU   : {lru(k, reqs)}")
    print(f"OPTFF : {optff(k, reqs)}")


if __name__ == "__main__":
    main()
