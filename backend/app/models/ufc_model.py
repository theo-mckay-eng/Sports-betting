import math
from typing import Dict

def elo_win_prob(elo_a: float, elo_b: float) -> float:
    """ELO expected win probability."""
    if elo_a == 0 and elo_b == 0:
        return 0.5
    diff = elo_a - elo_b
    try:
        return 1.0 / (1.0 + 10.0 ** (-diff / 400.0))
    except (OverflowError, ValueError):
        return 1.0 if diff > 0 else 0.0

def mma_model(fighter_a_wins: int, fighter_a_losses: int, fighter_b_wins: int, fighter_b_losses: int, fighter_a_finish_rate: float = 0.5, fighter_b_finish_rate: float = 0.5, fighter_a_elo: float = 1500, fighter_b_elo: float = 1500, fighter_a_reach_adv: float = 0.0, fighter_a_sig_strikes_pm: float = 4.5, fighter_b_sig_strikes_pm: float = 4.5, fighter_a_td_avg: float = 2.0, fighter_b_td_avg: float = 2.0, is_title_fight: bool = False) -> Dict:
    """Composite MMA win probability model."""
    total_a = fighter_a_wins + fighter_a_losses
    total_b = fighter_b_wins + fighter_b_losses
    wr_a = fighter_a_wins / max(1, total_a)
    wr_b = fighter_b_wins / max(1, total_b)
    
    elo_prob_a = elo_win_prob(fighter_a_elo, fighter_b_elo)
    
    strike_total = fighter_a_sig_strikes_pm + fighter_b_sig_strikes_pm
    strike_a = fighter_a_sig_strikes_pm / max(0.1, strike_total)
    
    td_total = fighter_a_td_avg + fighter_b_td_avg
    td_a = fighter_a_td_avg / max(0.1, td_total)
    
    reach_boost = fighter_a_reach_adv * 0.002
    
    prob_a = (wr_a * 0.20 + elo_prob_a * 0.35 + strike_a * 0.25 + td_a * 0.20) + reach_boost
    prob_a = max(0.05, min(0.95, prob_a))
    
    finish_prob = (fighter_a_finish_rate + fighter_b_finish_rate) / 2.0
    if is_title_fight:
        finish_prob *= 0.85
    
    finish_prob = max(0.0, min(1.0, finish_prob))
    
    return {
        "fighter_a_prob": prob_a,
        "fighter_b_prob": 1.0 - prob_a,
        "finish_prob": finish_prob,
        "decision_prob": 1.0 - finish_prob,
    }
