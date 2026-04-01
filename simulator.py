import numpy as np

def simulate_set(p1, rng):
    s1 = 0
    s2 = 0
    while True:
        if rng.random() < p1:
            s1 += 1
        else:
            s2 += 1
        if (s1 >= 11 or s2 >= 11) and abs(s1 - s2) >= 2:
            return 1 if s1 > s2 else 2

def simulate_match(p1, rng):
    a = 0
    b = 0
    while a < 3 and b < 3:
        w = simulate_set(p1, rng)
        if w == 1:
            a += 1
        else:
            b += 1
    return a, b

def monte_carlo(p1, n=20000, seed=None):
    rng = np.random.default_rng(seed)
    counts = {"3-0":0,"3-1":0,"3-2":0,"0-3":0,"1-3":0,"2-3":0}
    for _ in range(n):
        a, b = simulate_match(p1, rng)
        counts[f"{a}-{b}"] += 1
    probs = {k: v/n for k, v in counts.items()}
    p1_win = probs["3-0"] + probs["3-1"] + probs["3-2"]
    over_3_5 = probs["3-2"] + probs["2-3"]
    return probs, p1_win, over_3_5