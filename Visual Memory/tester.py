color = (37, 115, 193)
result_color = tuple(c1 - c2 for c1, c2 in zip((33,33,33), color))

print(result_color)