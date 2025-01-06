a = []

while True:
    b = input("Введите строку (или 'ENOUGH' для завершения): ")
    if b == "ENOUGH":
        break
    if len(b) < 4:
        print("LEARNED ALL")
        exit()
    a.append(b)

c = []

for i in range(len(a)):
    b = a[i]

    d = [b[j:j+4] for j in range(0, len(b), 4) if len(b[j:j+4]) == 4]

    if (i + 1) % 3 == 0:
        d = [group[::-1] for group in d]

    e = []
    for group in d:
        e.append(group[0].upper() + group[1:].lower())

    f = list(set(e))

    f.sort(reverse=True)

    c.append(f)

for i in range(len(c)):
    print(f"Строка {i+1}: {c[i]}")
