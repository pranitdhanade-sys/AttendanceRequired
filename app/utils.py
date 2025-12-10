# app/utils.py
import math
from typing import Dict

def calc_needed(total: int, attended: int, target_pct: float) -> int:
    """
    Solve for minimal integer x >= 0 such that (attended + x) / (total + x) >= target_pct/100.
    Returns the minimal x (0 if already at/above target).
    If target_pct >= 100, function raises ValueError.
    """
    p = target_pct / 100.0
    if p >= 1.0:
        raise ValueError("target must be less than 100")

    numerator = p * total - attended
    if numerator <= 0:
        return 0
    denom = 1.0 - p
    x = math.ceil(numerator / denom - 1e-12)
    return max(0, x)


def calc_max_skip(total: int, attended: int, target_pct: float) -> int:
    """
    Largest integer s >= 0 such that attended / (total + s) >= p
    => s <= (attended / p) - total
    """
    p = target_pct / 100.0
    if p <= 0:
        raise ValueError("target must be > 0")
    max_s = math.floor(attended / p - total + 1e-12)
    return max(0, max_s)


def simulate_upcoming(total: int, attended: int, target_pct: float, upcoming: int) -> dict:
    """
    Given N upcoming classes, find minimal k (0..N) to attend so that overall >= target.
    Also compute final percentages if attend all or none.
    """
    p = target_pct / 100.0
    # minimal k such that (attended + k) / (total + upcoming) >= p
    needed_numer = math.ceil(p * (total + upcoming) - attended - 1e-12)
    min_k = max(0, needed_numer)
    if min_k > upcoming:
        will_reach = False
    else:
        will_reach = True

    pct_all = ((attended + upcoming) / (total + upcoming)) * 100.0 if (total + upcoming) > 0 else 0.0
    pct_none = (attended / (total + upcoming)) * 100.0 if (total + upcoming) > 0 else 0.0

    return {
        "upcoming": upcoming,
        "minAttendOfUpcoming": min_k,
        "willReachTarget": will_reach,
        "pctIfAttendAll": round(pct_all, 6),
        "pctIfAttendNone": round(pct_none, 6),
    }
