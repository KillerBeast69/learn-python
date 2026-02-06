def area_sum(rectangles):
    total = 0
    for i in rectangles:
        h, w = i
        area = h * w
        total += area
    return total