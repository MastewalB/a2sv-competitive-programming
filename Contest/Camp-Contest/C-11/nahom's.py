def solution(N, k):

    while len(N) > k:
        curr = 0
        count = 1
        R = []

        for i in range(len(N)):
            curr += int(N[i])
            if i == (count * k) - 1:
                R.append(str(curr))
                curr = 0
                count += 1

        if len(N) % k != 0:
            R.append(str(curr))
        N = ''.join(R)

    return N


print(solution("1100", 3
               ))
