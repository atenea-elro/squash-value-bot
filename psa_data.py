from features import PlayerFeatures

def get_features(player1: str, player2: str):
    # Neutral por defecto
    f1 = PlayerFeatures(form=0.55, fatigue=3.0, h2h=0.5)
    f2 = PlayerFeatures(form=0.55, fatigue=3.0, h2h=0.5)
    return f1, f2