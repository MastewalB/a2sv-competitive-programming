def spiralOrder(matrix):
    output = []
    m = len(matrix)
    n = len(matrix[0])
    processed = 0

    while len(output) < m * n:
        for i in range(processed, n - processed):
            output.append(matrix[processed][i])
        for j in range(processed + 1, m - processed):
            output.append(matrix[j][n - processed - 1])
        if len(output) == m*n:
            break
        for i in range(n - processed - 2, processed - 1, -1):
            output.append(matrix[m - processed - 1][i])
        for j in range(m - processed - 2, processed, -1):
            output.append(matrix[j][processed])
        if len(output) == (m*n):
            break

        processed += 1

    return output

# 110min
