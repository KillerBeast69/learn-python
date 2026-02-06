def calculate_experience_points(level):
    total = 0
    for current_lvl in range(1, level):
        xp = current_lvl * 5
        total += xp
    return total