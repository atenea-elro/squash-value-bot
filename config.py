import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
ODDS_REGIONS = os.getenv("ODDS_REGIONS", "eu")
ODDS_MARKETS = os.getenv("ODDS_MARKETS", "h2h")
SPORT_KEY = os.getenv("SPORT_KEY", "squash")  # puede variar en The Odds API

EDGE_MIN = float(os.getenv("EDGE_MIN", "0.05"))  # 5% edge mínimo
MAX_PICKS = int(os.getenv("MAX_PICKS", "3"))
SIM_N = int(os.getenv("SIM_N", "20000"))

K_FORM = float(os.getenv("K_FORM", "0.10"))
K_FATIGA = float(os.getenv("K_FATIGA", "0.02"))
K_H2H = float(os.getenv("K_H2H", "0.05"))

SEND_IF_NO_PICKS = os.getenv("SEND_IF_NO_PICKS", "true").lower() == "true"

def validate_config():
    missing = []
    if not TELEGRAM_TOKEN: missing.append("TELEGRAM_TOKEN")
    if not CHAT_ID: missing.append("CHAT_ID")
    if not ODDS_API_KEY: missing.append("ODDS_API_KEY")
    if missing:
        raise RuntimeError(f"Faltan secrets/env vars: {', '.join(missing)}")