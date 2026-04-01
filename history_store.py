import pandas as pd
from datetime import datetime

FILE = "history.csv"

def log_reco(event, p1_point, p1_win, over_3_5, picks):
    row = {
        "ts": datetime.utcnow().isoformat(),
        "event_id": event.get("event_id"),
        "commence_time": event.get("commence_time"),
        "player1": event["player1"],
        "player2": event["player2"],
        "book": event.get("book"),
        "odds_p1": event["odds_p1"],
        "odds_p2": event["odds_p2"],
        "p1_point": p1_point,
        "p1_win": p1_win,
        "over_3_5": over_3_5,
        "picks": str(picks),
    }
    try:
        df = pd.read_csv(FILE)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    except Exception:
        df = pd.DataFrame([row])
    df.to_csv(FILE, index=False)