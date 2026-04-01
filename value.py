def ev(prob, odds):
    return prob * odds - 1.0

def pick_candidates(event, p1_win, edge_min):
    picks = []
    e1 = ev(p1_win, event["odds_p1"])
    e2 = ev(1 - p1_win, event["odds_p2"])

    if e1 > edge_min:
        picks.append(("h2h", event["player1"], event["odds_p1"], p1_win, e1, "medio"))
    if e2 > edge_min:
        picks.append(("h2h", event["player2"], event["odds_p2"], 1 - p1_win, e2, "medio"))

    return sorted(picks, key=lambda x: x[4], reverse=True)