import numpy as np

def simular_puntos_partido(media_puntos_total, handicap, n=10000):
    # Simulamos 10.000 partidos basados en la media de puntos esperada
    # Usamos una distribución normal para el basket
    rng = np.random.default_rng()
    
    # Estimamos puntos de cada equipo
    puntos_j1 = rng.normal(media_puntos_total/2 - handicap/2, 12, n)
    puntos_j2 = rng.normal(media_puntos_total/2 + handicap/2, 12, n)
    
    victorias_j1 = np.sum(puntos_j1 > puntos_j2)
    prob_j1 = victorias_j1 / n
    
    return prob_j1, puntos_j1, puntos_j2

def calcular_ev(prob, cuota):
    return (prob * cuota) - 1
