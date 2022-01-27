keyword = "TUES" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace('J', "")
cipher = [c for i, c in enumerate(keyword) if c not in (keyword)[:i]]

phrase = "jica e na baba ti prostoraa".replace(' ', "").upper().replace('J', 'I')
for i, _ in enumerate(phrase):
    if phrase[i] == phrase[i - 1] and i % 2:
        phrase = phrase[:i] + 'X' + phrase[i:]
phrase += (len(phrase) % 2) * 'X'
cut = [phrase[i:i + 2] for i in range(0, len(phrase), 2)]

encoded = ""
for l in cut:
    pos = []
    for c in l:
        for i, cc in enumerate(cipher):
            if cc == c:
                pos.append(i)
    if pos[0] % 5 == pos[1] % 5:
        encoded += cipher[(((pos[0] + 5) // 5) % 5) * 5 + pos[0] % 5] + cipher[(((pos[1] + 5) // 5) % 5) * 5 + pos[1] % 5]
    elif pos[0] // 5 == pos[1] // 5:
        encoded += cipher[(pos[0] // 5) * 5 + (pos[0] + 1) % 5] + cipher[(pos[1] // 5) * 5 + (pos[1] + 1) % 5]
    else:
        encoded += cipher[(pos[0] // 5) * 5 + pos[1] % 5] + cipher[(pos[1] // 5) * 5 + pos[0] % 5]

cut = [encoded[i:i + 2] for i in range(0, len(encoded), 2)]
decoded = ""
for l in cut:
    pos = []
    for c in l:
        for i, cc in enumerate(cipher):
            if cc == c:
                pos.append(i)
    if pos[0] % 5 == pos[1] % 5:
        decoded += cipher[(((pos[0] - 5) // 5) % 5) * 5 + pos[0] % 5] + cipher[(((pos[1] - 5) // 5) % 5) * 5 + pos[1] % 5]
    elif pos[0] // 5 == pos[1] // 5:
        decoded += cipher[(pos[0] // 5) * 5 + (pos[0] - 1) % 5] + cipher[(pos[1] // 5) * 5 + (pos[1] - 1) % 5]
    else:
        decoded += cipher[(pos[0] // 5) * 5 + pos[1] % 5] + cipher[(pos[1] // 5) * 5 + pos[0] % 5]

for i in range(0, 5):
    for j in range(0, 5):
        print(cipher[(i * 5) + j], end = ' ')
    print()
print(encoded)
print(decoded)
print(phrase == decoded)
