def calc_attendance(total: int, attended: int, target: float):
    current_pct = (attended / total * 100) if total > 0 else 0
    needed = max(0, int((target/100 * total - attended) + 0.9999))  # ceil
    max_skip = max(0, int(attended - target/100 * total))
    return {
        "currentPct": current_pct,
        "needed": needed,
        "maxSkip": max_skip
    }

def simulate_upcoming(total: int, attended: int, target: float, upcoming: int):
    min_attend = 0
    will_reach = False

    for i in range(upcoming + 1):
        if (attended + i) / (total + upcoming) * 100 >= target:
            min_attend = i
            will_reach = True
            break

    pct_if_attend_all = (attended + upcoming) / (total + upcoming) * 100 if total + upcoming > 0 else 0
    pct_if_attend_none = attended / (total + upcoming) * 100 if total + upcoming > 0 else 0

    return {
        "upcoming": upcoming,
        "minAttendOfUpcoming": min_attend,
        "willReachTarget": will_reach,
        "pctIfAttendAll": pct_if_attend_all,
        "pctIfAttendNone": pct_if_attend_none
    }
