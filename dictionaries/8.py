def get_most_common_enemy(enemies_dict):
    maxi = 0
    enemy = None
    for name in enemies_dict:
        count = enemies_dict[name]
        if count > maxi:
            maxi = count
            enemy = name
    return enemy