import math


def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return (root1, root2)
    elif D == 0:
        root = -b / (2 * a)
        return root
    else:
        return None


a = float(input("Enter the coefficient value a: "))
b = float(input("Enter the coefficient value b: "))
c = float(input("Enter the coefficient value c: "))

roots = solve_quadratic_equation(a, b, c)

if roots is None:
    print("The equation has no real roots")
elif isinstance(roots, tuple):
    print(f"The equation has two different roots: {roots}")
else:
    print(f"The equation has one root: {roots}")