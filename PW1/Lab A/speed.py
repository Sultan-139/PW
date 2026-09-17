import time
import decay

N0 = 200000
lam = 0.4

t0 = time.perf_counter()
res_loop = decay.simulate_loop(N0, lam)
t1 = time.perf_counter()
time_loop = t1 - t0


t0 = time.perf_counter()
res_numpy = decay.simulate(N0, lam)
t1 = time.perf_counter()
time_numpy = t1 - t0

speedup = time_loop / time_numpy

print(f"Pure-Python time: {time_loop:.4f} seconds")
print(f"NumPy time:       {time_numpy:.4f} seconds")
print(f"NumPy is {speedup:.2f}x faster than Python loop")