def pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]  # First element is always 1
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    
    for i in range(rows):
        print(" " * (rows - i - 1) + " ".join(map(str, triangle[i])))

pascals_triangle(5)
