def solve_quadratic(a, b, c):
    discriminant = (b**2 - 4*a*c)
    x1 = (-b + discriminant ** 0.5) / (2*a)
    x2 = (-b - discriminant ** 0.5) / (2*a)
    result = f'the roots of the equation are ({x1}, {x2}).'
    print(result)
    return x1, x2

if __name__ == "__main__":
    solve_quadratic(1, -7, 12)
