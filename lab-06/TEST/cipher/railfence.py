def encrypt(text, key):
    rail = ['' for _ in range(key)]
    direction = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction = not direction
        row += 1 if direction else -1

    return ''.join(rail)
