def convert(s, nRows):
    if nRows == 1:
        return s

    gap = (nRows - 1) * 2
    ans = []
    idx = 0
    step = gap

    for i in range(0, nRows):
        if i >= len(s):
            break
        j = 0
        ans.append(s[i])
        while True:
            if 0 < step < gap:
                if i + step + gap * j < len(s):
                    ans.append(s[i + step + gap * j])
                else:
                    break

            if i + gap * (j + 1) < len(s):
                ans.append(s[i + gap * (j + 1)])
            else:
                break
            j += 1
        step -= 2

    return ''.join(ans)

print(convert("PAYPALISHIRING", 4))
print(convert("A", 2))
