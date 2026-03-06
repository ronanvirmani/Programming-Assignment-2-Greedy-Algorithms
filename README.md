# Programming-Assignment-2-Greedy-Algorithms

## Student Information

- **Name:** Ronan Virmani
- **UFID:** 28617437

## Run Instructions

```bash
python3 src/cache.py <input_file>
```

## Assumptions

- Python 3.6+
- Input: first line is `k m`, second line is `m` space-separated integers

---

## Written Component

### Question 1: Empirical Comparison

| Input File | k | m | FIFO | LRU | OPTFF |
|------------|---|---|------|-----|-------|
| tests/test1.in | 5 | 60 | 45 | 45 | 29 |
| tests/test2.in | 3 | 60 | 40 | 22 | 22 |
| tests/test3.in | 4 | 55 | 41 | 41 | 25 |

**Does OPTFF have the fewest misses?** Yes, with all 3 tests.

**How does FIFO compare to LRU?** LRU outperforms FIFO on test2 (22 vs 40 misses) because pages 1 and 2 are accessed frequently, and LRU keeps them while FIFO evicts them. 

### Question 2: Bad Sequence for LRU

For k = 3, sequence: `1 2 3 4 1 2 3 4 1 2 3 4`

| Policy | Misses |
|--------|--------|
| LRU | 12 |
| OPTFF | 6 |

**Reasoning:** There are k+1 pages in a cycle causing LRU to evict the page needed next. OPTFF looks ahead and keeps these pages needed.

### Question 3: Prove OPTFF is Optimal

**Theorem:** OPTFF incurs no more misses than any offline algorithm A.

**Pf. [by Exchange Argument]:**

Let A be any optimal algorithm. We can turn A into OPTFF w/o increasing misses.

**Setup:** At some request i, both algorithms have the same things in their cache, but on a cache miss they evict different pages:
- OPTFF evicts page f (the page used farthest in the future)
- A evicts page p, where p != f

Now say we have A' that evicts f instead of p at position i.

**Case 1: Page f is never requested again.**
Evicting f causes no future misses. A' has the same misses as A.

**Case 2: Page p is requested at position k, and f is requested at position j, where k < j.**
- At position k: A hits, A' misses
- At position j: A misses, A' hits

A' just exchanges one miss for one hit, leaving the total misses the same as before.

**Case 3: Page p is never requested again, or is requested after f.**
Keeping p instead of f gives A no benefit. A' has ≤ misses as A.

**Conclusion:** In all the cases, A' has no more misses than A, and A' agrees with OPTFF on one more eviction. By repeated exchange, any optimal algorithm can be transformed to OPTFF w/o increasing misses.

Therefore OPTFF is optimal.
