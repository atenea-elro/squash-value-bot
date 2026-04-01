def ev(prob, odds):
    return prob * odds - 1.0

def pick_candidates(event, prob_j1, edge_min):
    picks = []
    
    # EV Ganador Equipo 1
    e1 = ev(prob_j1, event["odds_p1"])
    if e1 > edge_min:
        picks.append(("Ganador", event["player1"], event["odds_p1"], prob_j1, e1, "medio"))
        
    # EV Ganador Equipo 2
    e2 = ev(1 - prob_j1, event["odds_p2"])
    if e2 > edge_min:
        picks.append(("Ganador", event["player2"], event["odds_p2"], 1 - prob_j1, e2, "medio"))
        
    return sorted(picks, key=lambda x: x[4], reverse=True)
