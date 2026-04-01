from config import EDGE_MIN, MAX_PICKS, validate_config, SEND_IF_NO_PICKS
from odds_provider import fetch_odds, parse_h2h_events
from probability import no_vig_prob
from model import simular_puntos_partido, calcular_ev
from value import pick_candidates
from telegram import send_telegram

def format_msg(picks_by_event):
    if not picks_by_event:
        return "❌ No hay picks de Basket con valor hoy."

    lines = ["🏀 PICKS DE BASKETBALL (NBA/Euro)\n"]
    for ev, prob, picks in picks_by_event:
        lines.append(f"🔥 {ev['player1']} vs {ev['player2']}")
        lines.append(f"Cuotas: {ev['odds_p1']} / {ev['odds_p2']}")
        for (market, sel, odds, prob_val, edge, risk) in picks:
            lines.append(f" ✅ {market}: {sel} | Cuota {odds:.2f} | EV {edge:.3f}")
        lines.append("")
    return "\n".join(lines).strip()

def run():
    validate_config()
    raw = fetch_odds()
    events = parse_h2h_events(raw)

    picks_out = []
    for ev in events:
        # Sacamos la probabilidad implícita de las cuotas
        p1_prob_mercado, _ = no_vig_prob(ev["odds_p1"], ev["odds_p2"])
        
        # El modelo de basket analiza si la cuota está mal puesta
        picks = pick_candidates(ev, p1_prob_mercado, EDGE_MIN)[:MAX_PICKS]

        if picks:
            picks_out.append((ev, p1_prob_mercado, picks))

    msg = format_msg(picks_out)
    if picks_out or SEND_IF_NO_PICKS:
        send_telegram(msg)

if __name__ == "__main__":
    run()
