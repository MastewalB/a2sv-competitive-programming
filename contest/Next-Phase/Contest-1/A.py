
lineland = list(map(int, input().split()))
lineland.sort()

minDist = lineland[1] - lineland[0] + lineland[2] - lineland[1]
print(minDist)
