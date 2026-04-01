def no_vig_prob(odds1: float, odds2: float):
    p1 = 1.0 / odds1
    p2 = 1.0 / odds2
    s = p1 + p2
    return p1 / s, p2 / s

def point_p_from_match_win(p_match):
    p_match = max(0.05, min(0.95, p_match))
    return 0.5 + (p_match - 0.5) * 0.65