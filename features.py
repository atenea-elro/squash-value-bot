from dataclasses import dataclass

@dataclass
class PlayerFeatures:
    form: float      # 0..1
    fatigue: float   # 0..10 (más = peor)
    h2h: float       # 0..1 (0.5 desconocido)

def adjust_p(p_base, f1: PlayerFeatures, f2: PlayerFeatures, k_form, k_fatigue, k_h2h):
    adj_form = (f1.form - f2.form) * k_form
    adj_fat  = (f2.fatigue - f1.fatigue) * k_fatigue
    adj_h2h  = (f1.h2h - 0.5) * k_h2h

    p = p_base + adj_form + adj_fat + adj_h2h
    return max(0.35, min(0.65, p))