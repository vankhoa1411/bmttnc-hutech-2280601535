def encrypt(text, key):
    result = ''
    key = key.upper()
    j = 0
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            offset = 65 if text[i].isupper() else 97
            result += chr((ord(text[i]) - offset + shift) % 26 + offset)
            j += 1
        else:
            result += text[i]
    return result
