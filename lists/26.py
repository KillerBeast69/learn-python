def check_ingredient_match(recipe, inventory):
    obtained = 0
    required = []
    for ingrediant in recipe:
        if ingrediant in inventory:
            obtained += 1
        else:
            required.append(ingrediant)
    return obtained, required