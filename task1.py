import math
def distance(x1, y1, x2, y2):
    x1 = float(input("Введите x₁: "))
    y1 = float(input("Введите y₁: "))
    x2 = float(input("Введите x₂: "))
    y2 = float(input("Введите y₂: "))
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

answer = distance(x1, y1, x2, y2)
print(f"Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно {answer}")