def find_missing_ids(first_ids, second_ids):
    new = set()
    for ids in first_ids:
        if ids not in second_ids:
            new.add(ids)
    