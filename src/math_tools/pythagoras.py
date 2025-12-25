def find_triplets(lower, upper):
    results = []
    for a in range(lower, upper):
        for b in range(lower, upper):
            for c in range(lower, upper):
                if (a**2) + (b**2) == c**2 and a != 0 and b != 0 and c != 0:
                    msg = f"base = {a} units, height = {b} units and hypotenuse = {c} units are pythagorean triplets"
                    print(msg)
                    results.append((a, b, c))
    return results

if __name__ == "__main__":
    find_triplets(0, 20)
