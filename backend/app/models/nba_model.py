import math
from typing import Dict, Tuple

def nba_score_prob(avg_pts_home: float, avg_pts_away: float, avg_pts_allowed_home: float, avg_pts_allowed_away: float) -> Tuple[float, float]:
    """Offensive/defensive rating model for basketball."""
    exp_home = (avg_pts_home + avg_pts_allowed_away) / 2
    exp_away = (avg_pts_away + avg_pts_allowed_home) / 2
    
    if exp_home + exp_away == 0:
        return 0.5, 0.5
    
    diff = exp_home - exp_away
    try:
        prob_home = 1.0 / (1.0 + math.exp(-diff / 6.0))
    except (OverflowError, ValueError):
        prob_home = 1.0 if diff > 0 else 0.0
    
    return prob_home, 1.0 - prob_home

def elo_win_prob(elo_home: float, elo_away: float, home_advantage: float = 65) -> float:
    """ELO expected win probability for home team."""
    if elo_home == 0 and elo_away == 0:
        return 0.5
    
    diff = elo_home + home_advantage - elo_away
    try:
        return 1.0 / (1.0 + 10.0 ** (-diff / 400.0))
    except (OverflowError, ValueError):
        return 1.0 if diff > 0 else 0.0

def nba_model(home_pts: float, away_pts: float, home_allowed: float, away_allowed: float, home_elo: float = 1500, away_elo: float = 1500, home_last5_wins: int = 3, away_last5_wins: int = 3, home_b2b: bool = False, away_b2b: bool = False) -> Dict:
    """Multi-factor NBA win probability model."""
    base_home, base_away = nba_score_prob(home_pts, away_pts, home_allowed, away_allowed)
    elo_home = elo_win_prob(home_elo, away_elo, home_advantage=35)
    
    form_home = home_last5_wins / 5.0
    form_away = away_last5_wins / 5.0
    form_adj = (form_home - form_away) * 0.05
    
    fatigue = (-0.04 if home_b2b else 0.0) + (0.04 if away_b2b else 0.0)
    
    blended_home = (base_home * 0.45 + elo_home * 0.40 + 0.5 * 0.15) + form_adj + fatigue
    blended_home = max(0.05, min(0.95, blended_home))
    
    exp_home = (home_pts + away_allowed) / 2.0
    exp_away = (away_pts + home_allowed) / 2.0
    spread = exp_home - exp_away
    total = exp_home + exp_away
    
    return {
        "home_prob": blended_home,
        "away_prob": 1.0 - blended_home,
        "exp_home": exp_home,
        "exp_away": exp_away,
        "spread": spread,
        "total": total,
    }
