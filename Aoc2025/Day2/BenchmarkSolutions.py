import time
import math as m

# DUMMY DATA FOR BENCHMARKING
ranges = [(100_000, 200_000), (900_000_000, 900_050_000)]

## Optimized Mathematical Approach Function
def solve_math(ranges):
    count = 0
    for r in ranges:
        for id in range(r[0], r[1] +1):
            # Get number of digits
            d = int(m.log10(id) + 1)
            for mask in get_mask(d):  # Retrieve from cache
                if id % mask == 0:
                    count += 1
                    break

    return count

mask_cache = {}
## Caching Method for Optimizing Math Approach
def get_mask(d):
    if d in mask_cache:
        return mask_cache[d]

    masks = []
    for l in range(1, (d//2) + 1):
        if d % l == 0:
            mask = (10 ** d - 1) // (10 ** l - 1)
            masks.append(mask)
    
    mask_cache[d] = masks
    return masks

## Optimized String Doubling Approach Function
def solve_string(ranges):
    count = 0
    for r in ranges:
        for id in range(r[0], r[1] +1):
            s = str(id)
            d = s + s
            if s in d[1:-1]:
                count += 1
    return count

# --- Bencmark Math Approach ---
start_time = time.perf_counter()
math_count = solve_math(ranges)
end_time = time.perf_counter()
print(f"Mathematical Approach:   {end_time - start_time:.4f} seconds (Found: {math_count})")

# --- Benchmark String Doubling Approach ---
start_time = time.perf_counter()
string_count = solve_string(ranges)
end_time = time.perf_counter()
print(f"String Doubling Approach: {end_time - start_time:.4f} seconds (Found: {string_count})")