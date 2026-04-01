import requests
from config import ODDS_API_KEY, ODDS_REGIONS, ODDS_MARKETS, SPORT_KEY

def fetch_odds():
    url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": ODDS_REGIONS,
        "markets": ODDS_MARKETS,
        "oddsFormat": "decimal"
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def parse_h2h_events(raw):
    out = []
    for ev in raw:
        home = ev.get("home_team")
        away = ev.get("away_team")
        books = ev.get("bookmakers") or []
        if not (home and away and books):
            continue

        # toma el primer bookmaker con mercado h2h disponible
        picked = None
        for b in books:
            for m in (b.get("markets") or []):
                if m.get("key") == "h2h":
                    outcomes = m.get("outcomes") or []
                    odds_map = {o.get("name"): o.get("price") for o in outcomes}
                    if home in odds_map and away in odds_map:
                        picked = (b, odds_map)
                        break
            if picked:
                break

        if not picked:
            continue

        b, odds_map = picked
        out.append({
            "event_id": ev.get("id"),
            "commence_time": ev.get("commence_time"),
            "player1": home,
            "player2": away,
            "book": b.get("key"),
            "odds_p1": float(odds_map[home]),
            "odds_p2": float(odds_map[away]),
        })
    return out