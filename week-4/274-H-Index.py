def hIndex(citations):
    citations.sort()
    h = 0

    for i in range(len(citations) - 1, -1, -1):
        if citations[i] >= len(citations) - i:
            if i > 0 and citations[i - 1] > len(citations) - i:
                continue
            else:
                h = max(h, len(citations) - i)
                break

    return h
