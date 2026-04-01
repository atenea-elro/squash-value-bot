from config import (
    EDGE_MIN, MAX_PICKS, SIM_N, K_FORM, K_FATIGA, K_H2H,
    SEND_IF_NO_PICKS, validate_config
)
from odds_provider import fetch_odds, parse_h2h_events
from probability import no_vig_prob, point_p_from_match_win
from psa_data import get_features
from features import adjust_p
from simulator import monte_carlo
from value import pick_candidates
from telegram import send_telegram
from history_store import log_reco

def format_msg(picks_by_event):
    if not picks_by_event:
        return "❌ No hay picks con value hoy (según EDGE_MIN)."

    lines = ["📊 Picks con value (squash)\n"]
    for ev, p1_point, p1_win, picks in picks_by_event:
        lines.append(f"{ev['player1']} vs {ev['player2']}")
        lines.append(f"Book: {ev.get('book')} | H2H: {ev['odds_p1']} / {ev['odds_p2']}")
        lines.append(f"Modelo: p_point(P1)={p1_point:.3f} | p_win(P1)={p1_win:.3f}")
        for (market, sel, odds, prob, edge, risk) in picks:
            lines.append(f" - {market}: {sel} | odds {odds:.2f} | p {prob:.3f} | EV {edge:.3f} | riesgo {risk}")
        lines.append("")
    return "\n".join(lines).strip()

def run():
    validate_config()

    raw = fetch_odds()
    events = parse_h2h_events(raw)

    picks_out = []
    for ev in events:
        p1m, _ = no_vig_prob(ev["odds_p1"], ev["odds_p2"])
        p1_point_base = point_p_from_match_win(p1m)

        f1, f2 = get_features(ev["player1"], ev["player2"])
        p1_point = adjust_p(p1_point_base, f1, f2, K_FORM, K_FATIGA, K_H2H)

        score_probs, p1_win, over_3_5 = monte_carlo(p1_point, n=SIM_N)

        picks = pick_candidates(ev, p1_win, EDGE_MIN)[:MAX_PICKS]

        log_reco(ev, p1_point, p1_win, over_3_5, picks)

        if picks:
            picks_out.append((ev, p1_point, p1_win, picks))

    msg = format_msg(picks_out)
    if picks_out or SEND_IF_NO_PICKS:
        send_telegram(msg)

if __name__ == "__main__":
    run()