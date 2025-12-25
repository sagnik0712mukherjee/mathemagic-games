def calculate_highest_share():
    highest = []
    left = 100
    for i in range(1, 101):
        gets = (i/100) * (left)
        highest.append(gets)
        left -= gets

    h_idx = 0
    for j in range(0, len(highest) - 1):
        if highest[j+1] > highest[j]:
            h_idx = j + 1
    
    msg = f"highest is received by guest {h_idx + 1}."
    print(msg)
    return h_idx + 1

if __name__ == "__main__":
    calculate_highest_share()
