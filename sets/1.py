def remove_duplicates(spells):
    seen = set()
    unique = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique.append(spell)
    unique = set(unique)
    seen = [seen]
    return unique